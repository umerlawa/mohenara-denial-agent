"""The two budgets must never mix.

Bedrock carries $50 for the build; the Anthropic API carries $9 for the
frontier-comparison phase only. The failure this guards against is a single
shared counter: exhausting one budget would then block the other, or worse,
spending on one would quietly consume the other's headroom.

Offline. Uses a temp ledger; touches no real spend file and calls no API.
"""
from __future__ import annotations

import json
import pathlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))

from mohenara import config, spend  # noqa: E402

USAGE = {"input_tokens": 100, "output_tokens": 10,
         "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0}


@pytest.fixture(autouse=True)
def committed_caps(monkeypatch):
    """Run every test at the caps the repository ships, whatever the box is set to.

    `mohenara/env.py` loads .env.local at package import -- including under
    pytest -- and lets it override the ambient environment, by design, because
    two entry points once disagreed about credentials. The side effect was that
    a deployment doing the thing CLAUDE.md tells it to do (`export
    MOHENARA_BUDGET_ANTHROPIC=250` before a demo) turned three of these tests
    red. The tests were the wrong ones: they exercise the gate MECHANISM, and a
    mechanism test that inherits the local deployment's numbers is not hermetic.

    So the ambient overrides are cleared for the duration. The one test that
    genuinely asserts the shipped numbers reads them through
    `config.committed_provider`, which never consults the environment at all.
    """
    for name in config.provider_names():
        monkeypatch.delenv(f"MOHENARA_BUDGET_{name.upper()}", raising=False)
        monkeypatch.delenv(f"MOHENARA_STOP_{name.upper()}", raising=False)


@pytest.fixture
def ledger(tmp_path) -> pathlib.Path:
    return tmp_path / "spend.json"


def test_the_two_providers_are_configured_separately():
    """The guardrails the repository SHIPS, not what this box is running at.

    Read through committed_provider, so raising a cap for a demo -- which
    CLAUDE.md explicitly tells a deployment to do -- cannot turn this red.
    """
    bedrock = config.committed_provider("bedrock")
    anthropic = config.committed_provider("anthropic")
    # Raised 50 -> 100 on 2026-09-04, when serving moved onto Bedrock and the
    # AWS credits became the funded route. This pin exists so a cap changes
    # only the way this one did: deliberately, config and test together.
    assert bedrock["budget_usd"] == 100.00
    assert bedrock["stop_eval_usd"] == 90.00
    assert anthropic["budget_usd"] == 9.00
    assert anthropic["stop_eval_usd"] == 8.00
    assert bedrock is not anthropic


def test_a_deployment_may_raise_a_cap_without_the_shipped_one_changing():
    """The two readings are different questions and must stay different answers."""
    import os

    os.environ["MOHENARA_BUDGET_ANTHROPIC"] = "250"
    os.environ["MOHENARA_STOP_ANTHROPIC"] = "200"
    try:
        assert config.provider("anthropic")["budget_usd"] == 250.00
        assert config.committed_provider("anthropic")["budget_usd"] == 9.00
    finally:
        del os.environ["MOHENARA_BUDGET_ANTHROPIC"]
        del os.environ["MOHENARA_STOP_ANTHROPIC"]


def test_spending_on_bedrock_does_not_consume_the_anthropic_budget(ledger):
    spend.record(run_id="r", case_id="c", model="opus-4-6", effort="high",
                 usage=USAGE, cost=95.0, path=ledger)
    assert spend.provider_total("bedrock", ledger) == 95.0
    assert spend.provider_total("anthropic", ledger) == 0.0
    # Bedrock is now past its eval stop...
    with pytest.raises(spend.BudgetExceeded):
        spend.check_before_call(model_name="opus-4-6", is_eval_run=True, path=ledger)
    # ...and Anthropic is untouched.
    spend.check_before_call(model_name="opus-5", is_eval_run=True, path=ledger)


def test_spending_on_anthropic_does_not_consume_the_bedrock_budget(ledger):
    spend.record(run_id="r", case_id="c", model="opus-5", effort="high",
                 usage=USAGE, cost=8.5, path=ledger)
    assert spend.provider_total("anthropic", ledger) == 8.5
    assert spend.provider_total("bedrock", ledger) == 0.0
    with pytest.raises(spend.BudgetExceeded):
        spend.check_before_call(model_name="opus-5", is_eval_run=True, path=ledger)
    spend.check_before_call(model_name="opus-4-6", is_eval_run=True, path=ledger)


def test_anthropic_refuses_at_its_own_ceiling_not_bedrocks(ledger):
    spend.record(run_id="r", case_id="c", model="sonnet-5", effort="low",
                 usage=USAGE, cost=9.0, path=ledger)
    # $9 is far below Bedrock's $50, but it is Anthropic's hard ceiling.
    with pytest.raises(spend.BudgetExceeded, match="anthropic"):
        spend.check_before_call(model_name="sonnet-5", path=ledger)


def test_entries_are_attributed_to_a_provider(ledger):
    spend.record(run_id="r", case_id="c1", model="opus-4-6", effort="high",
                 usage=USAGE, cost=1.0, path=ledger)
    spend.record(run_id="r2", case_id="c2", model="opus-5", effort="high",
                 usage=USAGE, cost=2.0, path=ledger)
    entries = json.loads(ledger.read_text())["entries"]
    assert {e["provider"] for e in entries} == {"bedrock", "anthropic"}


def test_an_unpriced_model_raises_rather_than_costing_nothing(monkeypatch):
    """A null rate must raise, never silently cost $0.00.

    This used to assert that opus-5 and sonnet-5 specifically had null rates,
    which stopped being true the moment their pricing was looked up for the
    comparison phase. That made the test a record of a transient state rather
    than of the invariant. The invariant is what matters: ANY model without
    rates must raise, because a silent zero makes the budget ceiling
    unenforceable.
    """
    from mohenara import config, pricing

    cfg = json.loads(pathlib.Path(config.CONFIG_PATH).read_text())
    cfg["models"]["unpriced-probe"] = {
        "provider": "anthropic", "id": "claude-unpriced-probe",
        "efforts": ["low"], "rates": None,
    }
    monkeypatch.setattr(config, "_cfg", lambda: cfg)
    pricing.rates_for.cache_clear() if hasattr(pricing.rates_for, "cache_clear") else None

    with pytest.raises(KeyError, match="no rates"):
        pricing.cost_usd("unpriced-probe", input_tokens=1000, output_tokens=1000)


def test_frontier_rates_are_populated_and_sourced():
    """The comparison phase may not run on guessed pricing.

    Rates must be present, positive, and carry a note saying where they came
    from -- an unsourced number in this file is indistinguishable from one
    recalled from memory.
    """
    from mohenara import config
    for name in ("opus-5", "sonnet-5"):
        spec = config.model(name)
        rates = spec.get("rates")
        assert rates, f"{name} has no rates; the comparison phase cannot price itself"
        for field in ("input", "output", "cache_write_5m", "cache_read"):
            assert rates.get(field, 0) > 0, f"{name}.{field} is missing or non-positive"
        # Cache multipliers are fixed by the published pricing table.
        assert rates["cache_write_5m"] == pytest.approx(rates["input"] * 1.25)
        assert rates["cache_read"] == pytest.approx(rates["input"] * 0.1)
        assert "rates_note" in spec and spec["rates_note"].strip()


def test_a_corrupt_ledger_is_not_read_as_zero_spend(ledger):
    ledger.write_text("{not json")
    with pytest.raises(RuntimeError, match="corrupt|unreadable"):
        spend.load(ledger)


def test_the_ledger_path_is_overridable(tmp_path, monkeypatch):
    """A checkout outside the working tree must still account to one budget.

    Without the override, a second checkout starts from a $0 ledger and spends
    real money the enforced ceiling never sees.
    """
    import importlib
    import json

    recorded = json.loads(spend.SPEND_RECORD.read_text())["providers"]["bedrock"]["usd"]

    target = tmp_path / "elsewhere" / "spend.json"
    monkeypatch.setenv("MOHENARA_SPEND_PATH", str(target))
    reloaded = importlib.reload(spend)
    try:
        assert reloaded.SPEND_PATH == target.resolve()
        reloaded.record(run_id="r", case_id="c", model="opus-4-6", effort="low",
                        usage=USAGE, cost=1.25)
        assert target.exists(), "spend went somewhere other than the override"
        # Redirected AND seeded. This test used to expect a bare $1.25, which is
        # the very hole its own docstring describes: a redirected ledger that
        # starts at zero lets a second deployment re-spend a budget the record
        # already accounts for. It now starts from the committed record.
        assert reloaded.provider_total("bedrock") == pytest.approx(recorded + 1.25)
    finally:
        monkeypatch.delenv("MOHENARA_SPEND_PATH", raising=False)
        importlib.reload(spend)


# --- no spending path may bypass the gate -----------------------------------

API_CALL_PATTERNS = (
    ".converse(",        # boto3 bedrock-runtime
    ".invoke_model(",    # boto3 bedrock-runtime
    "query(prompt",      # claude_agent_sdk
)
GATE_MARKERS = ("check_before_call", "check_provider")


def _python_sources() -> list[pathlib.Path]:
    roots = [REPO / "src", REPO / "eval", REPO / "tools"]
    return [p for root in roots if root.is_dir() for p in root.rglob("*.py")]


def test_every_file_that_calls_the_api_also_gates_and_records():
    """A call that spends must be gated before and recorded after.

    tools/bedrock_preflight.py once walked a ladder of ten models through boto3
    directly: no gate, no ledger entry. Small money, but spend the ceiling
    could never see -- and CLAUDE.md claims both budgets are gated in spend.py
    before every call. This makes that claim testable rather than aspirational.
    """
    offenders = []
    for path in _python_sources():
        if path.name.startswith("test_"):
            continue
        text = path.read_text()
        if not any(pat in text for pat in API_CALL_PATTERNS):
            continue
        if not any(marker in text for marker in GATE_MARKERS):
            offenders.append(f"{path.relative_to(REPO)}: calls the API, never gates")
        elif "spend.record" not in text and "record(" not in text:
            offenders.append(f"{path.relative_to(REPO)}: gates but never records")
    assert not offenders, "\n".join(offenders)


def test_an_unregistered_model_is_priced_above_zero_not_at_zero():
    """A probe of a model the registry does not carry must still cost something.

    The ladder exists to discover which model ids are real, so most of them are
    unregistered by construction. Pricing those at $0.00 would let a preflight
    walk past an exhausted budget without moving the number.
    """
    bound = spend.upper_bound_rates("bedrock")
    for field in ("input", "output", "cache_write_5m", "cache_read"):
        assert bound[field] > 0, f"upper bound for {field} is not positive"
    # It must genuinely be an upper bound, not just some model's rates.
    from mohenara import config
    for name, spec in config.all_models().items():
        if spec.get("provider") != "bedrock" or not spec.get("rates"):
            continue
        for field, value in spec["rates"].items():
            assert bound[field] >= value, f"{name}.{field} exceeds the bound"


# --- env overrides: a deployment sets its own caps without a tracked edit ---

def test_budget_caps_are_env_overridable(monkeypatch):
    """A demo or production deployment has different limits from a build.

    Editing config/models.json to say so means a merge conflict on every pull,
    so the caps come from the environment when set. The gate, the per-call
    accounting and the provider separation are unchanged by this.
    """
    from mohenara import config

    monkeypatch.setenv("MOHENARA_BUDGET_ANTHROPIC", "250")
    monkeypatch.setenv("MOHENARA_STOP_ANTHROPIC", "200")
    p = config.provider("anthropic")
    assert (p["budget_usd"], p["stop_eval_usd"]) == (250.0, 200.0)

    monkeypatch.delenv("MOHENARA_BUDGET_ANTHROPIC")
    monkeypatch.delenv("MOHENARA_STOP_ANTHROPIC")
    assert config.provider("anthropic")["budget_usd"] == 9.0


def test_an_unparseable_budget_raises_rather_than_defaulting(monkeypatch):
    """A cap the guard cannot read must not quietly become the old cap."""
    from mohenara import config

    monkeypatch.setenv("MOHENARA_BUDGET_BEDROCK", "two hundred")
    with pytest.raises(ValueError, match="not a number"):
        config.provider("bedrock")


def test_a_stop_above_the_ceiling_is_rejected(monkeypatch):
    """Otherwise the eval stop can never fire and eval runs reach the hard cap.

    This is the mistake a hurried demo setup actually makes: raise the ceiling,
    forget the stop, and lose the protection that keeps a stray eval run from
    eating the budget the live demo depends on.
    """
    from mohenara import config

    monkeypatch.setenv("MOHENARA_BUDGET_BEDROCK", "60")
    monkeypatch.setenv("MOHENARA_STOP_BEDROCK", "100")
    with pytest.raises(ValueError, match="above the refuse ceiling"):
        config.provider("bedrock")


def test_the_gate_honours_an_overridden_cap(monkeypatch, ledger):
    """The override must reach the guard, not just the config reader."""
    from mohenara import config  # noqa: F401

    # Past the $100 default ceiling, so the gate must refuse...
    spend.record(run_id="r", case_id="c", model="opus-4-6", effort="low",
                 usage=USAGE, cost=101.0, path=ledger)
    with pytest.raises(spend.BudgetExceeded):
        spend.check_before_call(model_name="opus-4-6", path=ledger)

    # ...and must allow the same spend once the ceiling is raised above it.
    monkeypatch.setenv("MOHENARA_BUDGET_BEDROCK", "200")
    monkeypatch.setenv("MOHENARA_STOP_BEDROCK", "180")
    spend.check_before_call(model_name="opus-4-6", path=ledger)

    # The soft stop must still bite after an override. Push spend past the
    # raised $180 stop and confirm eval runs halt there rather than running on
    # to the $200 ceiling -- which is the protection that keeps a stray eval
    # from eating the headroom a live demo depends on.
    spend.record(run_id="r", case_id="c2", model="opus-4-6", effort="low",
                 usage=USAGE, cost=85.0, path=ledger)
    with pytest.raises(spend.BudgetExceeded, match="eval stop"):
        spend.check_before_call(model_name="opus-4-6", is_eval_run=True, path=ledger)


def test_a_run_that_spans_both_providers_is_not_labelled_with_one(ledger):
    """by_run is an index, and an index that lies is worse than no index.

    `by_run[run]["provider"]` was written once, when the bucket was created, and
    never revisited. The `queue` run then spanned both providers -- it served
    denials on the Anthropic API before the serving default moved to Bedrock --
    and every later Bedrock call was filed under `anthropic`. Reading provider
    totals off this index understated one budget by $0.47 and overstated the
    other by the same amount.

    The gate was never affected: it reads `ledger["providers"]`, which was
    correct throughout. This is about what the index tells anyone who reads it,
    the internal dashboard included, since it serves `by_run` verbatim.
    """
    spend.record(run_id="queue", case_id="a", model="opus-5", effort="low",
                 usage=USAGE, cost=0.50, path=ledger)
    led = spend.load(ledger)
    assert led["by_run"]["queue"]["provider"] == "anthropic"

    spend.record(run_id="queue", case_id="b", model="opus-4-6", effort="high",
                 usage=USAGE, cost=0.47, path=ledger)
    led = spend.load(ledger)
    run = led["by_run"]["queue"]

    assert run["provider"] == "mixed", (
        "a run served by two providers must not be labelled with either")
    assert run["providers"]["anthropic"]["usd"] == 0.50
    assert run["providers"]["bedrock"]["usd"] == 0.47
    assert run["usd"] == 0.97

    # And the index must agree with the block the gate actually reads.
    assert led["providers"]["anthropic"]["usd"] == 0.50
    assert led["providers"]["bedrock"]["usd"] == 0.47


def test_the_index_reconciles_with_the_authoritative_totals(ledger):
    """Whatever the runs are, the two views of the ledger must add up."""
    for i, (model, cost) in enumerate(
            [("opus-4-6", 1.0), ("opus-5", 2.0), ("opus-4-6", 3.0),
             ("sonnet-5", 4.0), ("sonnet-4-6", 5.0)]):
        spend.record(run_id=f"run-{i % 2}", case_id=f"c{i}", model=model,
                     effort="low", usage=USAGE, cost=cost, path=ledger)
    led = spend.load(ledger)
    from collections import defaultdict
    rolled = defaultdict(float)
    for run in led["by_run"].values():
        for name, p in run["providers"].items():
            rolled[name] += p["usd"]
    for name, total in led["providers"].items():
        assert round(rolled[name], 6) == round(total["usd"], 6), (
            f"by_run and providers disagree about {name}")

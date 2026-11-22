# make verify is the only definition of done.
#
# Offline loops run unconditionally. Loops that spend money are gated behind
# VERIFY_LIVE=1 so a clean-checkout verification cannot silently burn budget.
#
# The gate MUST keep the guard and the command in one shell -- one `if`, not a
# `test ... || exit 0` line followed by the command on the next line. Each make
# recipe line runs in its own shell, so `exit 0` there ends only the guard's
# own shell and the command underneath it still runs. That bug shipped once and
# spent real money during a run explicitly told not to; eval/test_makefile.py
# now fails if the broken shape comes back.

PY ?= .venv/bin/python
SLICE_DEV ?= eval/slices/dev15.txt

.PHONY: archive-raw clean help matrix merge-ledger preflight record-spend verify-annotations verify-headroom serve serve-internal venv verify verify-billing verify-budget verify-citations verify-credentials verify-default verify-frontend verify-surface verify-gate verify-human verify-inbox verify-ledger verify-leakage verify-leakage-static verify-loader verify-offline verify-parse verify-queue verify-schema verify-scorer verify-tokens

help:
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | sed 's/:.*## /\t/'

venv: ## create the virtualenv and install dependencies
	python3 -m venv .venv
	$(PY) -m pip install -q --upgrade pip
	$(PY) -m pip install -q -r requirements.txt

preflight: ## report which Bedrock models this account can actually invoke
	$(PY) tools/bedrock_preflight.py

record-spend: ## commit the live ledger as the record. Deliberate, never automatic.
	@cp results/spend.json results/spend_record.json
	@$(PY) -c "import json;d=json.load(open('results/spend_record.json'));\
	print('recorded', d['calls'], 'calls:', \
	' | '.join(f\"{k} \$${v['usd']:.4f}\" for k,v in sorted(d['providers'].items())))"

merge-ledger: ## reconcile this ledger with another deployment's. LEDGER=/path/to/spend.json
	@test -n "$(LEDGER)" || { echo "usage: make merge-ledger LEDGER=/path/to/spend.json"; exit 1; }
	$(PY) tools/merge_ledger.py results/spend_record.json "$(LEDGER)"

verify-scorer: ## fixture tests: known scores, negative control, failure taxonomy
	$(PY) -m pytest eval/test_score.py -q

verify-schema: ## schema is well-formed and rejects the malformed fixture
	$(PY) -c "import json,jsonschema; \
	jsonschema.Draft202012Validator.check_schema(json.load(open('schema/resolution.json'))); \
	print('schema/resolution.json valid (draft 2020-12)')"
	$(PY) -m pytest eval/test_score.py -q -k schema_invalid

verify-loader: ## uploaded cases render byte-identically to corpus cases
	$(PY) -m pytest eval/test_loader.py -q

verify-leakage-static: ## the label invariant, offline: nothing but the scorer reads labels
	$(PY) -m pytest eval/test_leakage.py -q

verify-gate: ## the VERIFY_LIVE gate actually gates
	$(PY) -m pytest eval/test_makefile.py -q

verify-billing: ## every billed call reaches the ledger, including failed ones
	$(PY) -m pytest eval/test_billing_paths.py -q

verify-inbox: ## a case that parks a second time is not lost
	$(PY) -m pytest eval/test_inbox_reparking.py -q

verify-citations: ## every cited source names a file that actually exists
	$(PY) -m pytest eval/test_citations.py -q

verify-default: ## the serving default names a model this deployment can actually run
	$(PY) -m pytest eval/test_serving_default.py -q -m 'not headroom'

verify-headroom: ## is there budget left to demo with. Run before a demo, not in CI.
	$(PY) -m pytest eval/test_serving_default.py -q -m headroom

verify-credentials: ## .env.local wins, the two providers' keys never mix, nothing leaks
	$(PY) -m pytest eval/test_credentials.py -q

verify-annotations: ## demo annotations trace to the model's own citations, never to the input
	$(PY) -m pytest eval/test_annotations.py eval/test_demo_view.py -q

verify-parse: ## case-header facts come off the artifact bytes, never typed in
	$(PY) -m pytest eval/test_caseinfo.py -q

verify-queue: ## the pool warms the cache solo then fans out; cancel stops the spend
	$(PY) -m pytest eval/test_queue_control.py -q

verify-surface: ## nothing internal reaches the client-facing app
	$(PY) -m pytest eval/test_client_surface.py -q

verify-ledger: ## the ledger survives two deployments on one account
	$(PY) -m pytest eval/test_ledger_sync.py -q

verify-budget: ## the two provider budgets never mix
	$(PY) -m pytest eval/test_budget_isolation.py -q

verify-offline: verify-schema verify-scorer verify-loader verify-leakage-static \
                verify-gate verify-billing verify-inbox verify-citations \
                verify-tokens verify-budget verify-default verify-surface verify-credentials verify-ledger verify-annotations verify-parse verify-queue ## every loop that costs nothing

# --- loops below here call the API; gated on VERIFY_LIVE=1 -------------------

verify-leakage: ## system must behave identically with dev_labels.jsonl deleted
	@if [ "$(VERIFY_LIVE)" = "1" ]; then \
	  $(PY) -m pytest eval/test_leakage.py -q; \
	else echo "skipped (set VERIFY_LIVE=1)"; fi

verify-human: ## awaiting-human round trip, and the inverse
	@if [ "$(VERIFY_LIVE)" = "1" ]; then \
	  $(PY) -m pytest eval/test_awaiting_human.py -q; \
	else echo "skipped (set VERIFY_LIVE=1)"; fi

verify-tokens: ## replay raw responses; totals must match harness and frontend
	# Offline: reads results/ and the HTTP layer, and calls no model. It was
	# gated behind VERIFY_LIVE=1, which hid 128 free tests from verify-offline.
	$(PY) -m pytest eval/test_token_accounting.py -q

verify-frontend: ## Playwright: operator journeys plus the internal data app
	@if [ "$(VERIFY_LIVE)" = "1" ]; then \
	  npx playwright test; \
	else echo "skipped (set VERIFY_LIVE=1)"; fi

serve: ## the operator app a client sees -- no spend, no evals, no accuracy
	set -a; . ./.env.local; set +a; \
	$(PY:%/python=%)/uvicorn mohenara.api:app --app-dir src --port 8765 --reload

serve-internal: ## the internal data app. Do NOT expose this publicly.
	set -a; . ./.env.local; set +a; \
	$(PY:%/python=%)/uvicorn mohenara.internal_api:app --app-dir src --port 8766 --reload

verify: verify-offline verify-leakage verify-human verify-frontend ## the definition of done
	@echo
	@if [ "$(VERIFY_LIVE)" = "1" ]; then \
	  echo "  verify: all suites green -- offline AND live."; \
	else \
	  echo "  verify: the OFFLINE suites are green."; \
	  echo "  The three live suites did NOT run: leakage, awaiting-human,"; \
	  echo "  frontend. This is NOT the definition of done."; \
	  echo "  Rerun with VERIFY_LIVE=1."; \
	  exit 1; \
	fi

matrix: ## run the 12-cell eval matrix and render results/matrix.md
	$(PY) eval/run_matrix.py --slice eval/slices/dev5.txt
	$(PY) eval/make_matrix_report.py

archive-raw: ## compress raw responses of scored runs
	$(PY) eval/archive_raw.py

clean:
	rm -rf results/_test .pytest_cache **/__pycache__

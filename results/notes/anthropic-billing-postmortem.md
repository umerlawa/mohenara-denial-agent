# Post-mortem: $8.96 of "anthropic" spend that never touched the API key

Written 2026-08-20, after Umer checked the Anthropic console and found the
project's API key had **zero recorded usage** for the entire build — while the
ledger showed $8.96 of anthropic-provider spend and every opus-5 call had
succeeded, including calls made while the configured key was **expired**.

## What actually happened

The resolver calls Claude by spawning the Claude Code CLI through the Agent
SDK. The CLI is a full product with its own credential resolution, and it had
three ways to authenticate that were not the configured `ANTHROPIC_API_KEY`:

1. **Host-managed session credentials.** The build ran inside a managed
   container that sets `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST=1` and delivers an
   OAuth token over a file descriptor
   (`CLAUDE_CODE_OAUTH_TOKEN_FILE_DESCRIPTOR`). A CLI spawned with those
   markers authenticates as the *container's session* — and prefers that over
   the env key.
2. **On-disk login state.** `~/.claude.json` carries `oauthAccount`: the
   login of whoever owns the machine. On this container that is the managed
   session; on a developer laptop it is their personal Claude account. The CLI
   reads it regardless of the environment.
3. **Inherited file descriptors**, independent of any variable naming them.

So every "anthropic" call — the $7.53 frontier comparison, the queue smoke
tests, the first demo run — was served and billed through the managed session's
own account. The key's console correctly showed zero. The tokens were real,
the accuracy results stand, the token counts are valid measurements. Only the
billing attribution was wrong.

## Why the guards missed it

- `_agent_env` checked the key was **present**. It was. Presence says nothing
  about use.
- An earlier hardening pass **popped** foreign credentials from the subprocess
  env dict, and its tests passed. But the Agent SDK builds the subprocess
  environment as `{**os.environ, **options.env}` — options.env is an overlay,
  so a popped key silently returns from the parent process. The tests read the
  intermediate dict, not the layer that reached the CLI.
- Blanking the variables to `""` (which does survive the merge) closed the env
  channel — and the CLI then authenticated from `~/.claude.json`. A denylist
  cannot enumerate channels it does not know exist, and each miss is silent:
  the call succeeds and someone else pays.

## Evidence

- The egress proxy does **not** inject auth: `GET /v1/models` with an invalid
  key returns 401 through the same proxy. (Rules out one hypothesis.)
- With host markers blanked AND a bogus `ANTHROPIC_API_KEY`, the resolve still
  succeeded — recorded live on 2026-08-20. That run proved the on-disk channel.
- With the full guard (below), the same bogus-key resolve fails; the bare CLI
  reports `api_error_status: 401, "API key is invalid"`, `total_cost_usd: 0`,
  after ~3 minutes of the CLI's internal auth retries.
- With the full guard and the real key: `is_error: false`, usage billed to the
  key — visible in the console, which is the one check code cannot do.

## The fix: default-deny on all three channels

`tools/cli_guard.py` is now the resolver's `cli_path`. It execs the real CLI
with:

- an environment rebuilt from the explicit allowlist in `config/models.json`
  (`subprocess_env_allowlist`) plus the selected provider's own
  `credential_env` and `env` flags — nothing else survives, whatever the SDK
  merged in;
- `HOME` pointed at a private empty directory (`.cli-home/`, gitignored), so
  `~/.claude.json` belongs to this project and contains no login;
- file descriptors above stderr closed.

Which account a model bills is now exactly what `config/models.json` says:
`provider` per model, `credential_env` per provider, `serving_provider` for the
apps. The same guard runs on every deployment, so a laptop's personal login is
excluded the same way the container's session was.

## The proof is behavioural and repeatable

`python tools/anthropic_auth_probe.py` (~3 minutes, ≤$0.001):

1. bogus key through the real pipeline → **must fail** (any success means a
   credential channel is open again);
2. real key against `GET /v1/models` → must be 200 (free);
3. one minimal billed call → **must appear in the Anthropic console**.

`eval/test_credentials.py` pins the guard offline: it reproduces the SDK's
merge and the guard's filter and asserts on the FINAL environment — the layer
that actually failed — including that no `host_managed_auth_env` marker
survives and that the CLI's HOME is never the real one.

## Ledger consequences

On Umer's instruction the anthropic bucket was reset to $0. The 69 phantom
entries ($8.9581) are archived with their token counts in
`results/abandoned/spend_anthropic_phantom.json`; bedrock ($45.86) was always
real and is untouched. Dollar figures for anthropic-side runs in
`results/frontier_comparison.md` and `RESULTS.md` remain correct as *computed
token value* but were never billed to the project's key.

One more consequence worth naming: the local demo clone's $0.407045 opus-5
call almost certainly billed the developer's own Claude login through channel
2, not the key. The guard closes that too; the probe verifies it on that
machine the same way it did here.

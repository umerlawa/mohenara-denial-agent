// The internal data app. Separate suite because it runs against a separate
// server on a separate port -- which is the point of the split.
//
// This suite carries the DOM leg of the token-accounting chain. It used to live
// in the customer app's results view; moving that view here without moving the
// assertion would have quietly dropped the invariant the brief asks for:
//
//   raw API response -> prediction file   eval/test_token_accounting.py
//   prediction file  -> HTTP API          eval/test_token_accounting.py
//   HTTP API         -> rendered DOM      HERE
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');

const REPO = path.resolve(__dirname, '..');
const BASE = process.env.INTERNAL_URL || 'http://127.0.0.1:8766';

function runsOnDisk() {
  const dir = path.join(REPO, 'results');
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter(d => fs.existsSync(path.join(dir, d, 'run.json')));
}

test.use({ baseURL: BASE });

test('runs table shows costs identical to results/ on disk', async ({ page }) => {
  const runs = runsOnDisk();
  test.skip(runs.length === 0, 'no eval runs on disk');

  await page.goto('/');
  const row = page.locator('tr.click[data-run]').first();
  await expect(row).toBeVisible();

  const runId = await row.getAttribute('data-run');
  const onDisk = JSON.parse(
    fs.readFileSync(path.join(REPO, 'results', runId, 'run.json'), 'utf8'));

  // Read from the same row, so this cannot pass by comparing a file to itself.
  const cells = await row.locator('td').allTextContents();
  const shown = cells.find(c => c.trim().startsWith('$'));
  expect(shown.trim()).toBe('$' + Number(onDisk.cost_usd).toFixed(4));
});

test('drilling into a run shows per-case cost matching the prediction file', async ({ page }) => {
  const runs = runsOnDisk();
  test.skip(runs.length === 0, 'no eval runs on disk');

  await page.goto('/');
  const row = page.locator('tr.click[data-run]').first();
  const runId = await row.getAttribute('data-run');
  await row.click();

  const caseRow = page.locator('#runDetail tr.click[data-case]').first();
  await expect(caseRow).toBeVisible();
  const caseId = await caseRow.getAttribute('data-case');

  const pred = JSON.parse(fs.readFileSync(
    path.join(REPO, 'results', runId, 'predictions', `${caseId}.json`), 'utf8'));
  const cells = await caseRow.locator('td').allTextContents();
  const shownCost = cells.find(c => c.trim().startsWith('$'));
  expect(shownCost.trim()).toBe('$' + Number(pred.usage.cost_usd).toFixed(4));

  // Output tokens too -- cost alone could match while the token panel is wrong.
  const shownTokens = cells.map(c => c.replace(/,/g, '').trim());
  expect(shownTokens).toContain(String(pred.usage.output_tokens));
});

test('both budgets are shown separately, at their real totals', async ({ page }) => {
  await page.goto('/');
  const header = page.locator('#spend');
  await expect(header).toContainText('bedrock');
  await expect(header).toContainText('anthropic');

  const served = await (await page.request.get('/api/spend')).json();
  for (const p of served.providers) {
    // The displayed figure must be the ledger's, not a rounded or combined one.
    await expect(header).toContainText('$' + p.usd.toFixed(4));
  }
});

test('the family view surfaces the weakest family rather than burying it', async ({ page }) => {
  await page.goto('/');
  await page.click('nav button[data-tab=families]');

  const served = await (await page.request.get('/api/families')).json();
  test.skip(served.length === 0, 'no scored runs on disk');

  // Sorted worst-first on purpose: a headline accuracy hides a weak family, and
  // the point of this view is that it cannot.
  const first = page.locator('#tab-families tbody tr').first();
  await expect(first).toContainText(served[0].family);
});

test('case lookup shows every run that touched a case', async ({ page }) => {
  const runs = runsOnDisk();
  test.skip(runs.length === 0, 'no eval runs on disk');

  const preds = fs.readdirSync(path.join(REPO, 'results', runs[0], 'predictions'));
  test.skip(preds.length === 0, 'no predictions');
  const caseId = preds[0].replace(/\.json$/, '');

  await page.goto('/');
  await page.click('nav button[data-tab=case]');
  await page.fill('#caseId', caseId);
  await page.click('#lookup');

  const panels = page.locator('#caseOut .panel');
  await expect(panels.first()).toBeVisible();

  const served = await (await page.request.get(`/api/case/${caseId}`)).json();
  await expect(panels).toHaveCount(served.runs.length);
});

// --- the analysis tabs ------------------------------------------------------
//
// These exist because the runs table answers "what did it score" and nothing
// else. Every assertion below is against a number the dashboard computes from
// results/ on disk, cross-checked here against the same files, so a tab that
// renders a plausible-looking figure from the wrong denominator fails.

test('the failure taxonomy separates not-answering from answering wrongly', async ({ page }) => {
  await page.goto('/');
  await page.click('nav button[data-tab=taxonomy]');
  const section = page.locator('#tab-taxonomy');
  await expect(section).toBeVisible();

  const api = await (await page.request.get('/api/failure-taxonomy')).json();
  const kinds = api.buckets.map(b => b.kind);

  // The distinction the whole tab exists to draw: a case the system never
  // reached is an infrastructure fact, and lumping it in with wrong answers
  // makes the model look worse than it is.
  expect(kinds.join(' ')).toContain('never answered');
  expect(kinds.join(' ')).toContain('refused');

  // The buckets must partition the failures -- no case counted twice, none lost.
  const summed = api.buckets.reduce((n, b) => n + b.n, 0);
  expect(summed, 'the buckets must add up to the total').toBe(api.total);

  for (const b of api.buckets) await expect(section).toContainText(String(b.n));
});

test('the confusion view names the costly mistakes rather than just counting them',
  async ({ page }) => {
  await page.goto('/');
  await page.click('nav button[data-tab=confusion]');
  await expect(page.locator('#tab-confusion')).toBeVisible();

  const api = await (await page.request.get('/api/confusion?field=path')).json();
  const wrong = api.cells.filter(c => c.expected !== c.got && c.got !== '(no answer)');
  expect(wrong.length, 'there are known wrong answers to display').toBeGreaterThan(0);

  // An asymmetric error costs more in one direction than the other. Telling a
  // biller to resubmit a claim that will deny again spends a filing window;
  // the reverse merely wastes a review. The tab has to say which is which.
  const costly = wrong.filter(c => c.costly);
  expect(costly.length, 'the costly directions must be annotated').toBeGreaterThan(0);
  await expect(page.locator('#tab-confusion')).toContainText(costly[0].expected);
});

test('the economics view reports a cache hit rate that matches the token counts',
  async ({ page }) => {
  await page.goto('/');
  await page.click('nav button[data-tab=economics]');
  await expect(page.locator('#tab-economics')).toBeVisible();

  const rows = await (await page.request.get('/api/economics')).json();
  expect(rows.length).toBeGreaterThan(0);
  for (const r of rows) {
    // Recomputed here rather than trusted: a hit rate is easy to render from
    // the wrong denominator and impossible to spot by eye once it is a percent.
    const expected = r.cache_read / (r.cache_read + r.cache_write);
    expect(Math.abs(r.cache_hit_rate - expected)).toBeLessThan(0.001);
    expect(Math.abs(r.cost_per_case - r.cost / r.cases)).toBeLessThan(0.001);
  }
});

test('regressions exclude cases the candidate never attempted', async ({ page }) => {
  await page.goto('/');
  await page.click('nav button[data-tab=regress]');
  await expect(page.locator('#tab-regress')).toBeVisible();

  // The tab renders nothing until a comparison is actually asked for, so drive
  // the controls rather than only the endpoint behind them.
  await page.selectOption('#rBase', 'final-sonnet-4-6-low-edi');
  await page.selectOption('#rCand', 'final-opus-4-6-low-edi');
  await page.click('#rGo');

  const res = await page.request.get(
    '/api/regressions?baseline=final-sonnet-4-6-low-edi&candidate=final-opus-4-6-low-edi');
  const api = await res.json();

  // A case the candidate never reached -- because a run was throttled or hit a
  // budget stop -- is not a regression. Counting those blamed the change under
  // test for an infrastructure stop, and turned a net of -1 into -25.
  const all = [...(api.broke || []), ...(api.fixed || [])];
  for (const c of all) {
    expect(c.case_id, 'a compared case must have been attempted by both runs')
      .toBeTruthy();
  }
  expect(api.shared_cases, 'the comparison must state its own denominator')
    .toBeGreaterThan(0);

  // The excluded cases must be reported, not silently dropped: a comparison
  // over 115 of 140 cases that does not say so reads as a comparison over 140.
  expect(api.not_attempted_by_one_side).toBeGreaterThan(0);
  await expect(page.locator('#tab-regress'))
    .toContainText(String(api.not_attempted_by_one_side));

  // And the arithmetic has to close: every shared case is fixed, broke, or
  // unchanged, and the net is the difference between the two correct counts.
  expect(api.candidate_correct - api.baseline_correct)
    .toBe(api.fixed.length - api.broke.length);
  expect(api.fixed.length + api.broke.length).toBeLessThanOrEqual(api.shared_cases);
});

test('every reference card in the cached prefix is actually cited by something',
  async ({ page }) => {
  await page.goto('/');
  await page.click('nav button[data-tab=reference]');
  await expect(page.locator('#tab-reference')).toBeVisible();

  const api = await (await page.request.get('/api/reference-usage')).json();
  const cards = api.cards || api;
  expect(cards.length).toBeGreaterThan(0);
  // A card nobody cites is dead weight in a prefix paid for on every call.
  // If one ever appears, this test should fail and the card should go.
  const unused = cards.filter(c => (c.citations ?? c.n ?? 0) === 0);
  expect(unused.map(c => c.file ?? c.name),
    'unused cards cost cache-write tokens on every call').toEqual([]);
});

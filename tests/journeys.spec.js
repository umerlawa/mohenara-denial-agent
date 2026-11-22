// One test per operator journey against the client-facing app.
//
// This app is deliberately incurious about the model: there is no model or
// effort control, no cost, no token counts, no eval data. Several of these tests
// assert the ABSENCE of those things, so putting them back fails the suite
// rather than quietly reaching a client demo.
//
// No test here is allowed to skip on a condition the suite itself creates. An
// earlier revision skipped journey 3 when nothing in the queue was awaiting
// input -- which is to say it skipped exactly when the awaiting-human path was
// broken. Each journey now seeds the state it needs and fails if it cannot.
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');

const REPO = path.resolve(__dirname, '..');

// Two cases picked from recorded runs, not at random:
//   RESOLVES parks under no configuration tested (opus-4-6 and sonnet-4-6, both
//   formats), so journey 1 asserting a resolution is a real assertion.
//   PARKS is an NCCI PTP case whose CCMI is in neither the 835 nor the chart
//   note. Every model tested, Opus 5 included, refuses to guess it and asks --
//   which is the behaviour journey 3 exists to prove.
const RESOLVES = 'MOH2-000009';
const PARKS = 'MOH2-000233';
const EDI_DIR = path.join(REPO, 'corpus', 'v2-chain-corpus-v1.1', 'edi', RESOLVES);

function ediFiles() {
  if (!fs.existsSync(EDI_DIR)) return [];
  return fs.readdirSync(EDI_DIR).filter(f => /\.(edi|txt)$/.test(f))
    .map(f => path.join(EDI_DIR, f));
}

const card = (page, label) =>
  page.locator('[data-testid=job]').filter({ hasText: label }).first();

// A resolve on Opus 5 at high effort takes a while and the queue is serialised,
// so wait on the card's own state rather than on any one request.
async function waitForState(locator, states, timeout = 300_000) {
  await expect(locator).toContainText(new RegExp(states.join('|'), 'i'), { timeout });
}

test('journey 1: submit an EDI artifact set and watch it resolve', async ({ page }) => {
  const files = ediFiles();
  expect(files.length, `no EDI artifacts for ${RESOLVES} in this checkout`).toBeGreaterThan(0);

  await page.goto('/');
  // Start from an empty worklist so later journeys address cards by name
  // rather than by position in whatever the last run left behind.
  await page.request.post('/api/queue/clear');
  await page.reload();
  await expect(page.locator('[data-testid=empty]')).toBeVisible();

  await page.setInputFiles('#files', files);
  // One artifact directory is one denial, not one denial per file.
  await expect(page.locator('#batchHint')).toContainText('1 denial');
  await page.click('[data-testid=submit]');

  const job = page.locator('[data-testid=job]').first();
  await expect(job).toBeVisible();
  await waitForState(job, ['Resolved']);

  await job.click();
  await expect(page.locator('[data-testid=detail]')).toBeVisible();
});

test('journey 2: a resolved denial shows the claim header and a next action', async ({ page }) => {
  await page.goto('/');
  const resolved = page.locator('[data-testid=job]').filter({ hasText: 'Resolved' }).first();
  await expect(resolved, 'journey 1 should have left a resolved denial').toBeVisible();

  await resolved.click();
  const detail = page.locator('[data-testid=detail]');
  await expect(detail.locator('[data-testid=root-cause]')).not.toBeEmpty();
  await expect(detail.locator('[data-testid=next-action]')).not.toBeEmpty();
  // Copy-to-clipboard exists because whatever this produces gets pasted into
  // whichever practice-management system the operator actually lives in.
  await expect(detail.locator('[data-testid=copy]')).toBeVisible();
});

test('journey 3: a denial needing input is answerable with text and documents', async ({ page }) => {
  await page.goto('/');

  // Seed the state under test rather than hoping for it.
  await page.fill('#caseId', PARKS);
  await page.click('#byId');

  const job = card(page, PARKS);
  await expect(job).toBeVisible();
  await waitForState(job, ['Needs your input']);
  await job.click();

  const detail = page.locator('[data-testid=detail]');
  await expect(detail.locator('[data-testid=answer-input]')).toBeVisible();
  // A document, because the answer to these questions is usually a document
  // rather than a sentence.
  await expect(detail.locator('[data-testid=answer-files]')).toBeVisible();

  await detail.locator('[data-testid=answer-input]').fill(
    'CMS NCCI PTP edit file for Q2 2026: the pair carries CCMI 1, so a bypass '
    + 'modifier is permitted when the documentation supports it.');
  await detail.locator('[data-testid=answer-files]').setInputFiles({
    name: 'ncci-lookup.md', mimeType: 'text/markdown',
    buffer: Buffer.from('# NCCI PTP lookup\n\nColumn One 97150 / Column Two 97110, '
      + 'effective Q2 2026: Correct Coding Modifier Indicator = 1.\n'),
  });
  await detail.locator('[data-testid=submit-answer]').click();

  // The answer must actually move the denial off the parked state.
  await waitForState(card(page, PARKS), ['Resolved', 'Resolving']);
  await waitForState(card(page, PARKS), ['Resolved']);
});

test('journey 4: the client-facing app exposes no internal surface', async ({ page }) => {
  await page.goto('/');

  // Checked at the route level, not just by absent controls -- a view that is
  // merely not rendered is still one URL away.
  for (const route of ['/api/spend', '/api/runs', '/api/models', '/api/runs/x',
                       '/api/families', '/api/economics']) {
    const res = await page.request.get(route);
    expect(res.status(), `${route} must not be served by the operator app`).toBe(404);
  }

  // And nothing in the page may name a model, an effort level, or a token cost.
  const body = (await page.locator('body').textContent()).toLowerCase();
  for (const banned of ['opus', 'sonnet', 'claude', 'effort', 'token']) {
    expect(body, `the operator UI must not mention "${banned}"`).not.toContain(banned);
  }
  await expect(page.locator('#model, [data-testid=model-select]')).toHaveCount(0);

  // Nor may the payload behind it. The queue carries the full case text and the
  // usage record on the server; neither belongs on the wire to a client demo.
  const queue = await (await page.request.get('/api/queue')).text();
  for (const leak of ['cost_usd', 'cache_read', 'opus', 'sonnet', '_source']) {
    expect(queue.toLowerCase(), `/api/queue must not carry "${leak}"`)
      .not.toContain(leak.toLowerCase());
  }
});

test('journey 5: intake is file-first with optional notes, and the queue is empty-stated',
  async ({ page }) => {
  await page.goto('/');
  // The primary control is a drop target for documents, not a text box.
  await expect(page.locator('[data-testid=drop]')).toBeVisible();
  await expect(page.locator('[data-testid=notes]')).toBeVisible();

  // Format is the operator's choice and both are offered.
  await expect(page.locator('#fmt button[data-fmt=edi]')).toBeVisible();
  await expect(page.locator('#fmt button[data-fmt=md]')).toBeVisible();

  // Submitting nothing is refused in the page, not by a server round trip.
  await page.click('[data-testid=submit]');
  await expect(page.locator('#batchHint')).toContainText('at least one document');
});

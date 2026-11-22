// The practice-audience demo at /demo?v=practice. A template with zero data:
// every number, name, and sentence on the page is computed at runtime from the
// uploaded cases and their real resolution outputs.
//
// The load-bearing assertions: BEFORE upload the page shows no numbers at all;
// every figure afterwards equals what this test computes independently from
// the same 835 bytes; and the served bundle contains none of those values as
// literals -- a hardcoded amount would keep showing when it is wrong.
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');

const REPO = path.resolve(__dirname, '..');
const CORPUS = path.join(REPO, 'corpus', 'v2-chain-corpus-v1.1', 'edi');
const PAGE = '/demo?v=practice';

const fmt = n => '$' + Number(n).toLocaleString('en-US',
  { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const titleCase = s => s.toLowerCase().split(/\s+/)
  .map(w => w ? w[0].toUpperCase() + w.slice(1) : w).join(' ');

// The test's OWN 835 reading -- the independent side of every money assertion.
function parse835(text) {
  const out = { billed: 0, paid: 0, denied: 0, patient: null, payer: null };
  for (const seg of text.split('~').map(s => s.trim()).filter(Boolean)) {
    const e = seg.split('*');
    if (e[0] === 'CLP' && e.length > 4) {
      out.billed += parseFloat(e[3]) || 0;
      out.paid += parseFloat(e[4]) || 0;
    } else if (e[0] === 'NM1' && e[1] === 'QC' && !out.patient) {
      out.patient = titleCase(`${e[4]} ${e[3]}`.trim());
    } else if (e[0] === 'N1' && e[1] === 'PR' && !out.payer) {
      out.payer = titleCase(e[2]);
    }
  }
  out.denied = Math.round((out.billed - out.paid) * 100) / 100;
  return out;
}

function caseFiles(caseId) {
  const dir = path.join(CORPUS, caseId);
  const files = {};
  for (const f of fs.readdirSync(dir)) files[f] = fs.readFileSync(path.join(dir, f), 'utf8');
  return files;
}

// One case dropped onto the page as loose files (a synthetic DataTransfer has
// no directory entries, so this exercises the loose-file grouping; the folder
// walk shares the same filter and intake).
async function dropCase(page, files) {
  await page.evaluate(fileList => {
    const dt = new DataTransfer();
    for (const [name, body] of fileList)
      dt.items.add(new File([body], name, { type: 'text/plain' }));
    document.querySelector('[data-region=dropzone]').dispatchEvent(
      new DragEvent('drop', { dataTransfer: dt, bubbles: true }));
  }, Object.entries(files));
}

const cardCount = page => page.locator('.card:not(template .card)').count();

// ---------------------------------------------------------------------------
// Free: the empty page and the bundle.
// ---------------------------------------------------------------------------
test('practice: before upload the page shows no numbers and holds no case data',
  async ({ page }) => {
  await page.goto(PAGE);
  const visible = await page.locator('body').innerText();
  expect(visible, 'no digits may render before any case exists').not.toMatch(/\d/);
  await expect(page.locator('[data-region=dropzone]')).toBeVisible();
  await expect(page.locator('[data-region=stats]')).toBeHidden();
  await expect(page.locator('.logo img')).toBeVisible();
  expect((await page.request.get('/assets/logo.svg')).status()).toBe(200);

  // The served bundle carries no case literal: amounts, names, payers of the
  // corpus cases this demo will be filmed with.
  const bundle = (await (await page.request.get(PAGE)).text()).toLowerCase();
  for (const cid of ['MOH2-000029', 'MOH2-000011', 'MOH2-000061', 'MOH2-000009', 'MOH2-000117']) {
    const got = parse835(caseFiles(cid)['remit_835.edi']);
    for (const banned of [String(got.denied), got.patient, got.payer]) {
      expect(bundle, `bundle must not contain ${JSON.stringify(banned)}`)
        .not.toContain(String(banned).toLowerCase());
    }
  }
});

test('practice: a dropped case parses into a card and money stats, nothing resolved',
  async ({ page }) => {
  await page.goto(PAGE);
  const files = caseFiles('MOH2-000029');
  const want = parse835(files['remit_835.edi']);
  await dropCase(page, files);

  await expect.poll(() => cardCount(page)).toBe(1);
  const card = page.locator('.card').first();
  await expect(card.locator('[data-bind=denied-amount]')).toHaveText(fmt(want.denied));
  await expect(card.locator('[data-bind=patient-name]')).toHaveText(want.patient);
  await expect(card.locator('[data-bind=payer-dos-service]')).toContainText(want.payer);
  await expect(page.locator('[data-bind=total-denied]')).toHaveText(fmt(want.denied));
  // The dropzone stays open for more cases until the run starts, and lists
  // what has landed so the person dropping folders can see them arrive.
  await expect(page.locator('[data-region=dropzone]')).toBeVisible();
  await expect(page.locator('[data-bind=drop-list]')).toContainText('6 files');
  await expect(page.locator('[data-bind=dropzone-instruction]'))
    .toContainText('Resolve all');
  // Nothing has resolved: no outcome, no why, no flag, chip not final.
  await expect(card.locator('.outcome')).toBeHidden();
  await expect(card.locator('.why')).toBeHidden();
  await expect(card.locator('[data-bind=deadline-flag]')).toBeHidden();
});

// ---------------------------------------------------------------------------
// Free: the full run flow against a scripted backend. Chips advance on the
// polled states, a parked case moves to the inbox and back, buckets and
// breakdowns land -- all without a single resolve.
// ---------------------------------------------------------------------------
function synth835(claim, patientLast, patientFirst, payer, billed) {
  return `N1*PR*${payer}~CLP*${claim}*4*${billed.toFixed(2)}*0**CI*R*11*1~` +
    `NM1*QC*1*${patientLast}*${patientFirst}****MI*Z~DTM*232*20260118~SVC*HC:1*1*0**1~`;
}

const canned = (over) => Object.assign({
  job: { state: 'resolved', filing_deadline: null },
  rationale: 'Denied CO-4 / N822 — the required modifier is absent per the 835, '
    + 'and CLP07 carries a payer control number.',
  root_cause: { family: 'missing_therapy_modifier', explanation: 'x' },
  next_action: { path: 'correct_and_resubmit', detail: 'x' },
  annotations: { anchored: [{ artifact: 'remit_835.edi' }], unanchored: [] },
  question: null, why_needed: null, answers: [],
}, over);

test('practice: the scripted run advances chips, parks, resumes, and lands buckets',
  async ({ page }) => {
  const CASES = [
    ['S1', 'ONE', 'ANNA', 'ALPHA HEALTH PLAN', 100],
    ['S2', 'TWO', 'BEN', 'BETA MUTUAL', 50],
    ['S3', 'THREE', 'CARA', 'ALPHA HEALTH PLAN', 25],
  ];
  const views = {
    j0: canned({}),
    j1: canned({ next_action: { path: 'bill_patient', detail: 'x' },
                 root_cause: { family: 'eligibility_terminated', explanation: 'x' },
                 answers: [{ question: 'q', answer: 'a', at: '', documents: [] }] }),
    j2: canned({ next_action: { path: 'do_not_resubmit', detail: 'x' },
                 root_cause: { family: 'exact_duplicate', explanation: 'x' } }),
  };
  const parkedView = canned({
    job: { state: 'needs_input' }, next_action: null, root_cause: null,
    question: 'Has the primary plan already processed this claim?',
  });
  let phase = 0;         // advances on each poll of /api/queue
  let answered = false;
  const stateFor = (i) => {
    // j0 runs first; j1 parks until answered; j2 follows. Never timers -- the
    // page only moves when a poll reports a new state.
    if (i === 0) return phase < 2 ? 'queued' : phase < 4 ? 'resolving' : 'resolved';
    if (i === 1) return phase < 4 ? 'queued' : phase < 6 ? 'resolving'
      : !answered ? 'needs_input' : phase < 10 ? 'resolving' : 'resolved';
    return phase < 6 ? 'queued' : phase < 8 ? 'resolving' : 'resolved';
  };
  await page.route('**/api/batch', route => route.fulfill({
    status: 200, contentType: 'application/json',
    body: JSON.stringify([{ id: 'j0' }, { id: 'j1' }, { id: 'j2' }]) }));
  await page.route('**/api/queue', route => {
    phase++;
    route.fulfill({ status: 200, contentType: 'application/json',
      body: JSON.stringify(CASES.map((_, i) => ({ id: `j${i}`, state: stateFor(i) }))) });
  });
  await page.route('**/api/demo/view/*', route => {
    const id = route.request().url().split('/').pop();
    const v = id === 'j1' && !answered ? parkedView : views[id];
    route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(v) });
  });
  await page.route('**/api/queue/*/answer', route => {
    answered = true;
    if (phase < 8) phase = 8;
    route.fulfill({ status: 200, contentType: 'application/json', body: '{}' });
  });

  await page.goto(PAGE);
  for (const [claim, last, first, payer, billed] of CASES)
    await dropCase(page, { 'remit_835.edi': synth835(claim, last, first, payer, billed) });
  await expect.poll(() => cardCount(page)).toBe(3);
  await expect(page.locator('[data-bind=total-denied]')).toHaveText(fmt(175));
  // Three separate drops accumulated -- nothing ran, the zone listed each.
  await expect(page.locator('[data-bind=drop-list] > div')).toHaveCount(3);
  await expect(page.locator('[data-region=dropzone]')).toBeVisible();

  await page.click('[data-action=resolve-all]');
  // Only the click starts the run; the intake closes with it.
  await expect(page.locator('[data-region=dropzone]')).toBeHidden();

  // Intermediate stages, straight off the scripted states.
  const chip0 = page.locator('[data-key=c0] .chip');
  await expect(chip0).toHaveText(/Working the denial/, { timeout: 15_000 });
  await expect(chip0).toHaveText(/Done/, { timeout: 15_000 });

  // The parked case moved to the inbox with the backend's actual question.
  const parked = page.locator('[data-region=inbox] .card');
  await expect(parked).toHaveCount(1, { timeout: 15_000 });
  await expect(parked.locator('[data-bind=human-question]'))
    .toHaveText('Has the primary plan already processed this claim?');
  await expect(page.locator('[data-bind=waiting-on-answer]')).toHaveText(fmt(50));

  // Answer inline; the card moves back and the run completes.
  await parked.locator('[data-bind=answer-input]').fill('Yes — their EOB shows it paid primary.');
  await parked.locator('[data-action=send-answer]').click();
  await expect(page.locator('[data-region=inbox] .card')).toHaveCount(0, { timeout: 15_000 });

  await expect(page.locator('[data-region=summary]')).toBeVisible({ timeout: 20_000 });
  // Buckets: recover=100 (resubmit), patient=50, no action=25, waiting=0.
  await expect(page.locator('[data-bind=recoverable]')).toHaveText(fmt(100));
  await expect(page.locator('[data-bind=patient-responsibility]')).toHaveText(fmt(50));
  await expect(page.locator('[data-bind=no-action]')).toHaveText(fmt(25));
  await expect(page.locator('[data-bind=waiting-on-answer]')).toHaveText(fmt(0));
  await expect(page.locator('[data-bind=summary-headline]')).toContainText(fmt(100));

  // Why-section: rationale rendered without billing-code tokens, sources named.
  const why0 = page.locator('[data-key=c0] [data-bind=why-text]');
  await expect(why0).not.toHaveText('');
  await expect(why0).not.toContainText('CO-4');
  await expect(why0).not.toContainText('N822');
  await expect(why0).not.toContainText('835');
  await expect(why0).not.toContainText('CLP07');
  await expect(why0).toContainText('per the payer remittance');
  await expect(why0).toContainText('required modifier is absent');
  await expect(page.locator('[data-key=c0] [data-bind=why-sources]'))
    .toContainText('payer remittance');
  // The answered case cites the human answer among its sources.
  await expect(page.locator('[data-key=c1] [data-bind=why-sources]'))
    .toContainText('your answer');

  // Breakdowns by payer and reason, from the batch.
  await expect(page.locator('[data-region=by-payer] .row')).toHaveCount(2);
  await expect(page.locator('[data-region=by-payer]')).toContainText('Alpha Health Plan');
  await expect(page.locator('[data-region=by-reason] .row')).toHaveCount(3);
});

test('practice: stop halts the batch, history and the card open the detail dialog',
  async ({ page }) => {
  // Scripted backend again: j0 finishes with a corrected claim, j1 keeps
  // running until Stop is clicked, then reports cancelled. Free.
  const corrected = {
    artifact: 'claim_837p.edi',
    text: 'CLM*A*1~\nSV1*HC:97110:GP*1*UN*1***1~',
    changed: [{ line: 2, before: 'SV1*HC:97110*1*UN*1***1~',
                after: 'SV1*HC:97110:GP*1*UN*1***1~', why: 'append GP' }],
    dropped: [], note: null,
  };
  const views = {
    j0: canned({ corrected,
                 next_action: { path: 'correct_and_resubmit', detail: 'x',
                                resubmission_frequency_code: '7' } }),
    j1: canned({ job: { state: 'cancelled' }, rationale: null,
                 next_action: null, root_cause: null }),
  };
  let stopped = false;
  const cancelCalls = [];
  await page.route('**/api/batch', route => route.fulfill({
    status: 200, contentType: 'application/json',
    body: JSON.stringify([{ id: 'j0' }, { id: 'j1' }]) }));
  await page.route('**/api/queue/cancel-all', route => {
    stopped = true; cancelCalls.push(1);
    route.fulfill({ status: 200, contentType: 'application/json',
                    body: JSON.stringify({ cancelled: 1 }) });
  });
  await page.route('**/api/queue', route => route.fulfill({
    status: 200, contentType: 'application/json',
    body: JSON.stringify([
      { id: 'j0', state: 'resolved', label: 'A', case_id: 'CASE-A',
        billed_amount: 100, updated_at: '2' },
      { id: 'j1', state: stopped ? 'cancelled' : 'resolving', label: 'B',
        case_id: 'CASE-B', billed_amount: 50, updated_at: '1' },
    ]) }));
  await page.route('**/api/demo/view/*', route => route.fulfill({
    status: 200, contentType: 'application/json',
    body: JSON.stringify(views[route.request().url().split('/').pop()]) }));

  await page.goto(PAGE);
  await dropCase(page, { 'remit_835.edi': synth835('A1', 'ONE', 'ANNA', 'ALPHA PLAN', 100) });
  await dropCase(page, { 'remit_835.edi': synth835('B1', 'TWO', 'BEN', 'ALPHA PLAN', 50) });
  await expect.poll(() => cardCount(page)).toBe(2);
  await page.click('[data-action=resolve-all]');

  // The panic button is there while anything is moving, and stops it.
  const stopBtn = page.locator('[data-action=stop-all]');
  await expect(stopBtn).toBeVisible({ timeout: 10_000 });
  await stopBtn.click();
  await expect.poll(() => cancelCalls.length).toBe(1);
  await expect(page.locator('[data-key=c1] .chip')).toHaveText('Stopped', { timeout: 10_000 });
  await expect(page.locator('[data-region=summary]')).toBeVisible({ timeout: 15_000 });
  await expect(stopBtn).toBeHidden();
  await expect(page.locator('[data-action=new-batch]')).toBeVisible();

  // Clicking the finished card opens the resubmission detail.
  await page.click('[data-key=c0] .who');
  const dlg = page.locator('[data-region=detail]');
  await expect(dlg).toBeVisible();
  await expect(dlg).toContainText('Corrected claim — ready to resubmit');
  await expect(dlg).toContainText('replacement claim (frequency code 7)');
  await expect(dlg).toContainText('SV1*HC:97110:GP');
  await expect(dlg.locator('[data-action=detail-copy]')).toBeVisible();
  await expect(dlg.locator('[data-action=detail-download]')).toBeVisible();
  await expect(dlg.locator('[data-action=detail-download-claim]')).toBeVisible();
  // Close on the X...
  await page.click('[data-action=detail-close]');
  await expect(dlg).toBeHidden();

  // ...and reopen from history, then close by clicking outside.
  await page.click('[data-action=history]');
  const rows = page.locator('[data-region=history-list] .histRow');
  await expect(rows).toHaveCount(2);
  await rows.first().click();
  await expect(dlg).toBeVisible();
  await page.mouse.click(8, 8);
  await expect(dlg).toBeHidden();

  // And the third close path: Escape (native dialog cancel).
  await page.click('[data-key=c0] .who');
  await expect(dlg).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(dlg).toBeHidden();

  // New batch returns the page to its empty intake.
  await page.click('[data-action=new-batch]');
  await expect(page.locator('[data-region=dropzone]')).toBeVisible();
  await expect(page.locator('[data-region=stats]')).toBeHidden();
  expect(await page.locator('body').innerText()).not.toMatch(/\d/);
});

// ---------------------------------------------------------------------------
// Live: five real denials through the dropzone and the real backend.
// Spends on the serving provider (~5-6 resolves).
// ---------------------------------------------------------------------------
test('demo live: the practice view runs five real denials end to end', async ({ page }) => {
  test.setTimeout(1_500_000);
  const IDS = ['MOH2-000029', 'MOH2-000011', 'MOH2-000061', 'MOH2-000009', 'MOH2-000117'];
  const expected = {};
  for (const cid of IDS) expected[cid] = parse835(caseFiles(cid)['remit_835.edi']);
  const totalDenied = IDS.reduce((s, c) => s + expected[c].denied, 0);

  await page.goto(PAGE);
  expect(await page.locator('body').innerText(),
    'no digits before upload').not.toMatch(/\d/);

  for (const cid of IDS) {
    const before = await cardCount(page);
    await dropCase(page, caseFiles(cid));
    await expect.poll(() => cardCount(page)).toBe(before + 1);
  }
  await expect(page.locator('[data-bind=total-denied]')).toHaveText(fmt(totalDenied));
  await page.screenshot({ path: 'results/playwright-artifacts/practice-live-1-loaded.png',
                          fullPage: true });
  // Cards map to cases by patient name; remember which card is which.
  const keyOf = {};
  for (const cid of IDS) {
    const card = page.locator('.card', {
      has: page.locator('[data-bind=patient-name]', { hasText: expected[cid].patient }) });
    await expect(card).toHaveCount(1);
    keyOf[cid] = await card.getAttribute('data-key');
  }

  await page.click('[data-action=resolve-all]');

  // Sample every chip until the batch lands; the history is the proof that
  // every card showed an intermediate stage before its final one.
  const history = Object.fromEntries(IDS.map(c => [c, []]));
  const answeredJobs = new Set();
  let midshot = false;
  const deadline = Date.now() + 1_380_000;
  let done = false;
  while (!done && Date.now() < deadline) {
    for (const cid of IDS) {
      const txt = (await page.locator(`[data-key=${keyOf[cid]}] .chip`).innerText()).trim();
      const h = history[cid];
      if (txt && h[h.length - 1] !== txt) h.push(txt);
    }
    // A case that stops to ask gets its answer through the inline inbox form.
    for (const parked of await page.locator('[data-region=inbox] .card').all()) {
      const job = await parked.getAttribute('data-job');
      if (!job || answeredJobs.has(job)) continue;
      answeredJobs.add(job);
      await parked.locator('[data-bind=answer-input]').fill(
        'Checked our records and the payer portal: no prior corrected claim or '
        + 'appeal has been filed for this claim, and no additional documentation '
        + 'exists beyond what was submitted.');
      await parked.locator('[data-action=send-answer]').click();
    }
    done = await page.locator('[data-region=summary]').isVisible();
    if (!done) await page.waitForTimeout(400);
    if (!midshot && Object.values(history).some(h => h.length > 1)) {
      midshot = true;
      await page.screenshot({ path: 'results/playwright-artifacts/practice-live-2-midrun.png',
                              fullPage: true });
    }
  }
  expect(done, 'the batch must complete inside the test window').toBe(true);
  for (const d of await page.locator('.card.done details.why').all()) {
    await d.evaluate(el => el.open = true);
  }
  await page.screenshot({ path: 'results/playwright-artifacts/practice-live-3-final.png',
                          fullPage: true });

  const FINALS = ['Done', 'Could not finish'];
  for (const cid of IDS) {
    const h = history[cid];
    expect(h[h.length - 1], `${cid} must end final (saw: ${h.join(' > ')})`).toBe('Done');
    expect(h.length, `${cid} must show an intermediate stage first (saw: ${h.join(' > ')})`)
      .toBeGreaterThan(1);
    expect(h.slice(0, -1).some(s => !FINALS.includes(s)),
      `${cid} intermediate stages must be non-final (saw: ${h.join(' > ')})`).toBe(true);
  }

  // Ground truth per case: the resolution's own path, read off the backend.
  const buckets = { recover: 0, patient: 0, noaction: 0 };
  const BUCKET_OF = { correct_and_resubmit: 'recover', appeal: 'recover',
    resubmit_other_payer: 'recover', bill_patient: 'patient',
    do_not_resubmit: 'noaction', none: 'noaction' };
  for (const cid of IDS) {
    const card = page.locator(`[data-key=${keyOf[cid]}]`);
    const job = await card.getAttribute('data-job');
    const view = await (await page.request.get(`/api/demo/view/${job}`)).json();
    const path_ = view.next_action?.path;
    expect(BUCKET_OF[path_], `${cid} resolved with a bucketable path (${path_})`).toBeTruthy();
    buckets[BUCKET_OF[path_]] += expected[cid].denied;

    // Outcome line rendered and consistent with the path's bucket.
    const outcome = card.locator('[data-bind=outcome-line]');
    await expect(outcome).toBeVisible();
    const cls = { recover: /green/, patient: /amber/, noaction: /gray/ }[BUCKET_OF[path_]];
    await expect(outcome).toHaveClass(cls);

    // Why-section: non-empty reasoning citing at least one source document.
    await expect(card.locator('[data-bind=why-text]')).not.toHaveText('');
    await expect(card.locator('[data-bind=why-sources]')).toContainText('Based on');
  }
  const round2 = n => Math.round(n * 100) / 100;
  await expect(page.locator('[data-bind=recoverable]')).toHaveText(fmt(round2(buckets.recover)));
  await expect(page.locator('[data-bind=patient-responsibility]'))
    .toHaveText(fmt(round2(buckets.patient)));
  await expect(page.locator('[data-bind=no-action]')).toHaveText(fmt(round2(buckets.noaction)));
  await expect(page.locator('[data-bind=waiting-on-answer]')).toHaveText(fmt(0));
  await expect(page.locator('[data-bind=total-denied]')).toHaveText(fmt(round2(totalDenied)));
  await expect(page.locator('[data-bind=handled-count]')).toHaveText('5 of 5 claims handled');

  // And the served bundle still holds none of what it just displayed.
  const bundle = (await (await page.request.get(PAGE)).text()).toLowerCase();
  for (const cid of IDS) {
    expect(bundle).not.toContain(String(expected[cid].denied));
    expect(bundle).not.toContain(expected[cid].patient.toLowerCase());
  }
});

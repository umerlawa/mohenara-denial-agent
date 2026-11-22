// The outreach demo at /demo. A separate frontend on the same backend.
//
// The load-bearing assertion in here is the BEFORE state. Any screen can draw
// red boxes on a claim after the fact; what makes this one honest is that the
// input renders with zero annotations until the model has actually said
// something, and that every annotation afterwards traces to a segment the model
// quoted and that was then matched against the artifact bytes. A frontend that
// found the defective lines itself would pass an after-only test and would keep
// highlighting confidently on a case the model got wrong.
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');

const REPO = path.resolve(__dirname, '..');
const QUEUE = path.join(REPO, 'results', 'queue');
const CASE = 'MOH2-000029';

// The three therapy CPTs billed without the GP modifier. Read off the corpus
// artifact, not typed from memory.
const GP_CODES = ['97110', '97112', '97140'];

// results/queue is shared live state: the operator app reads the same directory.
// A seeded job left behind with a non-terminal state is invisible to
// `/api/queue/clear` -- which only drops FINISHED jobs -- so it sits in the
// operator's worklist for ever and breaks that suite's empty-state assertion.
// It did exactly that once. Anything seeded here is removed again.
test.afterAll(() => {
  if (!fs.existsSync(QUEUE)) return;
  for (const f of fs.readdirSync(QUEUE)) {
    if (f.startsWith('demoseed-')) fs.unlinkSync(path.join(QUEUE, f));
  }
});


// ---------------------------------------------------------------------------
// Free: renders a recorded run. Catches every markup and anchoring regression
// without paying for a resolve, so the live test below only ever has to fail
// for real reasons.
// ---------------------------------------------------------------------------
const GP_LINES = [
  'SV1*HC:97110*77.92*UN*2***1~',
  'SV1*HC:97112*44.76*UN*1***1~',
  'SV1*HC:97140*47.07*UN*1***1~',
];
const CLM_BEFORE = 'CLM*PA25896500*169.75***11:B:1*Y*A*Y*Y~';
const CLM_AFTER = 'CLM*PA25896500*169.75***11:B:7*Y*A*Y*Y~';

function seed(id, state) {
  const resolution = {
    schema_version: '1.0', case_id: CASE, status: 'resolved',
    rationale: 'All three lines denied CO-4 + N822: no GP modifier.',
    usage: { cost_usd: 0.3, model: 'claude-opus-5', effort: 'high' },
    resolution: {
      root_cause: { family: 'missing_therapy_modifier',
                    explanation: 'Therapy CPTs billed without the GP modifier.' },
      next_action: { path: 'correct_and_resubmit',
                     detail: 'Append GP to all three service lines.',
                     resubmission_frequency_code: '7' },
      evidence: GP_LINES.map(q => ({
        artifact: 'claim_837p.edi', fact: `${q} carries no GP modifier.`,
        chip: 'Missing GP modifier', severity: 'error',
        segments: [{ text: q, id: 'SV1' }],
      })),
      corrected_claim: {
        artifact: 'claim_837p.edi',
        edits: GP_LINES.map(q => ({
          before: q, after: q.replace(/(\*\d+\.\d+\*UN)/, ':GP$1'),
          why: 'append GP',
        })).concat([{ before: CLM_BEFORE, after: CLM_AFTER,
                     why: 'frequency code 7 — replacement claim' }]),
      },
    },
  };
  fs.mkdirSync(QUEUE, { recursive: true });
  fs.writeFileSync(path.join(QUEUE, `${id}.json`), JSON.stringify({
    id, label: CASE, state, input_format: 'edi', case_id: CASE, notes: null,
    created_at: '2026-08-20T00:00:00+00:00',
    updated_at: '2026-08-20T00:00:00+00:00',
    resolution: state === 'resolving' ? null : resolution,
    error: null, answers: [],
    _source: { files: null, text: null, case_id: CASE },
  }));
  return id;
}

test('demo: a run still in flight shows the claim plain, with nothing marked', async ({ page }) => {
  const id = seed('demoseed-run', 'resolving');
  await page.goto(`/demo?job=${id}`);

  await expect(page.locator('[data-testid=raw]')).toContainText(CLM_BEFORE);
  await expect(page.locator('[data-testid=annotation]')).toHaveCount(0);
  await expect(page.locator('[data-testid=chip]')).toHaveCount(0);
  await expect(page.locator('[data-testid=corrected]')).toHaveCount(0);
});

test('demo: a running case shows Stop, and Stop cancels that job', async ({ page }) => {
  // The cancel POST is intercepted, so nothing real is killed -- this pins
  // that the button exists while money is being spent and addresses the
  // job on screen.
  const id = seed('demoseed-stoppable', 'resolving');
  const cancels = [];
  await page.route('**/api/queue/*/cancel', route => {
    cancels.push(route.request().url());
    route.fulfill({ status: 200, contentType: 'application/json',
                    body: JSON.stringify({ id, state: 'cancelling' }) });
  });
  await page.goto(`/demo?job=${id}`);
  const stop = page.locator('[data-testid=stop]');
  await expect(stop).toBeVisible();
  await stop.click();
  await expect.poll(() => cancels.length).toBe(1);
  expect(cancels[0]).toContain(id);
});

test('demo: a finished run marks the three lines and produces the corrected claim',
  async ({ page }) => {
  const id = seed('demoseed-done', 'resolved');
  await page.goto(`/demo?job=${id}`);

  const marks = page.locator(
    '[data-testid=annotation][data-artifact="claim_837p.edi"][data-severity=error]');
  await expect(marks).toHaveCount(3);
  for (const code of GP_CODES) await expect(marks.filter({ hasText: code })).toHaveCount(1);
  await expect(page.locator('[data-testid=chip]').first()).toContainText(/GP/i);

  // Right pane: the corrected file, with the frequency code changed to 7.
  const corrected = page.locator('[data-testid=corrected]');
  await expect(corrected).toContainText(CLM_AFTER);
  await expect(corrected.locator('[data-testid=changed]').filter({ hasText: '11:B:7' }))
    .toHaveCount(1);
  // Four changed lines: three modifiers plus the frequency code. Nothing else.
  await expect(corrected.locator('[data-testid=changed]')).toHaveCount(4);
});

test('demo: the corrected pane gives way to a card when there is no file to produce',
  async ({ page }) => {
  const id = 'demoseed-decision';
  seed(id, 'resolved');
  const p = path.join(QUEUE, `${id}.json`);
  const job = JSON.parse(fs.readFileSync(p, 'utf8'));
  job.resolution.resolution.next_action = { path: 'bill_patient', detail: 'Bill the patient.' };
  job.resolution.resolution.corrected_claim = null;
  fs.writeFileSync(p, JSON.stringify(job));

  await page.goto(`/demo?job=${id}`);
  await expect(page.locator('[data-testid=corrected]')).toHaveCount(0);
  await expect(page.locator('[data-testid=card]')).toBeVisible();
  await expect(page.locator('[data-testid=next-action]')).toContainText(/patient/i);

  // No resubmission, no frequency talk. A live bill-patient run once closed
  // its banner with "new original claim (frequency 1)" -- a statement about a
  // resubmission that the resolution explicitly does not make.
  await expect(page.locator('[data-testid=banner]')).toBeVisible();
  await expect(page.locator('[data-testid=banner]')).not.toContainText(/frequency/i);
});

test('demo: a segment repeated verbatim is marked at every occurrence',
  async ({ page }) => {
  // MOH2-000029's remit carries the same LQ*HE*N822~ under each denied line.
  // A real run cited it and the screen showed nothing: the anchorer treated
  // "occurs three times" as "too ambiguous to place". Identical text IS the
  // citation -- all three lines get the mark.
  const id = 'demoseed-repeat';
  seed(id, 'resolved');
  const p = path.join(QUEUE, `${id}.json`);
  const job = JSON.parse(fs.readFileSync(p, 'utf8'));
  job.resolution.resolution.evidence = [{
    artifact: 'remit_835.edi', fact: 'Every line carries remark N822.',
    chip: 'Remark N822 on each line', severity: 'error',
    segments: [{ text: 'LQ*HE*N822~' }],
  }];
  job.resolution.resolution.corrected_claim = null;
  fs.writeFileSync(p, JSON.stringify(job));

  await page.goto(`/demo?job=${id}`);
  await expect(page.locator(
    '[data-testid=annotation][data-artifact="remit_835.edi"]')).toHaveCount(3);
});

test('demo: the audience is told nothing about the backend', async ({ page }) => {
  const id = seed('demoseed-clean', 'resolved');
  await page.goto(`/demo?job=${id}`);

  const body = (await page.locator('body').textContent()).toLowerCase();
  for (const banned of ['opus', 'sonnet', 'claude', 'effort', 'cost_usd']) {
    expect(body, `the demo must not mention "${banned}"`).not.toContain(banned);
  }
  const payload = (await (await page.request.get(`/api/demo/view/${id}`)).text()).toLowerCase();
  for (const banned of ['opus', 'sonnet', 'cost_usd', '_source']) {
    expect(payload, `/api/demo/view must not carry "${banned}"`).not.toContain(banned);
  }
  for (const route of ['/api/spend', '/api/runs', '/api/models']) {
    expect((await page.request.get(route)).status()).toBe(404);
  }
});

test('demo: variants are swappable and a bad variant name is refused', async ({ page }) => {
  const list = await (await page.request.get('/api/demo/variants')).json();
  expect(list.variants).toContain('v1');
  expect(list.default).toBe('v1');

  expect((await page.request.get('/demo?v=v1')).status()).toBe(200);
  expect((await page.request.get('/demo?v=nope')).status()).toBe(404);
  // Untrusted name straight off a URL: no traversal, no absolute paths.
  expect((await page.request.get('/demo?v=..%2F..%2Fstatic')).status()).toBe(400);
});

// ---------------------------------------------------------------------------
// Live. One real resolve of MOH2-000029, end to end through the page.
// ---------------------------------------------------------------------------
test('demo: MOH2-000029 runs end to end, unmarked before and marked after',
  async ({ page }) => {
  test.setTimeout(600_000);
  await page.goto('/demo');

  await expect(page.locator('[data-testid=annotation]')).toHaveCount(0);
  await page.fill('[data-testid=case-input]', CASE);
  await page.click('[data-testid=run]');

  // BEFORE: the artifacts are on screen and carry no annotations at all. This
  // is the assertion the whole design exists to make true.
  const raw = page.locator('[data-testid=raw]');
  await expect(raw).toContainText(CLM_BEFORE, { timeout: 60_000 });
  await expect(page.locator('[data-testid=annotation]')).toHaveCount(0);
  await expect(page.locator('[data-testid=chip]')).toHaveCount(0);

  // The timer runs on real elapsed time while the model works.
  await expect(page.locator('[data-testid=timer]')).toHaveText(/[1-9]/, { timeout: 30_000 });

  // AFTER: the run lands and the findings are placed.
  const corrected = page.locator('[data-testid=corrected]');
  const card = page.locator('[data-testid=card]');
  await expect(card).toBeVisible({ timeout: 540_000 });

  // The three GP-modifier highlights, on the claim, marked as the defect
  // itself rather than as supporting context.
  const marks = page.locator(
    '[data-testid=annotation][data-artifact="claim_837p.edi"][data-severity=error]');
  await expect(marks).toHaveCount(3);
  for (const code of GP_CODES) {
    await expect(marks.filter({ hasText: code }),
      `line ${code} must be marked`).toHaveCount(1);
  }

  // And the corrected claim carries the GP modifier on exactly those lines.
  for (const code of GP_CODES) {
    await expect(page.locator('[data-testid=changed]').filter({ hasText: `${code}:GP` }),
      `${code} must gain :GP in the corrected claim`).toHaveCount(1);
  }

  // The claim-frequency line.
  //
  // The mockup says "frequency code 7". On THIS case that is wrong and the run
  // says so: CO-4 + N822 is a return-as-unprocessable, the claim was never
  // adjudicated, and reference/runtime/08-therapy-modifiers.md requires a new
  // original claim -- "not a corrected 7" -- while 00-group-codes.md notes that
  // Part B rejects frequency 7 either way. So the assertion is that the screen
  // states the frequency decision and states the correct one. Asserting a 7
  // here would only pass by making the system give a biller the wrong answer.
  const freqLine = page.locator('[data-testid=banner], [data-testid=corrected-note]');
  await expect(freqLine.first()).toBeVisible();
  const freqText = (await freqLine.allTextContents()).join(' ');
  expect(freqText, 'the frequency decision must be stated on screen')
    .toMatch(/frequency|CLM05-3/i);
  expect(freqText, 'Part B rejects frequency 7 on an unprocessable claim')
    .not.toMatch(/frequency code 7/i);
});

// ---------------------------------------------------------------------------
// Parked cases, seeded (free). The model stops and asks; the demo must show
// the settled ground, take an answer through the dialog, and afterwards show
// the verification trail. All rendering, no API spend.
// ---------------------------------------------------------------------------
const PARKED_SEGMENT = 'CAS*CO*4*77.92~';

function seedParked(id) {
  const resolution = {
    schema_version: '1.0', case_id: CASE, status: 'awaiting_human',
    rationale: 'Defect signature is settled; the disposition is not.',
    usage: { cost_usd: 0.2, model: 'claude-opus-5', effort: 'high' },
    awaiting_human: {
      question: 'Was a corrected claim already submitted for PA25896500?',
      why_needed: 'A prior corrected submission changes the vehicle.',
      blocks: ['next_action.path'], asked_of: 'provider',
    },
    partial: {
      evidence: [
        { artifact: 'remit_835.edi', fact: 'All three lines carry CO-4 with N822.',
          chip: 'Missing modifier on every line', severity: 'error',
          segments: [{ text: PARKED_SEGMENT }] },
        { artifact: 'chart_note.txt', fact: 'PT plan of care documented.',
          chip: 'Physical therapy confirmed', severity: 'context', segments: [] },
      ],
      denial: { group: 'CO', carc: '4', rarc: 'N822', level: 'line' },
    },
  };
  fs.mkdirSync(QUEUE, { recursive: true });
  fs.writeFileSync(path.join(QUEUE, `${id}.json`), JSON.stringify({
    id, label: CASE, state: 'needs_input', input_format: 'edi', case_id: CASE,
    notes: null, created_at: '2026-08-20T00:00:00+00:00',
    updated_at: '2026-08-20T00:00:00+00:00', resolution, error: null,
    answers: [], _source: { files: null, text: null, case_id: CASE },
  }));
  return id;
}

test('demo: a parked case shows the settled ground and asks for one thing',
  async ({ page }) => {
  const id = seedParked('demoseed-parked');
  await page.goto(`/demo?job=${id}`);

  // Right pane: what WAS established, as cards, before any question.
  const est = page.locator('[data-testid=established]');
  await expect(est).toHaveCount(2);
  await expect(est.first()).toContainText('Missing modifier on every line');

  // Left pane: the partial finding is anchored on the real remit line.
  const marks = page.locator('[data-testid=annotation][data-artifact="remit_835.edi"]');
  await expect(marks).toHaveCount(1);
  await expect(marks.first()).toContainText('CAS*CO*4*77.92');

  // The ask, at the bottom, clickable.
  const needs = page.locator('[data-testid=needs-input]');
  await expect(needs).toBeVisible();
  await expect(needs).toContainText('Was a corrected claim already submitted');
});

test('demo: clicking the ask opens a dialog with text and document input',
  async ({ page }) => {
  const id = seedParked('demoseed-dialog');
  await page.goto(`/demo?job=${id}`);

  await page.click('[data-testid=needs-input]');
  const dialog = page.locator('[data-testid=answer-dialog]');
  await expect(dialog).toBeVisible();
  await expect(dialog).toContainText('Was a corrected claim already submitted');
  await expect(dialog).toContainText('Why this matters');
  await expect(dialog.locator('[data-testid=answer-input]')).toBeVisible();
  await expect(dialog.locator('[data-testid=answer-files]')).toBeVisible();

  // An empty answer is refused in the page; the dialog stays up.
  await dialog.locator('[data-testid=submit-answer]').click();
  await expect(dialog).toBeVisible();
});

test('demo: the dialog answers the job it opened for, even after the page moves on',
  async ({ page }) => {
  // A stray submission or a history click can change the page's current job
  // while the dialog sits open. The answer belongs to the QUESTION -- posting
  // it to whatever the page shows now sent a real answer to a job that never
  // asked one. The POST is intercepted, so nothing resumes and nothing spends.
  const asked = seedParked('demoseed-drift-asked');
  const other = seedParked('demoseed-drift-other');

  const posts = [];
  await page.route('**/api/queue/*/answer', route => {
    posts.push(route.request().url());
    route.fulfill({ status: 409, contentType: 'application/json',
                    body: JSON.stringify({ detail: 'intercepted by test' }) });
  });

  await page.goto(`/demo?job=${asked}`);
  await page.click('[data-testid=needs-input]');
  await expect(page.locator('[data-testid=answer-dialog]')).toBeVisible();

  // The page drifts to another case underneath the open dialog.
  await page.evaluate(id => replay(id), other);
  await expect(page.locator('[data-testid=needs-input]')).toBeVisible();

  await page.fill('[data-testid=answer-input]', 'The answer to the first question.');
  await page.click('[data-testid=submit-answer]');

  await expect.poll(() => posts.length).toBe(1);
  expect(posts[0], 'the answer must go to the job whose question was open')
    .toContain(asked);
  expect(posts[0]).not.toContain(other);
});

test('demo: a case answered by a human shows the verification trail',
  async ({ page }) => {
  const id = 'demoseed-trail';
  seed(id, 'resolved');
  const p = path.join(QUEUE, `${id}.json`);
  const job = JSON.parse(fs.readFileSync(p, 'utf8'));
  job.answers = [{
    question: 'Was a corrected claim already submitted for PA25896500?',
    answer: 'No — confirmed with the clearinghouse this morning.',
    at: '2026-08-20T01:00:00+00:00', documents: ['clearinghouse-log.md'],
  }];
  fs.writeFileSync(p, JSON.stringify(job));

  await page.goto(`/demo?job=${id}`);
  const trail = page.locator('[data-testid=trail]');
  await expect(trail).toBeVisible();
  await expect(trail).toContainText('Verified with human input');
  await expect(trail).toContainText('Was a corrected claim already submitted');
  await expect(trail).toContainText('confirmed with the clearinghouse');
  await expect(trail).toContainText('clearinghouse-log.md');
  // And the resolution itself still renders above it.
  await expect(page.locator('[data-testid=card]')).toBeVisible();
});

// ---------------------------------------------------------------------------
// Live. The full human-in-the-loop arc on a case that genuinely parks:
// MOH2-000233's CCMI lives in neither the 835 nor the chart note, and every
// configuration tested refuses to guess it. Two resolves (~$0.50-0.80).
// ---------------------------------------------------------------------------
test('demo live: a parked case takes an answer through the dialog and resumes',
  async ({ page }) => {
  test.setTimeout(900_000);
  const PARKS = 'MOH2-000233';
  await page.goto('/demo');

  await page.fill('[data-testid=case-input]', PARKS);
  await page.click('[data-testid=run]');

  // The artifacts land plain while the model works.
  await expect(page.locator('[data-testid=raw]')).toContainText('CLP', { timeout: 60_000 });
  await expect(page.locator('[data-testid=annotation]')).toHaveCount(0);

  // The model stops and asks -- and shows the ground it DID settle.
  const needs = page.locator('[data-testid=needs-input]');
  await expect(needs).toBeVisible({ timeout: 480_000 });
  await expect(page.locator('[data-testid=established]').first(),
    'a parked case must show what it established before the question')
    .toBeVisible();

  // Answer through the dialog, with a document.
  await needs.click();
  const dialog = page.locator('[data-testid=answer-dialog]');
  await expect(dialog).toBeVisible();
  await dialog.locator('[data-testid=answer-input]').fill(
    'CMS NCCI PTP edit file for the DOS quarter: the 97150/97110 pair carries '
    + 'CCMI 1, so a bypass modifier is permitted where documentation supports it.');
  await dialog.locator('[data-testid=answer-files]').setInputFiles({
    name: 'ncci-ptp-lookup.md', mimeType: 'text/markdown',
    buffer: Buffer.from('# NCCI PTP lookup\n\nColumn One 97150 / Column Two 97110, '
      + 'DOS quarter: Correct Coding Modifier Indicator = 1.\n'),
  });
  await dialog.locator('[data-testid=submit-answer]').click();

  // The resume streams and lands; the trail records the exchange.
  await expect(page.locator('[data-testid=trail]')).toBeVisible({ timeout: 480_000 });
  await expect(page.locator('[data-testid=trail]')).toContainText('ncci-ptp-lookup.md');
  await expect(page.locator('[data-testid=card], [data-testid=corrected]').first())
    .toBeVisible();
});

// ---------------------------------------------------------------------------
// Header rework, upload, history, wrapping. Seeded, free.
// ---------------------------------------------------------------------------
test('demo: the brand is Mohenara alone and the controls are New / Upload / history',
  async ({ page }) => {
  await page.goto('/demo');
  await expect(page.locator('.logo')).toHaveText('MOHENARA');
  expect(await page.title()).toBe('Mohenara');
  await expect(page.locator('[data-testid=new-case]')).toHaveText('+ New');
  // Upload lives IN the intake pane -- the empty state is the invitation --
  // not up in the header next to controls that act on a loaded case.
  await expect(page.locator('[data-testid=raw] [data-testid=upload]')).toBeVisible();
  await expect(page.locator('header [data-testid=upload]')).toHaveCount(0);
  await expect(page.locator('[data-testid=history]')).toBeVisible();
  // The upload control feeds a real file input, so the file picker works.
  await expect(page.locator('[data-testid=upload-input]')).toHaveAttribute('type', 'file');
  // And "+ New" restores the intake state, upload button included.
  await page.click('[data-testid=new-case]');
  await expect(page.locator('[data-testid=raw] [data-testid=upload]')).toBeVisible();
});

test('demo: dropped files stage in the pane and only Resolve submits them', async ({ page }) => {
  // A drop must never start a billed resolve on its own -- it did once, and a
  // stray drop spent real money. The files land in the left pane, plain, and
  // the POST happens only when Resolve case is clicked. The POST is
  // intercepted, so collection and filtering are proven without a resolve.
  // (A synthetic DataTransfer carries no directory entries, so this exercises
  // the plain-files path; the folder walk shares the same filter.)
  const posted = [];
  await page.route('**/api/batch', route => {
    posted.push(route.request().postDataJSON());
    route.fulfill({ status: 500, contentType: 'application/json',
                    body: JSON.stringify({ detail: 'intercepted by test' }) });
  });

  await page.goto('/demo');
  await page.evaluate(() => {
    const dt = new DataTransfer();
    dt.items.add(new File(['ISA*00~'], 'remit_835.edi', { type: 'text/plain' }));
    dt.items.add(new File(['Progress note.'], 'chart_note.txt', { type: 'text/plain' }));
    dt.items.add(new File(['junk'], 'thumbnail.png', { type: 'image/png' }));
    dt.items.add(new File(['junk'], '.DS_Store', { type: 'application/octet-stream' }));
    document.getElementById('leftPane').dispatchEvent(
      new DragEvent('drop', { dataTransfer: dt, bubbles: true }));
  });

  // Staged: the files are on screen, the run button is armed, nothing posted.
  await expect(page.locator('[data-tab="remit_835.edi"]')).toBeVisible();
  await expect(page.locator('[data-tab="chart_note.txt"]')).toBeVisible();
  await expect(page.locator('[data-testid=run]')).toHaveText('Resolve case');
  expect(posted.length, 'a drop must not submit anything').toBe(0);

  await page.click('[data-testid=run]');
  await expect.poll(() => posted.length).toBe(1);
  const denial = posted[0].denials[0];
  expect(Object.keys(denial.files).sort(), 'strays must not ride into the case')
    .toEqual(['chart_note.txt', 'remit_835.edi']);
  expect(denial.input_format).toBe('edi');
});

test('demo: prose artifacts wrap while EDI stays exact', async ({ page }) => {
  const id = seed('demoseed-wrap', 'resolved');
  await page.goto(`/demo?job=${id}`);
  await expect(page.locator('[data-testid=raw]')).toContainText('CLM');
  // chart_note.txt renders in a wrapping container; the EDI files do not.
  await expect(page.locator('[data-file="chart_note.txt"]')).toHaveClass(/wrapfile/);
  await expect(page.locator('[data-file="claim_837p.edi"]')).not.toHaveClass(/wrapfile/);
  // And the note's text row actually wraps rather than escaping the pane.
  await page.click('[data-tab="chart_note.txt"]');
  const row = page.locator('[data-file="chart_note.txt"] .ln span').last();
  const styles = await row.evaluate(el => getComputedStyle(el).whiteSpace);
  expect(styles).toBe('pre-wrap');
});

test('demo: history lists past cases with status dots and a needs-input action',
  async ({ page }) => {
  seed('demoseed-hist-done', 'resolved');
  seedParked('demoseed-hist-need');
  await page.goto('/demo');
  await page.click('[data-testid=history]');

  const panel = page.locator('[data-testid=history-panel]');
  await expect(panel).toBeVisible();
  const done = panel.locator('[data-testid=hist-row]', { hasText: CASE })
    .filter({ has: page.locator('.hdot.done') });
  await expect(done.first()).toBeVisible();

  // Address the SEEDED row by id. This suite shares results/queue/ with the
  // live deployment, and `.first()` on an unfiltered needs-input locator once
  // grabbed a REAL parked case that happened to sort above the seed -- the
  // test then failed against the app behaving correctly.
  const need = panel.locator('[data-testid=hist-row][data-id="demoseed-hist-need"]');
  await expect(need).toBeVisible();
  await expect(need.locator('.hdot.need')).toBeVisible();
  await expect(need.locator('[data-testid=hist-needs]')).toHaveText('Needs input');

  // The needs-input action reopens the case AND lands in the answer dialog.
  await need.locator('[data-testid=hist-needs]').click();
  await expect(page.locator('[data-testid=answer-dialog]')).toBeVisible();
  await expect(page.locator('[data-testid=answer-dialog]'))
    .toContainText('Was a corrected claim already submitted');
});

test('demo: a history row reopens its case', async ({ page }) => {
  const id = seed('demoseed-hist-open', 'resolved');
  await page.goto('/demo');
  await page.click('[data-testid=history]');
  await page.locator(`[data-testid=hist-row][data-id="${id}"]`).click();
  await expect(page.locator('[data-testid=history-panel]')).toBeHidden();
  await expect(page.locator('[data-testid=corrected]')).toBeVisible();
});

// ---------------------------------------------------------------------------
// Mid-run displays, seeded render check (free): each variant puts up its own
// container on a job that is genuinely mid-run.
// ---------------------------------------------------------------------------
for (const v of ['a', 'b', 'c']) {
  test(`demo: mid-run variant ${v.toUpperCase()} renders its display on a running job`,
    async ({ page }) => {
    const id = seed(`demoseed-live-${v}`, 'resolving');
    await page.goto(`/demo?job=${id}&live=${v}`);
    const live = page.locator('[data-testid=live-display]');
    await expect(live).toBeVisible();
    await expect(live).toHaveAttribute('data-variant', v);
    if (v === 'a') await expect(live.locator('[data-testid=live-headline]')).toHaveCount(1);
    if (v === 'b') {
      // A seeded job is stuck in `resolving`: exactly the stages whose facts
      // have been observed are checked, and the model-output stages are NOT --
      // proof the checks follow events, not time on screen.
      const list = live.locator('[data-testid=live-checklist]');
      await expect(list.locator('[data-stage=analyzing]')).toHaveAttribute('data-done', '1');
      await expect(list.locator('[data-stage=drafting]')).toHaveAttribute('data-done', '0');
      await expect(list.locator('[data-stage=evidence]')).toHaveAttribute('data-done', '0');
    }
    if (v === 'c') await expect(live.locator('[data-testid=live-findings]')).toHaveCount(1);
  });
}

// ---------------------------------------------------------------------------
// Mid-run displays, live: one real resolve per variant. Each asserts the
// display carries REAL run content mid-flight, then hands off to the normal
// result view.
// ---------------------------------------------------------------------------
for (const v of ['a', 'b', 'c']) {
  test(`demo live: variant ${v.toUpperCase()} shows the real mid-run and hands off`,
    async ({ page }) => {
    test.setTimeout(600_000);
    await page.goto(`/demo?live=${v}`);
    await page.fill('[data-testid=case-input]', CASE);
    await page.click('[data-testid=run]');

    const live = page.locator('[data-testid=live-display]');
    await expect(live).toBeVisible({ timeout: 60_000 });
    await expect(live).toHaveAttribute('data-variant', v);

    if (v === 'a') {
      // A real sentence from the model's own streaming rationale.
      await expect(live.locator('[data-testid=live-headline]'))
        .not.toBeEmpty({ timeout: 300_000 });
    }
    if (v === 'b') {
      // Stages check off as backend facts arrive: the model writing output is
      // an observed event, not a timer.
      await expect(live.locator('[data-stage=analyzing]'))
        .toHaveAttribute('data-done', '1', { timeout: 120_000 });
      await expect(live.locator('[data-stage=drafting]'))
        .toHaveAttribute('data-done', '1', { timeout: 300_000 });
    }
    if (v === 'c') {
      // At least one finding rendered the moment its object completed.
      await expect(live.locator('[data-testid=live-findings] li').first())
        .toBeVisible({ timeout: 300_000 });
    }

    // Handoff: the live display yields to the normal result view.
    await expect(page.locator('[data-testid=card]')).toBeVisible({ timeout: 540_000 });
    await expect(live).toBeHidden();
    await expect(page.locator(
      '[data-testid=annotation][data-artifact="claim_837p.edi"][data-severity=error]'))
      .toHaveCount(3);
  });
}

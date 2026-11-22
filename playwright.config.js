// Playwright drives the real app against the real API. The frontend tests are
// the only place the operator's actual path is exercised end to end, so mocking
// the resolver here would hollow out the thing being verified.
//
// Cost is contained by pinning these tests to the cheaper model at low effort
// (see VERIFY_MODEL / VERIFY_EFFORT), not by faking the backend.
const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 240_000,           // a real resolve at high effort is slow
  expect: { timeout: 30_000 },
  fullyParallel: false,       // shared inbox + spend ledger on disk
  workers: 1,
  retries: 0,
  reporter: [['list'], ['html', { open: 'never', outputFolder: 'results/playwright-report' }]],
  // This image ships Chromium at /opt/pw-browsers and blocks 'playwright
  // install'. The pinned @playwright/test build looks for a different revision,
  // so point it at the binary that is actually here.
  projects: [
    {
      name: 'operator',
      testMatch: /journeys\.spec\.js/,
      use: {
        browserName: 'chromium',
        baseURL: 'http://127.0.0.1:8765',
        launchOptions: { executablePath: process.env.PW_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' },
      },
    },
    {
      // The outreach demo. Same server as `operator` -- it is a second frontend
      // on the same backend -- but a separate project so the operator suite can
      // be run, and stay green, without the demo's live resolve.
      name: 'demo',
      testMatch: /(?:demo|practice)\.spec\.js/,
      use: {
        browserName: 'chromium',
        baseURL: 'http://127.0.0.1:8765',
        launchOptions: { executablePath: process.env.PW_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' },
      },
    },
    {
      // The internal app is a different process on a different port. Running
      // this spec against the operator server would assert routes that are
      // deliberately absent there, so the two are kept apart.
      name: 'internal',
      testMatch: /internal\.spec\.js/,
      use: {
        browserName: 'chromium',
        baseURL: process.env.INTERNAL_URL || 'http://127.0.0.1:8766',
        launchOptions: { executablePath: process.env.PW_CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' },
      },
    },
  ],
  use: {
    baseURL: 'http://127.0.0.1:8765',
    screenshot: 'only-on-failure',   // read the screenshot before fixing
    trace: 'retain-on-failure',
    video: 'off',
  },
  outputDir: 'results/playwright-artifacts',
  webServer: [{
    command: '.venv/bin/uvicorn mohenara.api:app --host 127.0.0.1 --port 8765 --app-dir src',
    // A bare readiness probe. /api/models and /api/spend do not exist on the
    // operator app -- that is the point, and journey 4 asserts it -- so the
    // health check cannot be one of them.
    url: 'http://127.0.0.1:8765/api/health',
    // Default FALSE. With reuse on, a server already listening on this port --
    // one started from the working tree, say -- silently serves the clean
    // checkout's test run, so the verification would pass against code that is
    // not the code being verified. Opt in with PW_REUSE_SERVER=1 for fast local
    // iteration only.
    reuseExistingServer: process.env.PW_REUSE_SERVER === '1',
    timeout: 60_000,
    stdout: 'pipe',
    stderr: 'pipe',
  }, {
    command: '.venv/bin/uvicorn mohenara.internal_api:app --host 127.0.0.1 --port 8766 --app-dir src',
    url: 'http://127.0.0.1:8766/api/spend',
    reuseExistingServer: process.env.PW_REUSE_SERVER === '1',
    timeout: 60_000,
    stdout: 'pipe',
    stderr: 'pipe',
  }],
});

# The app shells out to the Claude Code CLI through the Agent SDK, so it needs
# a real process with Node on PATH -- not a serverless function. That rules out
# Vercel/Lambda-style hosts and makes a container the deployable unit. Anything
# that runs one works: Cloud Run, Fly, Render, ECS, or a plain VM.
FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
      nodejs npm ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# The CLI the SDK drives. Pinned: an unpinned CLI would let the thing under
# test change without a commit.
RUN npm install -g @anthropic-ai/claude-code@2.1.42

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/
COPY reference/ reference/
COPY schema/ schema/
COPY config/ config/
# The corpus is optional: paste and upload work without it. Include it if you
# want the demo to resolve cases by id.
COPY corpus/ corpus/

# The ledger lives here. Mount a volume over it to keep spend across restarts --
# without one, a redeploy resets the budget guard to zero and the cap stops
# meaning anything.
RUN mkdir -p results
VOLUME ["/app/results"]

ENV PYTHONUNBUFFERED=1 PORT=8080
EXPOSE 8080

# Credentials come from the environment at run time, never from the image.
# AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY / AWS_REGION for Bedrock,
# ANTHROPIC_API_KEY for the first-party API.
CMD ["sh", "-c", "uvicorn mohenara.api:app --app-dir src --host 0.0.0.0 --port ${PORT:-8080}"]

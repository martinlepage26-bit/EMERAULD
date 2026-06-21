# backend/Dockerfile
# Production image for the PHAROS FastAPI backend.
# Multi-stage: builder installs deps, final stage is lean.
#
# Build:  docker build -t pharos-backend ./backend
# Run local (port 9202):  docker run -p 9202:9202 --env-file .env pharos-backend
# Run on Railway:         Railway injects $PORT — CMD handles it via ${PORT:-9202}

# ── Stage 1: dependency builder ───────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /build

# Install build tools only in builder stage
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install --no-cache-dir -r requirements.txt


# ── Stage 2: runtime ──────────────────────────────────────────────────────────
FROM python:3.11-slim AS runtime

WORKDIR /app

# Non-root user for security
RUN addgroup --system pharos && adduser --system --ingroup pharos pharos

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application source
COPY . .

# Ownership
RUN chown -R pharos:pharos /app

USER pharos

# Expose the default local port
EXPOSE 9202

# Health check — hits /api/health (no curl dep required on slim image)
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT:-9202}/api/health')" || exit 1

# Launch uvicorn.
# ${PORT:-9202}: Railway injects $PORT at runtime; local Docker runs default to 9202.
# Using shell form (not exec/JSON array) so $PORT is expanded by the shell.
# --workers 2: adequate for Railway hobby/starter tier; scale up on larger plans.
CMD uvicorn server:app \
    --host 0.0.0.0 \
    --port ${PORT:-9202} \
    --workers 2 \
    --log-level info \
    --access-log

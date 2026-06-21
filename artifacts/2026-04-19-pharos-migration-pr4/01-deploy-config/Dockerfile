# backend/Dockerfile
# Production image for the PHAROS FastAPI backend.
# Multi-stage: builder installs deps, final stage is lean.
#
# Build:  docker build -t pharos-backend ./backend
# Run:    docker run -p 9202:9202 --env-file .env pharos-backend

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

# Expose the API port
EXPOSE 9202

# Health check — hits the root endpoint (add /api/health if not present)
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:9202/api/health')" || exit 1

# Launch uvicorn in production mode
# Workers: 2 * CPU + 1 is the standard formula; clamp to 4 for small hosts
CMD ["uvicorn", "server:app", \
     "--host", "0.0.0.0", \
     "--port", "9202", \
     "--workers", "2", \
     "--log-level", "info", \
     "--access-log"]

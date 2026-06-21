"""
LightRAG configuration for EMERAULD vault.
LLM: OpenRouter when OPENROUTER_API_KEY is set; otherwise Claude via Anthropic
Embeddings: sentence-transformers/all-MiniLM-L6-v2 (local, free)
Storage: file-based (NetworkX graph, NanoVectorDB, JsonKV)
"""

import json
import os
import time
from pathlib import Path

def resolve_vault_root() -> Path:
    """
    Resolve the vault root in a way that works both:
    - inside this git checkout (default), and
    - in the original WSL/Windows location via env override.

    Env override: EMERAULD_VAULT_ROOT=/mnt/c/Users/softinfo/Documents/EMERAULD
    """
    override = (os.environ.get("EMERAULD_VAULT_ROOT") or "").strip()
    if override:
        return Path(override)
    return Path(__file__).resolve().parents[1]


VAULT_ROOT = resolve_vault_root()
STORAGE_DIR = VAULT_ROOT / ".lightrag" / "storage"
VENV_PYTHON = "/home/martin/.venvs/emerauld/bin/python3"

EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
EMBED_DIM = 384

ANTHROPIC_MODEL = "claude-haiku-4-5-20251001"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
CREDENTIALS_FILE = Path.home() / ".claude" / ".credentials.json"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "openai/gpt-4o-mini")

_last_call = 0.0
_MIN_INTERVAL = 1.0
_embed_model = None


def resolve_embed_model_path() -> str:
    """
    Prefer local HuggingFace cache to avoid hub network calls. This keeps vault
    ingest resilient even when DNS/network is flaky.
    """
    env_override = (os.environ.get("EMERAULD_EMBED_MODEL_PATH") or "").strip()
    if env_override:
        return env_override

    hub_root = Path.home() / ".cache" / "huggingface" / "hub"
    cached = hub_root / "models--sentence-transformers--all-MiniLM-L6-v2" / "snapshots"
    if cached.exists():
        snapshots = sorted(
            (p for p in cached.iterdir() if p.is_dir()),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        if snapshots:
            return str(snapshots[0])

    return f"sentence-transformers/{EMBED_MODEL_NAME}"


async def get_api_token(force_refresh: bool = False) -> str:
    env_token = (
        os.environ.get("ANTHROPIC_API_KEY")
        or os.environ.get("CLAUDE_API_KEY")
        or ""
    ).strip()
    if env_token:
        return env_token

    if not CREDENTIALS_FILE.exists():
        raise RuntimeError(
            "Claude credentials not found. Set ANTHROPIC_API_KEY (or CLAUDE_API_KEY), "
            f"or sign into Claude Code to create {CREDENTIALS_FILE}."
        )

    data = json.loads(CREDENTIALS_FILE.read_text(encoding="utf-8"))
    oauth = data.get("claudeAiOauth")
    if not oauth:
        raise RuntimeError(f"Claude OAuth credentials not found in {CREDENTIALS_FILE}")

    token = oauth.get("accessToken")
    expires_at = oauth.get("expiresAt", 0) / 1000  # ms -> seconds
    if force_refresh or time.time() >= expires_at - 60:  # refresh 60s before expiry or on demand
        import httpx

        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.post(
                "https://auth.anthropic.com/oauth/token",
                data={
                    "grant_type": "refresh_token",
                    "refresh_token": oauth["refreshToken"],
                    "client_id": "claude-code",
                },
            )
            if r.status_code != 200:
                raise RuntimeError(
                    f"Failed to refresh Claude OAuth token ({r.status_code}): {r.text}"
                )

            new_data = r.json()
            token = new_data.get("access_token")
            if not token:
                raise RuntimeError("Claude OAuth refresh did not return an access token")

            oauth["accessToken"] = token
            oauth["expiresAt"] = int(time.time() * 1000) + new_data.get("expires_in", 3600) * 1000
            data["claudeAiOauth"] = oauth
            CREDENTIALS_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

    if not token:
        raise RuntimeError(f"Claude OAuth access token missing in {CREDENTIALS_FILE}")

    return token


def get_embed_model():
    global _embed_model
    if _embed_model is None:
        from sentence_transformers import SentenceTransformer

        _embed_model = SentenceTransformer(resolve_embed_model_path())
    return _embed_model


async def embedding_func(texts: list[str]):
    import numpy as np

    model = get_embed_model()
    embeddings = model.encode(texts, normalize_embeddings=True)
    return np.array(embeddings, dtype=np.float32)


async def llm_func(
    prompt: str,
    system_prompt: str | None = None,
    history_messages: list | None = None,
    **kwargs,
) -> str:
    global _last_call

    import asyncio
    import httpx

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    for msg in history_messages or []:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": prompt})

    openrouter_token = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if openrouter_token:
        return await openrouter_llm_func(messages)

    anthropic_messages = [m for m in messages if m["role"] != "system"]
    force_refresh = False
    for attempt in range(5):
        gap = _MIN_INTERVAL - (time.monotonic() - _last_call)
        if gap > 0:
            await asyncio.sleep(gap)

        try:
            token = await get_api_token(force_refresh=force_refresh)
            force_refresh = False  # consume the flag
            headers = {
                "x-api-key": token,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            }
            body = {
                "model": ANTHROPIC_MODEL,
                "max_tokens": 4096,
                "messages": anthropic_messages,
            }
            if system_prompt:
                body["system"] = system_prompt

            async with httpx.AsyncClient(timeout=120) as client:
                response = await client.post(ANTHROPIC_URL, headers=headers, json=body)
                _last_call = time.monotonic()

                if response.status_code == 401 and attempt < 4:
                    # Token may have become invalid mid-run (race with expiry,
                    # upstream rotation, transient 401). Force-refresh and retry once.
                    force_refresh = True
                    await asyncio.sleep(1)
                    continue

                if response.status_code == 429:
                    await asyncio.sleep(20 * (2 ** attempt))
                    continue

                response.raise_for_status()
                return response.json()["content"][0]["text"]

        except (httpx.TimeoutException, httpx.ConnectError, httpx.NetworkError, OSError) as e:
            # Network can be intermittently unavailable (e.g., transient DNS failures).
            # Retry with light backoff rather than failing the whole ingest.
            if isinstance(e, OSError):
                errno = getattr(e, "errno", None)
                if errno not in (-3,):
                    raise

            if attempt < 4:
                await asyncio.sleep(5 * (attempt + 1))
                continue
            raise

    raise RuntimeError("Anthropic: max retries exceeded")


async def openrouter_llm_func(messages: list[dict[str, str]]) -> str:
    global _last_call

    import asyncio
    import httpx

    token = os.environ["OPENROUTER_API_KEY"].strip()
    headers = {
        "authorization": f"Bearer {token}",
        "content-type": "application/json",
        "http-referer": "https://emerauld.local",
        "x-title": "EMERAULD LightRAG",
    }
    body = {
        "model": OPENROUTER_MODEL,
        "max_tokens": 4096,
        "messages": messages,
    }

    for attempt in range(5):
        gap = _MIN_INTERVAL - (time.monotonic() - _last_call)
        if gap > 0:
            await asyncio.sleep(gap)

        try:
            async with httpx.AsyncClient(timeout=120) as client:
                response = await client.post(OPENROUTER_URL, headers=headers, json=body)
                _last_call = time.monotonic()

                if response.status_code == 429:
                    await asyncio.sleep(20 * (2 ** attempt))
                    continue

                response.raise_for_status()
                data = response.json()
                return data["choices"][0]["message"]["content"]

        except (httpx.TimeoutException, httpx.ConnectError, httpx.NetworkError, OSError):
            if attempt < 4:
                await asyncio.sleep(5 * (attempt + 1))
                continue
            raise

    raise RuntimeError("OpenRouter: max retries exceeded")


def make_rag():
    from lightrag import LightRAG
    from lightrag.utils import EmbeddingFunc

    rag = LightRAG(
        working_dir=str(STORAGE_DIR),
        llm_model_func=llm_func,
        embedding_func=EmbeddingFunc(
            embedding_dim=EMBED_DIM,
            max_token_size=512,
            func=embedding_func,
        ),
    )
    return rag

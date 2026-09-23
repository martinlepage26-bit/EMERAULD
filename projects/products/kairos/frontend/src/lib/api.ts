/**
 * One definition of where the API lives and how it is called.
 *
 * The origin was previously pasted into six components. When the Worker moved
 * off its workers.dev hostname, every one of them had to be found by hand, so
 * it lives here now and is overridable per environment.
 */
export const API_BASE = process.env.NEXT_PUBLIC_API_BASE ?? "https://kairos.govern-ai.ca";

export const STORAGE_KEY = "kairos_api_key";

/** Shaped like the Worker's error envelope: `{ error: { code, message } }`. */
export class ApiError extends Error {
  constructor(
    readonly status: number,
    readonly code: string,
    message: string,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

export function storedKey(): string | null {
  try {
    return localStorage.getItem(STORAGE_KEY);
  } catch {
    // Storage can throw outright in a private window or with site data blocked.
    return null;
  }
}

export function storeKey(key: string): void {
  try {
    localStorage.setItem(STORAGE_KEY, key);
  } catch {
    /* A browser that refuses storage still works for the current page load. */
  }
}

export function clearKey(): void {
  try {
    localStorage.removeItem(STORAGE_KEY);
  } catch {
    /* Nothing to clear if storage is unavailable. */
  }
}

async function toError(res: Response): Promise<ApiError> {
  const body = (await res.json().catch(() => null)) as
    | { error?: { code?: string; message?: string } }
    | null;
  return new ApiError(
    res.status,
    body?.error?.code ?? "http_error",
    body?.error?.message ?? `Request failed with ${res.status}`,
  );
}

/** Calls the API without credentials. Used by signup, which mints them. */
export async function apiFetch<T>(path: string, init: RequestInit = {}): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers: {
      ...(init.body ? { "content-type": "application/json" } : {}),
      ...init.headers,
    },
  });
  if (!res.ok) throw await toError(res);
  return (await res.json()) as T;
}

/** Calls the API with a bearer key, defaulting to the one this browser holds. */
export async function authedFetch<T>(
  path: string,
  init: RequestInit = {},
  key: string | null = storedKey(),
): Promise<T> {
  if (!key) throw new ApiError(401, "no_key", "This browser has no API key.");
  return apiFetch<T>(path, {
    ...init,
    headers: { ...init.headers, authorization: `Bearer ${key}` },
  });
}

/** True when the key is currently accepted. Used to gate the dashboard. */
export async function verifyKey(key: string): Promise<boolean> {
  try {
    await authedFetch("/v1/me", {}, key);
    return true;
  } catch {
    // A network or CORS failure is indistinguishable from a bad key here, and
    // both mean the same thing to the caller: this key cannot be used yet.
    return false;
  }
}

/** `PLANS` in the Worker derives these; they are the checkout's price handles. */
export function priceLookupKey(planId: string): string {
  return `kairos_${planId}_monthly`;
}

export interface SignupResult {
  accountId: string;
  apiKey: string;
  trialEndsAt: string;
  note: string;
}

export function signup(input: {
  email: string;
  displayName: string;
  timezone?: string;
}): Promise<SignupResult> {
  return apiFetch<SignupResult>("/v1/accounts", {
    method: "POST",
    body: JSON.stringify({
      ...input,
      timezone:
        input.timezone ??
        Intl.DateTimeFormat().resolvedOptions().timeZone ??
        "UTC",
    }),
  });
}

export function startCheckout(planId: string, key: string): Promise<{ url?: string }> {
  return authedFetch<{ url?: string }>(
    "/v1/billing/checkout",
    { method: "POST", body: JSON.stringify({ priceLookupKey: priceLookupKey(planId) }) },
    key,
  );
}

import { RetryableError } from '../lib/errors';

export interface HttpJsonOptions {
  method?: string;
  token: string;
  body?: unknown;
  headers?: Record<string, string>;
}

/**
 * Shared fetch wrapper for platform APIs.
 *
 * The important behaviour is the error classification: 429 and 5xx become
 * retryable so the queue backs off and tries again, while 4xx becomes permanent
 * so a malformed post does not retry five times and then still fail. Getting
 * this backwards is how scheduled content silently disappears.
 */
export async function httpJson<T>(url: string, opts: HttpJsonOptions): Promise<T> {
  let res: Response;
  try {
    res = await fetch(url, {
      method: opts.method ?? 'GET',
      headers: {
        authorization: `Bearer ${opts.token}`,
        'content-type': 'application/json',
        ...opts.headers,
      },
      body: opts.body === undefined ? undefined : JSON.stringify(opts.body),
    });
  } catch (err) {
    throw new RetryableError(`Network failure calling ${hostOf(url)}: ${String(err)}`, 30);
  }

  if (res.status === 429) {
    const retryAfter = Number.parseInt(res.headers.get('retry-after') ?? '', 10);
    throw new RetryableError(
      `${hostOf(url)} rate limited`,
      Number.isFinite(retryAfter) ? retryAfter : 120,
    );
  }
  if (res.status >= 500) {
    throw new RetryableError(`${hostOf(url)} returned ${res.status}`, 60);
  }
  if (!res.ok) {
    const detail = (await res.text().catch(() => '')).slice(0, 500);
    throw new Error(`${hostOf(url)} returned ${res.status}: ${detail}`);
  }

  return (await res.json()) as T;
}

function hostOf(url: string): string {
  try {
    return new URL(url).host;
  } catch {
    return url;
  }
}

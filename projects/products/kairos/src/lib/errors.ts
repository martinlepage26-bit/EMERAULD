export class AppError extends Error {
  constructor(
    readonly status: number,
    readonly code: string,
    message: string,
    readonly detail?: unknown,
  ) {
    super(message);
    this.name = 'AppError';
  }
}

export const badRequest = (msg: string, detail?: unknown) =>
  new AppError(400, 'bad_request', msg, detail);
export const unauthorized = (msg = 'Missing or invalid credentials') =>
  new AppError(401, 'unauthorized', msg);
export const forbidden = (msg = 'Not permitted') => new AppError(403, 'forbidden', msg);
export const notFound = (what: string) => new AppError(404, 'not_found', `${what} not found`);
export const conflict = (msg: string) => new AppError(409, 'conflict', msg);
export const tooManyRequests = (msg: string) => new AppError(429, 'rate_limited', msg);

/**
 * A failure the job runner should retry rather than bury. Distinguishing these
 * from permanent failures is what keeps a transient platform outage from
 * silently dropping a day of scheduled posts.
 */
export class RetryableError extends Error {
  constructor(message: string, readonly retryAfterSeconds = 60) {
    super(message);
    this.name = 'RetryableError';
  }
}

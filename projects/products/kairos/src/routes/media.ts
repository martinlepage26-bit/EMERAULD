import { Hono } from 'hono';
import type { AppBindings } from '../env';
import { notFound } from '../lib/errors';

export const media = new Hono<AppBindings>();

/**
 * Serves post media to the platforms that fetch it at publish time.
 *
 * This endpoint is deliberately unauthenticated: X and LinkedIn fetch the URL
 * from their own infrastructure, carrying none of our credentials. Access
 * control is therefore the unguessability of the key itself, the same
 * capability-URL model a CDN uses. Keys are generated server-side and include a
 * random segment, so possession of the URL is the authorization.
 *
 * Two consequences worth stating plainly: anyone given the URL can fetch the
 * object for as long as it exists, and the key must never be derived from
 * user-supplied text, or it becomes guessable.
 */
media.get('/media/:key{.+}', async (c) => {
  const key = c.req.param('key');

  // Reject traversal and absolute forms before they reach R2. R2 keys are flat
  // strings so `..` has no special meaning there, but rejecting them keeps the
  // key space aligned with what the writer side generates.
  if (!key || key.includes('..') || key.startsWith('/')) {
    throw notFound('Media object');
  }

  const object = await c.env.MEDIA.get(key);
  if (!object) throw notFound('Media object');

  const headers = new Headers();
  object.writeHttpMetadata(headers);
  headers.set('etag', object.httpEtag);
  // Media is immutable once written: the key changes when the bytes change.
  headers.set('cache-control', 'public, max-age=31536000, immutable');
  // Capability URLs should not end up in a search index.
  headers.set('x-robots-tag', 'noindex, nofollow');
  if (!headers.has('content-type')) {
    headers.set('content-type', 'application/octet-stream');
  }

  return new Response(object.body, { headers });
});

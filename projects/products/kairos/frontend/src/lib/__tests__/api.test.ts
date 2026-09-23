import {
  ApiError,
  apiFetch,
  authedFetch,
  clearKey,
  priceLookupKey,
  signup,
  startCheckout,
  storeKey,
  storedKey,
  verifyKey,
} from '../api'

const mockFetch = jest.fn()
global.fetch = mockFetch as unknown as typeof fetch

function jsonResponse(body: unknown, status = 200): Response {
  return {
    ok: status >= 200 && status < 300,
    status,
    json: async () => body,
  } as Response
}

beforeEach(() => {
  mockFetch.mockReset()
  localStorage.clear()
})

describe('key storage', () => {
  it('round-trips and clears a key', () => {
    expect(storedKey()).toBeNull()
    storeKey('kai_sk_abc')
    expect(storedKey()).toBe('kai_sk_abc')
    clearKey()
    expect(storedKey()).toBeNull()
  })
})

describe('apiFetch', () => {
  it('surfaces the API error envelope rather than a bare status', async () => {
    mockFetch.mockResolvedValue(
      jsonResponse({ error: { code: 'conflict', message: 'An account already exists' } }, 409),
    )

    await expect(apiFetch('/v1/accounts', { method: 'POST', body: '{}' })).rejects.toMatchObject({
      status: 409,
      code: 'conflict',
      message: 'An account already exists',
    })
  })

  it('falls back to a usable message when the body is not the error envelope', async () => {
    mockFetch.mockResolvedValue({
      ok: false,
      status: 502,
      json: async () => {
        throw new Error('not json')
      },
    } as unknown as Response)

    await expect(apiFetch('/health')).rejects.toBeInstanceOf(ApiError)
  })

  it('sets a JSON content type only when there is a body', async () => {
    mockFetch.mockResolvedValue(jsonResponse({ ok: true }))
    await apiFetch('/health')

    const [, init] = mockFetch.mock.calls[0]
    expect(init.headers['content-type']).toBeUndefined()
  })
})

describe('authedFetch', () => {
  it('sends the stored key as a bearer token', async () => {
    storeKey('kai_sk_stored')
    mockFetch.mockResolvedValue(jsonResponse({ account: {} }))

    await authedFetch('/v1/me')

    const [, init] = mockFetch.mock.calls[0]
    expect(init.headers.authorization).toBe('Bearer kai_sk_stored')
  })

  it('fails before the network when this browser holds no key', async () => {
    await expect(authedFetch('/v1/me')).rejects.toMatchObject({ status: 401, code: 'no_key' })
    expect(mockFetch).not.toHaveBeenCalled()
  })
})

describe('verifyKey', () => {
  it('accepts a key the API accepts', async () => {
    mockFetch.mockResolvedValue(jsonResponse({ account: {} }))
    await expect(verifyKey('kai_sk_good')).resolves.toBe(true)
  })

  it('rejects a key the API refuses', async () => {
    mockFetch.mockResolvedValue(jsonResponse({ error: { code: 'unauthorized' } }, 401))
    await expect(verifyKey('kai_sk_bad')).resolves.toBe(false)
  })

  it('reports false rather than throwing when the request cannot be made at all', async () => {
    // This is the CORS and offline case: the browser rejects before a status exists.
    mockFetch.mockRejectedValue(new TypeError('Failed to fetch'))
    await expect(verifyKey('kai_sk_any')).resolves.toBe(false)
  })
})

describe('checkout', () => {
  it('derives the price lookup key the Worker expects', () => {
    expect(priceLookupKey('pro')).toBe('kairos_pro_monthly')
  })

  it('posts priceLookupKey with the bearer key, not a bare plan name', async () => {
    mockFetch.mockResolvedValue(jsonResponse({ url: 'https://checkout.stripe.com/x' }))

    await startCheckout('studio', 'kai_sk_live')

    const [url, init] = mockFetch.mock.calls[0]
    expect(url).toContain('/v1/billing/checkout')
    expect(init.headers.authorization).toBe('Bearer kai_sk_live')
    expect(JSON.parse(init.body)).toEqual({ priceLookupKey: 'kairos_studio_monthly' })
  })
})

describe('signup', () => {
  it('always sends a timezone, defaulting to the browser resolved one', async () => {
    mockFetch.mockResolvedValue(jsonResponse({ accountId: 'acct_1', apiKey: 'kai_sk_new' }, 201))

    await signup({ email: 'a@b.test', displayName: 'A' })

    const [, init] = mockFetch.mock.calls[0]
    expect(JSON.parse(init.body).timezone).toBeTruthy()
  })
})

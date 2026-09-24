import { render, screen, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { DashboardShell as DashboardLayout } from '@/components/DashboardShell'

const mockFetch = jest.fn()
global.fetch = mockFetch as unknown as typeof fetch

function jsonResponse(body: unknown, status = 200): Response {
  return { ok: status >= 200 && status < 300, status, json: async () => body } as Response
}

beforeEach(() => {
  mockFetch.mockReset()
  localStorage.clear()
})

const child = <p>dashboard content</p>

describe('dashboard key gate', () => {
  it('does not render children until a key is verified', async () => {
    render(<DashboardLayout>{child}</DashboardLayout>)

    await screen.findByText('Connect this browser')
    expect(screen.queryByText('dashboard content')).not.toBeInTheDocument()
  })

  it('never reads a key from the build environment', async () => {
    // The regression this guards: NEXT_PUBLIC_ADMIN_API_KEY used to seed the
    // key here, which shipped a working credential in the client bundle.
    process.env.NEXT_PUBLIC_ADMIN_API_KEY = 'kai_sk_should_never_be_used'

    render(<DashboardLayout>{child}</DashboardLayout>)

    await screen.findByText('Connect this browser')
    expect(mockFetch).not.toHaveBeenCalled()
    expect(localStorage.getItem('kairos_api_key')).toBeNull()

    delete process.env.NEXT_PUBLIC_ADMIN_API_KEY
  })

  it('renders children when a stored key still verifies', async () => {
    localStorage.setItem('kairos_api_key', 'kai_sk_good')
    mockFetch.mockResolvedValue(jsonResponse({ account: {} }))

    render(<DashboardLayout>{child}</DashboardLayout>)

    expect(await screen.findByText('dashboard content')).toBeInTheDocument()
  })

  it('clears a stored key the API now rejects and explains why', async () => {
    localStorage.setItem('kairos_api_key', 'kai_sk_revoked')
    mockFetch.mockResolvedValue(jsonResponse({ error: { code: 'unauthorized' } }, 401))

    render(<DashboardLayout>{child}</DashboardLayout>)

    expect(await screen.findByText(/no longer valid/i)).toBeInTheDocument()
    expect(localStorage.getItem('kairos_api_key')).toBeNull()
  })

  it('verifies a pasted key before storing it', async () => {
    const user = userEvent.setup()
    mockFetch.mockResolvedValue(jsonResponse({ error: { code: 'unauthorized' } }, 401))

    render(<DashboardLayout>{child}</DashboardLayout>)
    await screen.findByText('Connect this browser')

    await user.type(screen.getByPlaceholderText('kai_sk_…'), 'kai_sk_wrong')
    await user.click(screen.getByRole('button', { name: /connect/i }))

    expect(await screen.findByText(/was rejected/i)).toBeInTheDocument()
    // The point: a bad key is not written to storage on the way to failing.
    expect(localStorage.getItem('kairos_api_key')).toBeNull()
  })

  it('stores a pasted key that verifies and opens the dashboard', async () => {
    const user = userEvent.setup()
    mockFetch.mockResolvedValue(jsonResponse({ account: {} }))

    render(<DashboardLayout>{child}</DashboardLayout>)
    await screen.findByText('Connect this browser')

    await user.type(screen.getByPlaceholderText('kai_sk_…'), 'kai_sk_right')
    await user.click(screen.getByRole('button', { name: /connect/i }))

    expect(await screen.findByText('dashboard content')).toBeInTheDocument()
    expect(localStorage.getItem('kairos_api_key')).toBe('kai_sk_right')
  })

  it('disconnect clears the key and closes the dashboard', async () => {
    const user = userEvent.setup()
    localStorage.setItem('kairos_api_key', 'kai_sk_good')
    mockFetch.mockResolvedValue(jsonResponse({ account: {} }))

    render(<DashboardLayout>{child}</DashboardLayout>)
    await screen.findByText('dashboard content')

    await user.click(screen.getByRole('button', { name: /disconnect/i }))

    await waitFor(() => expect(localStorage.getItem('kairos_api_key')).toBeNull())
    expect(screen.queryByText('dashboard content')).not.toBeInTheDocument()
  })
})

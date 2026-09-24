import { metadata as root } from '../layout'
import { metadata as dashboard } from '../dashboard/layout'
import { metadata as calendar } from '../dashboard/calendar/layout'
import { metadata as posts } from '../dashboard/posts/layout'
import { metadata as inbox } from '../dashboard/inbox/layout'
import { metadata as insights } from '../dashboard/insights/layout'

// The app shipped to Pages with the create-next-app defaults still in place, so
// every tab read "Create Next App". These assert the scaffold text is gone and
// each route names itself.

const SCAFFOLD = /create next app/i

describe('page titles', () => {
  it('root carries no scaffold text', () => {
    const title = root.title as { default: string; template: string }
    expect(title.default).toBe('Kairos')
    expect(title.default).not.toMatch(SCAFFOLD)
    expect(String(root.description)).not.toMatch(SCAFFOLD)
  })

  it('root template nests route titles under the product name', () => {
    const title = root.title as { default: string; template: string }
    expect(title.template).toBe('%s · Kairos')
  })

  it('dashboard re-declares the template so nested routes keep the product name', () => {
    // title.template applies only to the segment directly below the one that
    // defines it, so the root template does not reach /dashboard/calendar.
    const title = dashboard.title as { default: string; template: string }
    expect(title.default).toBe('Overview')
    expect(title.template).toBe('%s · Kairos')
  })

  it.each([
    ['calendar', calendar, 'Calendar'],
    ['posts', posts, 'Posts & Drafts'],
    ['inbox', inbox, 'Inbox'],
    ['insights', insights, 'Insights'],
  ])('%s names itself', (_route, meta, expected) => {
    expect(meta.title).toBe(expected)
  })
})

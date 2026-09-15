import { httpJson } from './http';
import {
  EMPTY_METRICS,
  type InboundMessage,
  type MetricsSnapshot,
  type PlatformAdapter,
  type PublishInput,
  type PublishResult,
  type ReplyInput,
} from './types';

const API = 'https://api.linkedin.com/rest';
const VERSION_HEADER = { 'LinkedIn-Version': '202605', 'X-Restli-Protocol-Version': '2.0.0' };

interface PostsResponse {
  id: string;
}

interface CommentsResponse {
  elements?: Array<{
    id: string;
    actor: string;
    message?: { text?: string };
    created?: { time?: number };
    object?: string;
  }>;
}

interface SocialActionsResponse {
  likesSummary?: { totalLikes?: number };
  commentsSummary?: { aggregatedTotalComments?: number };
}

export class LinkedInAdapter implements PlatformAdapter {
  readonly platform = 'linkedin';

  async publish(input: PublishInput): Promise<PublishResult> {
    if (!input.externalAccountId) {
      throw new Error('LinkedIn publishing requires the member or organization URN');
    }

    const res = await httpJson<PostsResponse>(`${API}/posts`, {
      method: 'POST',
      token: input.accessToken,
      headers: VERSION_HEADER,
      body: {
        author: input.externalAccountId,
        commentary: input.body,
        visibility: 'PUBLIC',
        distribution: { feedDistribution: 'MAIN_FEED' },
        lifecycleState: 'PUBLISHED',
      },
    });

    return {
      externalPostId: res.id,
      url: `https://www.linkedin.com/feed/update/${res.id}`,
    };
  }

  async fetchInbound(accessToken: string, since: string): Promise<InboundMessage[]> {
    // LinkedIn scopes comment reads to a single post rather than offering an
    // account-wide inbox, so the engine walks recent posts and this method
    // returns comments for whichever post is passed as the `since` cursor.
    const res = await httpJson<CommentsResponse>(
      `${API}/socialActions/${encodeURIComponent(since)}/comments`,
      { token: accessToken, headers: VERSION_HEADER },
    );

    return (res.elements ?? [])
      .filter((c) => c.message?.text)
      .map((c) => ({
        threadId: c.object ?? since,
        externalId: c.id,
        authorHandle: c.actor,
        body: c.message?.text ?? '',
        createdAt: new Date(c.created?.time ?? Date.now()).toISOString(),
      }));
  }

  async fetchMetrics(accessToken: string, externalPostId: string): Promise<MetricsSnapshot> {
    const res = await httpJson<SocialActionsResponse>(
      `${API}/socialActions/${encodeURIComponent(externalPostId)}`,
      { token: accessToken, headers: VERSION_HEADER },
    );

    return {
      ...EMPTY_METRICS,
      likes: res.likesSummary?.totalLikes ?? 0,
      comments: res.commentsSummary?.aggregatedTotalComments ?? 0,
    };
  }

  async sendReply(input: ReplyInput): Promise<{ externalId: string }> {
    const res = await httpJson<{ id: string }>(
      `${API}/socialActions/${encodeURIComponent(input.threadId)}/comments`,
      {
        method: 'POST',
        token: input.accessToken,
        headers: VERSION_HEADER,
        body: { message: { text: input.body } },
      },
    );
    return { externalId: res.id };
  }
}

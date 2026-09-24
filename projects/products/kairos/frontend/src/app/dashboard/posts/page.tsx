"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import { FileText, Check } from "lucide-react";
import { format, parseISO } from "date-fns";
import { authedFetch } from "@/lib/api";
import { EmptyState, LoadError, Loading } from "@/components/LoadState";

interface Post {
  id: string;
  slot_id: string;
  hook: string | null;
  body: string;
  status: string;
  variant: number;
  platform: string;
  published_at: string | null;
  external_url: string | null;
}

interface Slot {
  id: string;
  scheduled_for: string;
  status: string;
  pillar: string;
  platform: string;
  handle: string;
}

interface Group {
  slot: Slot;
  posts: Post[];
}

const TABS = [
  { key: "review", label: "To review" },
  { key: "scheduled", label: "Scheduled" },
  { key: "published", label: "Published" },
] as const;
type TabKey = (typeof TABS)[number]["key"];

const PLATFORM: Record<string, string> = { x: "X", linkedin: "LinkedIn", instagram: "Instagram", threads: "Threads" };

/** The body usually opens with the hook; show it once. */
function Text({ post }: { post: Post }) {
  const hook = post.hook?.trim() ?? "";
  const body = post.body.trim();
  const showHook = hook !== "" && !body.startsWith(hook);
  return (
    <div className="text-gray-900 whitespace-pre-wrap leading-relaxed">
      {showHook && <p className="font-semibold mb-2">{hook}</p>}
      {body}
    </div>
  );
}

export default function PostsPage() {
  const [tab, setTab] = useState<TabKey>("review");
  const [posts, setPosts] = useState<Post[] | null>(null);
  const [slots, setSlots] = useState<Slot[] | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [acting, setActing] = useState<string | null>(null);

  const load = useCallback(() => {
    Promise.all([
      authedFetch<{ posts: Post[] }>("/v1/posts?limit=200"),
      authedFetch<{ slots: Slot[] }>("/v1/calendar?days=60"),
    ])
      .then(([p, c]) => {
        setPosts(p.posts ?? []);
        setSlots(c.slots ?? []);
      })
      .catch(setError);
  }, []);

  useEffect(() => {
    load();
  }, [load]);

  const groups = useMemo(() => {
    if (!posts || !slots) return null;
    const bySlot = new Map<string, Group>();
    for (const s of slots) bySlot.set(s.id, { slot: s, posts: [] });
    for (const p of posts) bySlot.get(p.slot_id)?.posts.push(p);
    const all = [...bySlot.values()].filter((g) => g.posts.length > 0);
    all.sort((a, b) => a.slot.scheduled_for.localeCompare(b.slot.scheduled_for));
    return {
      review: all.filter((g) => g.slot.status === "ready"),
      scheduled: all.filter((g) => ["approved", "publishing"].includes(g.slot.status)),
      published: all.filter((g) => g.slot.status === "published").reverse(),
    };
  }, [posts, slots]);

  const act = async (id: string, action: "approve" | "reject") => {
    setActing(id);
    try {
      await authedFetch(`/v1/posts/${id}/${action}`, { method: "POST", body: "{}" });
      load();
    } catch (err) {
      setError(err as Error);
    }
    setActing(null);
  };

  const shown = groups?.[tab] ?? [];

  return (
    <div>
      <h1 className="text-2xl sm:text-3xl font-bold mb-2">Posts</h1>
      <p className="text-gray-500 mb-6">
        Each upcoming post has three versions written in your voice. Choose the one to publish.
      </p>

      <div className="flex gap-4 border-b mb-8 overflow-x-auto">
        {TABS.map((t) => (
          <button
            key={t.key}
            onClick={() => setTab(t.key)}
            className={
              t.key === tab
                ? "pb-2 border-b-2 border-black font-medium whitespace-nowrap"
                : "pb-2 text-gray-500 hover:text-black whitespace-nowrap"
            }
          >
            {t.label}
            {groups && <span className="ml-1.5 text-xs text-gray-400">{groups[t.key].length}</span>}
          </button>
        ))}
      </div>

      {error ? (
        <LoadError error={error} />
      ) : !groups ? (
        <Loading />
      ) : shown.length === 0 ? (
        <EmptyState icon={<FileText className="w-8 h-8" />}>
          {tab === "review"
            ? "Nothing waiting for you. New drafts appear here as the calendar fills."
            : tab === "scheduled"
              ? "Nothing scheduled yet. Choose a version under To review."
              : "Nothing published yet."}
        </EmptyState>
      ) : (
        <div className="space-y-8">
          {shown.map(({ slot, posts: options }) => {
            const chosen = options.find((p) => ["approved", "publishing", "published"].includes(p.status));
            const list = tab === "review" ? options.filter((p) => p.status === "draft") : chosen ? [chosen] : [];
            return (
              <section key={slot.id} id={`slot-${slot.id}`} className="scroll-mt-6">
                <div className="flex flex-wrap items-baseline gap-x-3 gap-y-1 mb-3">
                  <h2 className="font-semibold">{format(parseISO(slot.scheduled_for), "EEE MMM d · HH:mm")}</h2>
                  <span className="text-sm text-gray-500">
                    {slot.pillar} · {PLATFORM[slot.platform] ?? slot.platform} {slot.handle}
                  </span>
                </div>
                <div className={tab === "review" ? "grid gap-4 lg:grid-cols-3" : "grid gap-4"}>
                  {list.map((post, i) => (
                    <article key={post.id} className="bg-white p-5 border rounded-2xl shadow-sm flex flex-col">
                      {tab === "review" && (
                        <div className="text-xs font-medium text-gray-400 mb-3">Option {i + 1}</div>
                      )}
                      {tab !== "review" && (
                        <div className="flex items-center gap-1.5 text-xs font-medium text-emerald-700 mb-3">
                          <Check className="w-3.5 h-3.5" /> {tab === "published" ? "Published" : "Chosen"}
                        </div>
                      )}
                      <div className="flex-1">
                        <Text post={post} />
                      </div>
                      {tab === "review" && (
                        <div className="flex gap-2 mt-5">
                          <button
                            disabled={acting !== null}
                            onClick={() => act(post.id, "approve")}
                            className="flex-1 bg-black text-white px-3 py-2 rounded-lg text-sm font-medium disabled:opacity-40"
                          >
                            Use this one
                          </button>
                          <button
                            disabled={acting !== null}
                            onClick={() => act(post.id, "reject")}
                            className="bg-gray-100 text-gray-700 px-3 py-2 rounded-lg text-sm font-medium disabled:opacity-40"
                          >
                            Discard
                          </button>
                        </div>
                      )}
                      {tab === "published" && post.external_url && (
                        <a href={post.external_url} target="_blank" rel="noreferrer" className="text-sm text-blue-600 mt-4">
                          View post
                        </a>
                      )}
                    </article>
                  ))}
                </div>
              </section>
            );
          })}
        </div>
      )}
    </div>
  );
}

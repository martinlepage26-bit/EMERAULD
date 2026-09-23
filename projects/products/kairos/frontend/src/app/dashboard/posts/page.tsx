"use client";

import { useEffect, useState } from "react";
import { FileText } from "lucide-react";
import { authedFetch } from "@/lib/api";
import { EmptyState, LoadError, Loading } from "@/components/LoadState";

interface Post {
  id: string;
  hook: string | null;
  body: string;
  status: string;
  variant: number;
  platform: string;
  created_at: string;
}

// Mirrors the post statuses in migrations/0001_init.sql.
const TABS = [
  { label: "Pending Review", status: "draft" },
  { label: "Published History", status: "published" },
] as const;

type Tab = (typeof TABS)[number];

export default function PostsPage() {
  const [tab, setTab] = useState<Tab>(TABS[0]);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-8">Posts &amp; Drafts</h1>

      <div className="flex gap-4 border-b mb-8">
        {TABS.map((t) => (
          <button
            key={t.status}
            onClick={() => setTab(t)}
            className={
              t.status === tab.status
                ? "pb-2 border-b-2 border-black font-medium"
                : "pb-2 text-gray-500 hover:text-black"
            }
          >
            {t.label}
          </button>
        ))}
      </div>

      {/* Keyed so a tab switch remounts with fresh state rather than resetting
          it from an effect, which would cascade an extra render. */}
      <PostList key={tab.status} status={tab.status} />
    </div>
  );
}

function PostList({ status }: { status: string }) {
  const [posts, setPosts] = useState<Post[] | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [acting, setActing] = useState<string | null>(null);

  useEffect(() => {
    authedFetch<{ posts: Post[] }>(`/v1/posts?status=${encodeURIComponent(status)}`)
      .then((r) => setPosts(r.posts ?? []))
      .catch(setError);
  }, [status]);

  const act = async (id: string, action: "approve" | "reject") => {
    setActing(id);
    try {
      await authedFetch(`/v1/posts/${id}/${action}`, { method: "POST" });
      // Drop it locally rather than refetching: the list it belonged to no
      // longer contains it either way.
      setPosts((current) => (current ?? []).filter((p) => p.id !== id));
    } catch (err) {
      setError(err as Error);
    }
    setActing(null);
  };

  if (error) return <LoadError error={error} />;
  if (posts === null) return <Loading />;

  if (posts.length === 0) {
    return (
      <EmptyState icon={<FileText className="w-8 h-8" />}>
        {status === "draft"
          ? "No drafts pending review right now. The drafting loop will generate more soon."
          : "Nothing published yet."}
      </EmptyState>
    );
  }

  return (
    <div className="space-y-4">
      {posts.map((post) => (
        <div key={post.id} className="bg-white p-6 border rounded-2xl shadow-sm">
          <div className="flex justify-between items-center mb-4">
            <span className="text-sm font-medium text-blue-600 bg-blue-50 px-2 py-1 rounded capitalize">
              {post.status}
            </span>
            <span className="text-xs text-gray-400">
              {post.platform} · variant {post.variant}
            </span>
          </div>

          {post.hook && <p className="font-medium text-gray-900 mb-2">{post.hook}</p>}
          <p className="text-gray-900 mb-6 font-serif whitespace-pre-wrap">{post.body}</p>

          {status === "draft" && (
            <div className="flex gap-3">
              <button
                disabled={acting === post.id}
                onClick={() => act(post.id, "approve")}
                className="bg-black text-white px-4 py-2 rounded-lg text-sm font-medium disabled:opacity-40"
              >
                Approve &amp; Queue
              </button>
              <button
                disabled={acting === post.id}
                onClick={() => act(post.id, "reject")}
                className="bg-gray-100 text-gray-700 px-4 py-2 rounded-lg text-sm font-medium disabled:opacity-40"
              >
                Reject
              </button>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

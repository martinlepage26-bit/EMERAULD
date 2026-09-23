"use client";

import { AlertCircle } from "lucide-react";
import { ApiError } from "@/lib/api";

/**
 * Every dashboard page previously swallowed fetch failures into console.error
 * and rendered its empty state, so a broken API looked exactly like an account
 * with no data. These separate the two.
 */
export function LoadError({ error }: { error: Error }) {
  const message =
    error instanceof ApiError && error.status === 401
      ? "Your API key was rejected. Disconnect and reconnect with a current key."
      : error instanceof ApiError
        ? error.message
        : "Could not reach the API.";

  return (
    <div
      role="alert"
      className="bg-red-50 border border-red-200 text-red-800 rounded-2xl p-6 flex gap-3 items-start"
    >
      <AlertCircle className="w-5 h-5 shrink-0 mt-0.5" />
      <div>
        <p className="font-medium mb-1">This did not load</p>
        <p className="text-sm">{message}</p>
      </div>
    </div>
  );
}

export function EmptyState({ icon, children }: { icon: React.ReactNode; children: React.ReactNode }) {
  return (
    <div className="bg-white border border-dashed rounded-2xl p-12 text-center text-gray-500 flex flex-col items-center">
      <div className="mb-4 text-gray-300">{icon}</div>
      <p>{children}</p>
    </div>
  );
}

export function Loading() {
  return <div className="text-sm text-gray-500">Loading…</div>;
}

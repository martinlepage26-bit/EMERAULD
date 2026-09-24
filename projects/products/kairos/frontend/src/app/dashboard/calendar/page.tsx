"use client";

import { useEffect, useState } from "react";
import { format, addDays, isSameDay, parseISO } from "date-fns";
import { authedFetch } from "@/lib/api";
import { LoadError, Loading } from "@/components/LoadState";

interface Slot {
  id: string;
  scheduled_for: string;
  status: string;
  platform: string;
  handle: string;
  pillar: string;
  post_id: string | null;
  hook: string | null;
  post_status: string | null;
}

// Mirrors the slot statuses in migrations/0001_init.sql.
const STATUS_STYLES: Record<string, string> = {
  planned: "bg-gray-50 text-gray-600 border-gray-200",
  drafting: "bg-gray-50 text-gray-600 border-gray-200",
  ready: "bg-blue-50 text-blue-700 border-blue-200",
  approved: "bg-emerald-50 text-emerald-700 border-emerald-200",
  publishing: "bg-emerald-50 text-emerald-700 border-emerald-200",
  published: "bg-green-50 text-green-700 border-green-200",
  failed: "bg-red-50 text-red-700 border-red-200",
  skipped: "bg-gray-50 text-gray-400 border-gray-200 line-through",
};

export default function CalendarPage() {
  const [slots, setSlots] = useState<Slot[] | null>(null);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    authedFetch<{ slots: Slot[] }>("/v1/calendar")
      .then((r) => setSlots(r.slots ?? []))
      .catch(setError);
  }, []);

  const today = new Date();
  const days = Array.from({ length: 14 }).map((_, i) => addDays(today, i));

  return (
    <div>
      <h1 className="text-2xl sm:text-3xl font-bold mb-2">Content calendar</h1>
      <p className="text-gray-500 mb-8">
        The next 14 days, planned across your topics. Topics that perform get more room.
      </p>

      {error ? (
        <LoadError error={error} />
      ) : slots === null ? (
        <Loading />
      ) : (
        <>
          <div className="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-3">
            {days.map((day) => {
              // Slot times are ISO strings from the API; compare by local day.
              const forDay = slots.filter((s) => isSameDay(parseISO(s.scheduled_for), day));
              return (
                <div key={day.toISOString()} className="bg-white border rounded-xl p-4 min-h-[120px]">
                  <div className="text-sm font-medium text-gray-400 mb-2">{format(day, "MMM d")}</div>
                  <div className="space-y-1">
                    {forDay.map((slot) => (
                      <div
                        key={slot.id}
                        title={slot.hook ?? `${slot.pillar} · ${slot.handle}`}
                        className={`text-xs border px-2 py-1 rounded truncate ${
                          STATUS_STYLES[slot.status] ?? STATUS_STYLES.planned
                        }`}
                      >
                        <span className="font-medium">{format(parseISO(slot.scheduled_for), "HH:mm")}</span>{" "}
                        {slot.hook ?? slot.pillar}
                      </div>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>

          {slots.length === 0 && (
            <p className="text-sm text-gray-500 mt-6">
              Nothing planned yet. The planner runs daily at 05:10 UTC, and connecting your first
              channel triggers it immediately.
            </p>
          )}
        </>
      )}
    </div>
  );
}

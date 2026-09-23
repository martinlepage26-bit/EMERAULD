"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { LayoutDashboard, Calendar, Inbox, FileText, BarChart, LogOut } from "lucide-react";
import { clearKey, storeKey, storedKey, verifyKey } from "@/lib/api";

/**
 * The key lives only in this browser's localStorage. It is never read from a
 * build-time variable, because anything prefixed `NEXT_PUBLIC_` is inlined into
 * the client bundle and would ship a working key to every visitor.
 */
type Gate =
  | { state: "checking" }
  | { state: "locked"; error?: string }
  | { state: "open" };

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const [gate, setGate] = useState<Gate>({ state: "checking" });

  useEffect(() => {
    // localStorage is unreachable during prerender, so the gate resolves on the
    // client. A stored key can also be revoked server-side, so it is checked on
    // every mount rather than trusted because it is present. Both branches
    // settle in a callback, never synchronously in the effect body.
    const stored = storedKey();
    const check = stored ? verifyKey(stored) : Promise.resolve(false);

    check.then((ok) => {
      if (ok) {
        setGate({ state: "open" });
        return;
      }
      if (stored) {
        clearKey();
        setGate({ state: "locked", error: "That key is no longer valid. Enter a current one." });
      } else {
        setGate({ state: "locked" });
      }
    });
  }, []);

  const disconnect = () => {
    clearKey();
    setGate({ state: "locked" });
  };

  if (gate.state === "checking") {
    return (
      <div className="flex h-screen items-center justify-center bg-gray-50 text-sm text-gray-500">
        Checking your key…
      </div>
    );
  }

  if (gate.state === "locked") {
    return <KeyGate error={gate.error} onUnlocked={() => setGate({ state: "open" })} />;
  }

  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r flex flex-col">
        <div className="p-6">
          <div className="flex items-center gap-2 mb-8">
            <div className="w-8 h-8 bg-black rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-xl leading-none">K</span>
            </div>
            <span className="text-xl font-semibold tracking-tight">Kairos</span>
          </div>
          <nav className="space-y-2 text-sm font-medium">
            <NavItem href="/dashboard" icon={<LayoutDashboard className="w-4 h-4" />} label="Overview" />
            <NavItem href="/dashboard/calendar" icon={<Calendar className="w-4 h-4" />} label="Calendar" />
            <NavItem href="/dashboard/posts" icon={<FileText className="w-4 h-4" />} label="Posts & Drafts" />
            <NavItem href="/dashboard/inbox" icon={<Inbox className="w-4 h-4" />} label="Inbox" />
            <NavItem href="/dashboard/insights" icon={<BarChart className="w-4 h-4" />} label="Insights" />
          </nav>
        </div>
        <div className="mt-auto p-6 border-t">
          <button
            onClick={disconnect}
            className="flex items-center gap-2 text-xs text-gray-500 hover:text-gray-900 transition-colors"
          >
            <LogOut className="w-3.5 h-3.5" /> Disconnect this browser
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-auto">
        <div className="p-8 max-w-6xl mx-auto">{children}</div>
      </main>
    </div>
  );
}

function KeyGate({ error, onUnlocked }: { error?: string; onUnlocked: () => void }) {
  const [value, setValue] = useState("");
  const [checking, setChecking] = useState(false);
  const [message, setMessage] = useState(error);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    const key = value.trim();
    if (!key) return;

    setChecking(true);
    setMessage(undefined);
    const ok = await verifyKey(key);
    setChecking(false);

    if (!ok) {
      setMessage("That key was rejected. Check it and try again.");
      return;
    }
    storeKey(key);
    onUnlocked();
  };

  return (
    <div className="flex h-screen items-center justify-center bg-gray-50">
      <form onSubmit={submit} className="w-full max-w-sm bg-white border rounded-2xl shadow-sm p-8">
        <div className="flex items-center gap-2 mb-6">
          <div className="w-8 h-8 bg-black rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-xl leading-none">K</span>
          </div>
          <span className="text-xl font-semibold tracking-tight">Kairos</span>
        </div>

        <h1 className="text-lg font-semibold mb-1">Connect this browser</h1>
        <p className="text-sm text-gray-500 mb-6">
          Paste the API key you were given when the account was created. It is stored in this
          browser only.
        </p>

        <input
          type="password"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder="kai_sk_…"
          autoComplete="off"
          autoFocus
          className="w-full border rounded-lg px-4 py-2 mb-3"
        />

        {message && <p className="text-sm text-red-600 mb-3">{message}</p>}

        <button
          type="submit"
          disabled={checking || !value.trim()}
          className="w-full bg-black text-white px-4 py-2 rounded-lg font-medium disabled:opacity-40"
        >
          {checking ? "Checking…" : "Connect"}
        </button>
      </form>
    </div>
  );
}

function NavItem({ href, icon, label }: { href: string; icon: React.ReactNode; label: string }) {
  return (
    <Link
      href={href}
      className="flex items-center gap-3 px-3 py-2 text-gray-700 rounded-lg hover:bg-gray-100 transition-colors"
    >
      {icon} {label}
    </Link>
  );
}

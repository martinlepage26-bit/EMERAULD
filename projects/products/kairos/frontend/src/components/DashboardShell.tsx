"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { LayoutDashboard, Calendar, Inbox, FileText, BarChart, LogOut } from "lucide-react";
import { clearKey, devDemoSession, getPublicConfig, storeKey, storedKey, verifyKey } from "@/lib/api";

/**
 * The key lives only in this browser's localStorage. It is never read from a
 * build-time variable, because anything prefixed `NEXT_PUBLIC_` is inlined into
 * the client bundle and would ship a working key to every visitor.
 */
type Gate =
  | { state: "checking" }
  | { state: "locked"; error?: string }
  | { state: "open" };

export function DashboardShell({ children }: { children: React.ReactNode }) {
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
        setGate({ state: "locked", error: "You've been signed out. Enter your access key to continue." });
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
        Signing you in…
      </div>
    );
  }

  if (gate.state === "locked") {
    return <KeyGate error={gate.error} onUnlocked={() => setGate({ state: "open" })} />;
  }

  return (
    <div className="flex flex-col md:flex-row h-screen bg-gray-50">
      {/* Phone: a top bar with scrollable navigation instead of the sidebar. */}
      <header className="md:hidden bg-white border-b">
        <div className="flex items-center justify-between px-4 py-3">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 bg-black rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-lg leading-none">K</span>
            </div>
            <span className="text-lg font-semibold tracking-tight">Kairos</span>
          </div>
          <button onClick={disconnect} className="text-xs text-gray-500 hover:text-gray-900">
            Sign out
          </button>
        </div>
        <nav className="flex gap-1 overflow-x-auto px-2 pb-2 text-sm font-medium">
          {NAV.map((n) => (
            <Link key={n.href} href={n.href} className="shrink-0 px-3 py-1.5 rounded-lg text-gray-700 hover:bg-gray-100">
              {n.label}
            </Link>
          ))}
        </nav>
      </header>

      {/* Sidebar */}
      <aside className="hidden md:flex w-64 bg-white border-r flex-col">
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
            <NavItem href="/dashboard/posts" icon={<FileText className="w-4 h-4" />} label="Posts" />
            <NavItem href="/dashboard/inbox" icon={<Inbox className="w-4 h-4" />} label="Inbox" />
            <NavItem href="/dashboard/insights" icon={<BarChart className="w-4 h-4" />} label="Results" />
          </nav>
        </div>
        <div className="mt-auto p-6 border-t">
          <button
            onClick={disconnect}
            className="flex items-center gap-2 text-xs text-gray-500 hover:text-gray-900 transition-colors"
          >
            <LogOut className="w-3.5 h-3.5" /> Sign out
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-auto">
        <div className="p-4 sm:p-8 max-w-6xl mx-auto">{children}</div>
      </main>
    </div>
  );
}

function KeyGate({ error, onUnlocked }: { error?: string; onUnlocked: () => void }) {
  const [value, setValue] = useState("");
  const [checking, setChecking] = useState(false);
  const [message, setMessage] = useState(error);
  const [devDemo, setDevDemo] = useState(false);

  useEffect(() => {
    getPublicConfig().then((c) => setDevDemo(c.devDemoLogin));
  }, []);

  const useDemo = async () => {
    setChecking(true);
    setMessage(undefined);
    try {
      storeKey(await devDemoSession());
      onUnlocked();
    } catch {
      setMessage("The demo account isn't available on this server.");
    }
    setChecking(false);
  };

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    const key = value.trim();
    if (!key) return;

    setChecking(true);
    setMessage(undefined);
    const ok = await verifyKey(key);
    setChecking(false);

    if (!ok) {
      setMessage("That access key wasn't recognised. Check it and try again.");
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

        <h1 className="text-lg font-semibold mb-1">Sign in</h1>
        <p className="text-sm text-gray-500 mb-6">
          Enter the access key from your welcome email. You&apos;ll stay signed in on this browser
          until you sign out.
        </p>

        <input
          type="password"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          placeholder="Access key"
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
          {checking ? "Checking…" : "Sign in"}
        </button>

        {devDemo && (
          <button
            type="button"
            onClick={useDemo}
            disabled={checking}
            className="w-full mt-3 border border-dashed border-amber-400 text-amber-700 bg-amber-50 px-4 py-2 rounded-lg text-sm font-medium disabled:opacity-40"
          >
            Use demo account (dev only)
          </button>
        )}
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

const NAV = [
  { href: "/dashboard", label: "Overview" },
  { href: "/dashboard/calendar", label: "Calendar" },
  { href: "/dashboard/posts", label: "Posts" },
  { href: "/dashboard/inbox", label: "Inbox" },
  { href: "/dashboard/insights", label: "Results" },
];

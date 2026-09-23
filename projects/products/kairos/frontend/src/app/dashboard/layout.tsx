"use client";

import Link from "next/link";
import { useEffect } from "react";
import { LayoutDashboard, Calendar, Inbox, FileText, BarChart } from "lucide-react";

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    if (!localStorage.getItem("kairos_api_key")) {
      const adminKey = process.env.NEXT_PUBLIC_ADMIN_API_KEY;
      if (adminKey) localStorage.setItem("kairos_api_key", adminKey);
    }
  }, []);

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
        <div className="mt-auto p-6 border-t text-xs text-gray-400">
          Admin Bypass Enabled
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-auto">
        <div className="p-8 max-w-6xl mx-auto">
          {children}
        </div>
      </main>
    </div>
  );
}

function NavItem({ href, icon, label }: { href: string; icon: React.ReactNode; label: string }) {
  return (
    <Link href={href} className="flex items-center gap-3 px-3 py-2 text-gray-700 rounded-lg hover:bg-gray-100 transition-colors">
      {icon} {label}
    </Link>
  );
}

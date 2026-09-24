import type { Metadata } from "next";
import { DashboardShell } from "@/components/DashboardShell";

// A Server Component purely so it can export metadata: the shell itself gates
// on a key held in localStorage, which only exists in the browser.
//
// The template is repeated here rather than inherited: `title.template` applies
// only to the segment directly below the one that defines it, so without this
// the nested routes would render a bare "Calendar" with no product name.
export const metadata: Metadata = {
  title: {
    default: "Overview",
    template: "%s · Kairos",
  },
};

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  return <DashboardShell>{children}</DashboardShell>;
}

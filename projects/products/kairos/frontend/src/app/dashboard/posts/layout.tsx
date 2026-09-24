import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Posts & Drafts",
};

export default function Layout({ children }: { children: React.ReactNode }) {
  return children;
}

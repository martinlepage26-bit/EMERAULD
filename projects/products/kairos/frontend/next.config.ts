import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // The dashboard is entirely client components fetching the Worker API at
  // runtime, so there is nothing for a Next server to do. A static export
  // deploys to Cloudflare Pages as plain assets.
  output: "export",

  // Pages serves /dashboard from dashboard/index.html; without this the export
  // emits dashboard.html and nested routes resolve inconsistently.
  trailingSlash: true,

  images: { unoptimized: true },
};

export default nextConfig;

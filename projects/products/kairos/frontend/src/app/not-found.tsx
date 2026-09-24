import Link from "next/link";

export const metadata = { title: "Page not found" };

export default function NotFound() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-50 px-6">
      <div className="max-w-sm text-center">
        <div className="w-10 h-10 bg-black rounded-lg flex items-center justify-center mx-auto mb-6">
          <span className="text-white font-bold text-2xl leading-none">K</span>
        </div>
        <h1 className="text-2xl font-semibold mb-2">This page doesn&apos;t exist</h1>
        <p className="text-gray-500 mb-8">The link may be out of date, or the address mistyped.</p>
        <div className="flex gap-3 justify-center">
          <Link href="/" className="px-4 py-2 rounded-lg bg-black text-white text-sm font-medium hover:bg-gray-800">
            Home
          </Link>
          <Link href="/dashboard" className="px-4 py-2 rounded-lg bg-white border text-sm font-medium hover:bg-gray-100">
            Dashboard
          </Link>
        </div>
      </div>
    </main>
  );
}

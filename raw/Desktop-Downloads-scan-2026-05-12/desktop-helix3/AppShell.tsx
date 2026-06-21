import { type ReactNode } from "react";
import { useApp } from "../context";
import type { Route } from "../types";

interface NavItem {
  id: Route;
  label: string;
  icon: string;
  sub?: string;
  alert?: boolean;
}

const NAV: NavItem[] = [
  { id: "dashboard",    label: "Dashboard",        icon: "⬡", sub: "Compliance overview" },
  { id: "policy-engine",label: "Policy Engine",    icon: "◈", sub: "L1 · L2 · L3 hierarchy" },
  { id: "helix-probe",  label: "HELIX Probe",      icon: "⟳", sub: "AI stress-testing" },
  { id: "audit-log",    label: "Audit Log",         icon: "▦", sub: "Immutable traces" },
  { id: "law25",        label: "Law 25 Centre",     icon: "⚖", sub: "Quebec compliance", alert: true },
];

export function AppShell({ children }: { children: ReactNode }) {
  const { state, dispatch } = useApp();

  const pendingHITL = state.hitlQueue.filter(
    (h) => h.status === "PENDING" || h.status === "ESCALATED"
  ).length;

  const overallScore = state.systems.length === 0
    ? 0
    : Math.round(
        state.systems.reduce((a, s) => a + s.complianceScore, 0) / state.systems.length
      );

  return (
    <div style={{ display: "flex", height: "100vh", overflow: "hidden" }}>
      {/* ── Sidebar ── */}
      <aside style={{
        width: "var(--sidebar)",
        flexShrink: 0,
        background: "var(--deep)",
        borderRight: "1px solid var(--border)",
        display: "flex",
        flexDirection: "column",
        overflow: "hidden",
      }}>
        {/* Logo */}
        <div style={{
          padding: "20px 16px 16px",
          borderBottom: "1px solid var(--border)",
        }}>
          <div style={{
            fontFamily: "'Syne', sans-serif",
            fontSize: 15,
            fontWeight: 800,
            letterSpacing: "0.15em",
            color: "var(--gold)",
            lineHeight: 1,
          }}>
            HELIX
          </div>
          <div style={{
            fontFamily: "'IBM Plex Mono', monospace",
            fontSize: 9,
            fontWeight: 500,
            letterSpacing: "0.12em",
            textTransform: "uppercase",
            color: "var(--text-ghost)",
            marginTop: 4,
          }}>
            Governance Platform v2.6
          </div>
        </div>

        {/* Compliance pulse */}
        <div style={{
          margin: "12px 12px 0",
          padding: "10px 12px",
          background: "var(--surface)",
          border: "1px solid var(--border)",
          borderRadius: "var(--radius)",
        }}>
          <div style={{
            fontFamily: "'IBM Plex Mono', monospace",
            fontSize: 9,
            fontWeight: 600,
            letterSpacing: "0.1em",
            textTransform: "uppercase",
            color: "var(--text-dim)",
            marginBottom: 6,
          }}>
            Law 25 Health
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
            <div style={{
              fontFamily: "'Syne', sans-serif",
              fontSize: 22,
              fontWeight: 800,
              color: overallScore >= 80 ? "var(--green)" : overallScore >= 60 ? "var(--amber)" : "var(--red)",
            }}>
              {overallScore}%
            </div>
            <div style={{ flex: 1 }}>
              <div className="progress-track">
                <div
                  className="progress-fill"
                  style={{
                    width: `${overallScore}%`,
                    background: overallScore >= 80 ? "var(--green)" : overallScore >= 60 ? "var(--amber)" : "var(--red)",
                  }}
                />
              </div>
            </div>
          </div>
        </div>

        {/* Nav */}
        <nav style={{ flex: 1, padding: "8px 0", overflowY: "auto" }}>
          {NAV.map((item) => {
            const isActive = state.route === item.id;
            const showAlert = item.id === "law25" && pendingHITL > 0;

            return (
              <button
                key={item.id}
                onClick={() => dispatch({ type: "NAVIGATE", route: item.id })}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 10,
                  width: "100%",
                  padding: "9px 16px",
                  background: isActive ? "var(--overlay)" : "transparent",
                  border: "none",
                  borderLeft: `2px solid ${isActive ? "var(--gold)" : "transparent"}`,
                  cursor: "pointer",
                  textAlign: "left",
                  transition: "all 0.12s",
                  color: isActive ? "var(--text)" : "var(--text-dim)",
                }}
                onMouseEnter={(e) => {
                  if (!isActive) (e.currentTarget as HTMLButtonElement).style.background = "rgba(255,255,255,0.03)";
                }}
                onMouseLeave={(e) => {
                  if (!isActive) (e.currentTarget as HTMLButtonElement).style.background = "transparent";
                }}
              >
                <span style={{
                  fontSize: 14,
                  color: isActive ? "var(--gold)" : "var(--text-ghost)",
                  flexShrink: 0,
                }}>
                  {item.icon}
                </span>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div style={{
                    fontSize: 12,
                    fontWeight: isActive ? 600 : 400,
                    fontFamily: "'IBM Plex Sans', sans-serif",
                    lineHeight: 1.2,
                  }}>
                    {item.label}
                  </div>
                  {item.sub && (
                    <div style={{
                      fontSize: 9,
                      fontFamily: "'IBM Plex Mono', monospace",
                      color: "var(--text-ghost)",
                      letterSpacing: "0.05em",
                      marginTop: 1,
                    }}>
                      {item.sub}
                    </div>
                  )}
                </div>
                {showAlert && (
                  <span style={{
                    background: "var(--red)",
                    color: "#fff",
                    fontFamily: "'IBM Plex Mono', monospace",
                    fontSize: 9,
                    fontWeight: 700,
                    padding: "1px 5px",
                    borderRadius: 10,
                    flexShrink: 0,
                  }}>
                    {pendingHITL}
                  </span>
                )}
              </button>
            );
          })}
        </nav>

        {/* Footer */}
        <div style={{
          padding: "12px 16px",
          borderTop: "1px solid var(--border)",
          fontFamily: "'IBM Plex Mono', monospace",
          fontSize: 9,
          color: "var(--text-ghost)",
          letterSpacing: "0.06em",
        }}>
          <div>RECURSION INVARIANT</div>
          <div style={{ marginTop: 3, lineHeight: 1.5, opacity: 0.6, fontSize: 8 }}>
            Inclusion gives recursion material;<br />
            recursion gives inclusion motion;<br />
            governance prevents the loop.
          </div>
        </div>
      </aside>

      {/* ── Main ── */}
      <main style={{
        flex: 1,
        overflow: "hidden",
        display: "flex",
        flexDirection: "column",
        background: "var(--void)",
      }}>
        {/* Top bar */}
        <header style={{
          height: "var(--topbar)",
          flexShrink: 0,
          borderBottom: "1px solid var(--border)",
          display: "flex",
          alignItems: "center",
          padding: "0 24px",
          gap: 16,
          background: "var(--deep)",
        }}>
          <div style={{
            fontFamily: "'IBM Plex Mono', monospace",
            fontSize: 10,
            fontWeight: 600,
            letterSpacing: "0.12em",
            textTransform: "uppercase",
            color: "var(--text-dim)",
          }}>
            {NAV.find((n) => n.id === state.route)?.label}
          </div>

          <div style={{ flex: 1 }} />

          {/* System status pills */}
          <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
            {state.systems.slice(0, 3).map((sys) => (
              <div
                key={sys.id}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 5,
                  padding: "3px 8px",
                  background: "var(--surface)",
                  border: "1px solid var(--border)",
                  borderRadius: "var(--radius)",
                }}
              >
                <span
                  className={`dot ${sys.status === "ACTIVE" ? "dot-green" : sys.status === "PAUSED" ? "dot-amber" : "dot-dim"}`}
                  style={{ width: 6, height: 6 }}
                />
                <span style={{
                  fontFamily: "'IBM Plex Mono', monospace",
                  fontSize: 9,
                  color: "var(--text-dim)",
                  letterSpacing: "0.05em",
                }}>
                  {sys.name.split(" ")[0]}
                </span>
              </div>
            ))}
          </div>

          <div style={{
            fontFamily: "'IBM Plex Mono', monospace",
            fontSize: 9,
            color: "var(--text-ghost)",
            letterSpacing: "0.06em",
          }}>
            {new Date().toLocaleString("en-CA", {
              month: "short", day: "2-digit",
              hour: "2-digit", minute: "2-digit",
            })}
          </div>
        </header>

        {/* Page content */}
        <div style={{ flex: 1, overflow: "auto" }}>
          {children}
        </div>
      </main>
    </div>
  );
}
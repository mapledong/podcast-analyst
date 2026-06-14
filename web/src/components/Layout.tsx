import { Link, Outlet } from "react-router-dom";
import ThemeToggle from "./ThemeToggle";

export default function Layout() {
  return (
    <div className="app-shell">
      <header className="site-header">
        <Link to="/" className="brand">
          <span className="brand-mark" aria-hidden />
          <span>
            <strong>Podcast Analyst</strong>
            <small>Summary Library</small>
          </span>
        </Link>
        <ThemeToggle />
      </header>
      <main className="site-main">
        <Outlet />
      </main>
      <footer className="site-footer">
        <p className="footer-disclaimer">
          Not investment advice. Summaries are for personal research and education only; verify
          facts and consult a qualified advisor before acting. Not affiliated with or endorsed by
          any podcast or guest.
        </p>
      </footer>
    </div>
  );
}

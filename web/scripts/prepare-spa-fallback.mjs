import { copyFileSync, existsSync } from "node:fs";
import { resolve } from "node:path";

const dist = resolve(process.cwd(), "dist");
const index = resolve(dist, "index.html");
const fallback = resolve(dist, "404.html");

if (!existsSync(index)) {
  throw new Error("dist/index.html not found. Run vite build before preparing fallback.");
}

copyFileSync(index, fallback);
console.log("Prepared SPA fallback: dist/404.html");

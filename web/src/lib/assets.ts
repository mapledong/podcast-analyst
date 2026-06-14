/** Resolve a public asset path for GitHub Pages subpath deploy (BASE_URL). */
export function assetUrl(relativePath: string): string {
  const base = import.meta.env.BASE_URL || "/";
  const path = relativePath.replace(/^\//, "");
  return `${base}${path}`;
}

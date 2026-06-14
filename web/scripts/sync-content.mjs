#!/usr/bin/env node
/**
 * Sync podcast catalog, episode metadata, markdown summaries, and cover art from Apple Podcasts.
 */
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import yaml from "yaml";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "../..");
const OUT = path.resolve(__dirname, "../src/data");
const SUMMARIES_OUT = path.join(OUT, "summaries");
const COVERS_OUT = path.resolve(__dirname, "../public/covers");

const PODCAST_SLUG = {
  "Invest Like the Best": "invest-like-the-best",
  Acquired: "acquired",
  Founders: "founders",
  "Business Breakdowns": "business-breakdowns",
};

function readYaml(rel) {
  return yaml.parse(fs.readFileSync(path.join(ROOT, rel), "utf8"));
}

function readJson(rel) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, rel), "utf8"));
}

function estimateReadMinutes(markdown) {
  const words = markdown.split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(words / 200));
}

async function fetchAppleCover(applePodcastId, podcastId) {
  fs.mkdirSync(COVERS_OUT, { recursive: true });
  const localFile = `${podcastId}.jpg`;
  const localPath = path.join(COVERS_OUT, localFile);

  const useCached = () => {
    if (fs.existsSync(localPath) && fs.statSync(localPath).size > 500) {
      return `/covers/${localFile}`;
    }
    return null;
  };

  try {
    const lookup = await fetch(
      `https://itunes.apple.com/lookup?id=${applePodcastId}&entity=podcast`,
    );
    if (!lookup.ok) throw new Error(`lookup HTTP ${lookup.status}`);
    const data = await lookup.json();
    const artwork = data.results?.[0]?.artworkUrl600;
    if (!artwork) throw new Error("no artwork in iTunes response");

    const imgRes = await fetch(artwork);
    if (!imgRes.ok) throw new Error(`artwork HTTP ${imgRes.status}`);
    const buf = Buffer.from(await imgRes.arrayBuffer());
    if (buf.length < 500) throw new Error("artwork too small");
    fs.writeFileSync(localPath, buf);
    console.log(`Cover saved: ${localFile} (${data.results[0].collectionName})`);
    return `/covers/${localFile}`;
  } catch (err) {
    const cached = useCached();
    if (cached) {
      console.warn(`Cover fetch failed for ${podcastId}, using cached JPG`);
      return cached;
    }
    console.warn(`Cover fetch failed for ${podcastId}: ${err.message}`);
    throw err;
  }
}

import { resolveDisplayTitles } from "./displayTitles.mjs";

spawnSync("node", ["scripts/generate-tickers.mjs"], {
  cwd: path.resolve(__dirname, ".."),
  stdio: "inherit",
});

function stripTemplateFooter(markdown) {
  return markdown
    .replace(/\n---\n\n<p align="center"><sub>podcast-analyst[^<]*<\/sub><\/p>\s*$/i, "\n")
    .trimEnd();
}

fs.mkdirSync(SUMMARIES_OUT, { recursive: true });

const podcastsConfig = readYaml("config/podcasts.yaml");
const episodesConfig = readYaml("config/episodes.yaml");

const podcasts = await Promise.all(
  podcastsConfig.podcasts.map(async (p) => {
    let cover_url = `/covers/${p.id}.jpg`;
    if (p.apple_podcast_id) {
      try {
        cover_url = await fetchAppleCover(p.apple_podcast_id, p.id);
      } catch {
        const cached = path.join(COVERS_OUT, `${p.id}.jpg`);
        if (fs.existsSync(cached)) cover_url = `/covers/${p.id}.jpg`;
      }
    } else if (p.cover_url) {
      cover_url = p.cover_url;
    }
    const { apple_podcast_id: _a, cover_remote: _r, ...rest } = p;
    return { ...rest, cover_url, episodeCount: 0 };
  }),
);

const episodes = [];

for (const epCfg of episodesConfig.episodes || []) {
  const id = epCfg.id;
  const approvedPath = path.join(ROOT, "data/approved", `${id}.json`);
  const outputPath = path.join(ROOT, "outputs", `EP${epCfg.episode_number}_${id}.md`);

  if (!fs.existsSync(approvedPath) || !fs.existsSync(outputPath)) {
    console.warn(`Skipping ${id}: missing approved JSON or markdown output`);
    continue;
  }

  const approved = readJson(`data/approved/${id}.json`);
  let markdown = fs.readFileSync(outputPath, "utf8");
  markdown = stripTemplateFooter(markdown);

  const podcastName = epCfg.podcast || approved.podcast || episodesConfig.podcast;
  const podcastId = PODCAST_SLUG[podcastName] || podcasts[0]?.id;

  const summaryFile = `${id}.md`;
  fs.writeFileSync(path.join(SUMMARIES_OUT, summaryFile), markdown);

  const readMatch = markdown.match(/≈(\d+)\s*min/i);
  const readMinutes = readMatch ? parseInt(readMatch[1], 10) : estimateReadMinutes(markdown);

  const keywords = (approved.keywords || []).map((k) => String(k).trim()).filter(Boolean);
  const investmentIdeas = (approved.top_investment_implications || []).map((row) => ({
    ticker: String(row.ticker || "").trim(),
    direction: row.direction,
    confidence: row.confidence,
    thesis: String(row.thesis || "").trim(),
  }));

  const { displayTitle, displaySubtitle } = resolveDisplayTitles(
    podcastId,
    epCfg.title,
    epCfg.guest,
    epCfg.guest_role || approved.metadata?.guest_role || "",
  );

  episodes.push({
    id,
    podcastId,
    episodeNumber: epCfg.episode_number,
    title: epCfg.title,
    guest: epCfg.guest,
    displayTitle,
    displaySubtitle,
    guestRole: epCfg.guest_role || approved.metadata?.guest_role || "",
    date: epCfg.date,
    durationMinutes: epCfg.duration_minutes,
    readMinutes,
    rating: approved.episode_rating?.overall ?? null,
    conclusion: approved.conclusion || "",
    youtubeUrl: epCfg.youtube_url || approved.metadata?.youtube_url || "",
    summaryFile,
    keywords,
    investmentIdeas,
    chronologySubject: approved.chronology?.subject || "",
  });
}

for (const p of podcasts) {
  p.episodeCount = episodes.filter((e) => e.podcastId === p.id).length;
}

const catalog = {
  generatedAt: new Date().toISOString(),
  podcasts,
  episodes: episodes.sort((a, b) => {
    const dateSort = new Set(["acquired", "business-breakdowns"]);
    if (dateSort.has(a.podcastId) && dateSort.has(b.podcastId)) {
      return b.date.localeCompare(a.date);
    }
    if (dateSort.has(a.podcastId)) return b.date.localeCompare(a.date);
    if (dateSort.has(b.podcastId)) return b.date.localeCompare(a.date);
    return b.episodeNumber - a.episodeNumber;
  }),
};

fs.writeFileSync(path.join(OUT, "catalog.json"), JSON.stringify(catalog, null, 2));
console.log(`Synced ${episodes.length} episodes → ${OUT}`);

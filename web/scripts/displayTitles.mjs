/** @typedef {{ company: string, person?: string, role?: string, tagline?: string }} ParsedTitle */

const COMPANY_FIRST = new Set(["acquired", "business-breakdowns"]);
const ACQUIRED = new Set(["acquired"]);

const EDITORIAL_WORDS = /\b(who|that|from|lessons|saved|story|interview|special|sessions|playbook|dynamism|capital)\b/i;

const SEASON_EPISODE_PREFIX = /^(?:Acquired\s+)?Season\s+(\d+),?\s+Episode\s+(\d+):\s*(.+)$/i;
const EPISODE_NUMBER_COLON = /^Episode\s+(\d+):\s*(.+)$/i;
const EPISODE_NUMBER_SPACE = /^Episode\s+(\d+)\s+(.+)$/i;
const EDITORIAL_COLON_PREFIX = /^(Interview|Special|Sessions|Short|ACQ Sessions):\s*(.+)$/i;
const PERSON_ON_THEME = /^(.+?)\s+on\s+(.+)$/i;
const GENERIC_HEADLINE =
  /^(Interview|Special|Sessions|Short|Episode\s+\d+|Season\s+\d+(?:,\s*Episode\s+\d+)?|Acquired(?:\s+Season\s+\d+\s+Episode\s+\d+)?)$/i;

function norm(text) {
  return String(text || "")
    .trim()
    .replace(/\s+/g, " ");
}

function normKey(text) {
  return norm(text).toLowerCase();
}

function titlesRedundant(title, guest) {
  const t = normKey(title);
  const g = normKey(guest);
  if (!t || !g) return false;
  if (t === g) return true;
  if (g.length > 3 && t.includes(g)) return true;
  if (t.length > 3 && g.includes(t)) return true;
  return false;
}

/** @param {...string} parts */
function formatSubtitle(...parts) {
  const seen = new Set();
  const out = [];
  for (const raw of parts) {
    const p = norm(raw);
    if (!p) continue;
    const key = normKey(p);
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(p);
  }
  return out.join(" · ");
}

function isEntityLabel(text) {
  const t = norm(text);
  if (!t || t.length > 55) return false;
  if (t.split(/\s+/).length > 7) return false;
  if (EDITORIAL_WORDS.test(t)) return false;
  if (t.endsWith(")") || t.includes("(")) return false;
  return true;
}

function isEditorialTitle(text, subject = "") {
  const t = norm(text);
  if (!t) return false;
  if (subject && normKey(t) !== normKey(subject)) {
    if (t.length > subject.length + 8) return true;
    if (t.split(/\s+/).length >= 6) return true;
    if (EDITORIAL_WORDS.test(t)) return true;
  }
  return t.split(/\s+/).length >= 7 || EDITORIAL_WORDS.test(t);
}

function looksLikePersonName(text) {
  const t = norm(text);
  if (!t || !isEntityLabel(t)) return false;
  const words = t.split(/\s+/);
  if (words.length < 2 || words.length > 4) return false;
  if (/\d/.test(t)) return false;
  if (/\b(inc|corp|llc|ltd|group|systems|technologies|part|volume|season)\b/i.test(t)) return false;
  return words.every((w) => w[0] === w[0]?.toUpperCase());
}

function seriesTagline(title) {
  title = norm(title);
  let m = title.match(/^(.+?)\s+Part\s+([IVX\d]+)\s*:?\s*(.*)$/i);
  if (m) {
    const tail = norm(m[3]);
    const part = `Part ${m[2]}`;
    return tail ? `${part}: ${tail}` : part;
  }
  m = title.match(/^(.+?)\s+Volume\s+([IVX\d]+)\s*$/i);
  if (m) return `Volume ${m[2]}`;
  m = title.match(/^([^:]+):\s*(.+)$/);
  if (m) return norm(m[2]);
  return "";
}

function parseEpisodeFraming(title) {
  title = norm(title);
  let m = title.match(SEASON_EPISODE_PREFIX);
  if (m) return { subject: norm(m[3]), framing: `Season ${m[1]} · Episode ${m[2]}` };
  m = title.match(EPISODE_NUMBER_COLON);
  if (m) return { subject: norm(m[2]), framing: `Episode ${m[1]}` };
  m = title.match(EPISODE_NUMBER_SPACE);
  if (m) return { subject: norm(m[2]), framing: `Episode ${m[1]}` };
  m = title.match(EDITORIAL_COLON_PREFIX);
  if (m) return { subject: norm(m[2]), framing: "" };
  return { subject: title, framing: "" };
}

function mergeFraming(guestRole, framing) {
  if (!framing) return guestRole;
  if (guestRole && normKey(framing) && normKey(guestRole).includes(normKey(framing))) return guestRole;
  return formatSubtitle(guestRole, framing);
}

function headlineFromSubject(subject) {
  subject = norm(subject);
  let m = subject.match(/^(.+?)\s*\([^)]*?\bwith\s+(.+?)\)$/i);
  if (m) return { headline: m[1].trim(), tagline: m[2].trim() };
  m = subject.match(/^(.+?)\s+\(([^)]+)\)$/);
  if (m) {
    const left = m[1].trim();
    const right = m[2].trim();
    if (/^Part\s+/i.test(right)) return { headline: subject, tagline: "" };
    if (looksLikePersonName(left) || left.split(/\s+/).length <= 3) {
      return { headline: left, tagline: right };
    }
  }
  m = subject.match(PERSON_ON_THEME);
  if (m) {
    const left = m[1].trim();
    const right = m[2].trim();
    if (left.includes("&") || looksLikePersonName(left) || left.split(/\s+/).length <= 6) {
      return { headline: left, tagline: right };
    }
  }
  const headline = companyHeadline(subject);
  const tagline = seriesTagline(subject);
  if (tagline && normKey(tagline) !== normKey(headline)) {
    return { headline, tagline };
  }
  return { headline, tagline: "" };
}

function companyHeadline(title) {
  title = norm(title);
  const { subject } = parseEpisodeFraming(title);
  title = subject;
  let m = title.match(/^(.+?)\s+Part\s+([IVX\d]+)\s*:?\s*(.*)$/i);
  if (m) return m[1].trim();
  m = title.match(/^(.+?)\s+Volume\s+([IVX\d]+)\s*$/i);
  if (m) return m[1].trim();
  m = subject.match(/^(.+?)\s*\([^)]*?\bwith\s+(.+?)\)$/i);
  if (m) return m[1].trim();
  m = title.match(/^([^:]+):\s*(.+)$/);
  if (m) {
    const left = m[1].trim();
    const right = m[2].trim();
    if (GENERIC_HEADLINE.test(left) || isEditorialTitle(left)) return right;
    if (isEntityLabel(left)) return left;
    if (left.split(/\s+/).length <= 4) return left;
    return right;
  }
  return title;
}

/** @param {string} title @param {string} guest @param {string} guestRole */
function resolveAcquiredTitles(title, guest, guestRole) {
  title = norm(title);
  guest = norm(guest);
  guestRole = norm(guestRole);

  const { subject, framing } = parseEpisodeFraming(title);
  if (guest && normKey(guest) === normKey(title)) {
    guest = subject;
  }

  let m = subject.match(/^(.+?)\s+CEO\s+(.+)$/i);
  if (m) {
    const company = m[1].trim();
    const person = m[2].trim();
    return {
      displayTitle: company,
      displaySubtitle: formatSubtitle(person, "CEO", mergeFraming(guestRole, framing)),
      displayGuest: person,
      displayGuestRole: "CEO",
    };
  }

  m = subject.match(/^(.+?)\s*\([^)]*?\bwith\s+(.+?)\)$/i);
  if (m) {
    const company = m[1].trim();
    const person = m[2].trim();
    return {
      displayTitle: company,
      displaySubtitle: formatSubtitle(person, mergeFraming(guestRole, framing)),
      displayGuest: person,
      displayGuestRole: guestRole,
    };
  }

  m = subject.match(/^The\s+(.+?)\s+Interview$/i);
  if (m) {
    const person = m[1].trim();
    return {
      displayTitle: person,
      displaySubtitle: formatSubtitle("Interview", mergeFraming(guestRole, framing)),
      displayGuest: person,
      displayGuestRole: guestRole,
    };
  }

  m = subject.match(/^(.+?)\s+with\s+(.+)$/i);
  if (m) {
    const company = m[1].trim();
    const person = m[2].trim();
    return {
      displayTitle: company,
      displaySubtitle: formatSubtitle(person, mergeFraming(guestRole, framing)),
      displayGuest: person,
      displayGuestRole: guestRole,
    };
  }

  if (
    guest &&
    subject &&
    normKey(guest) !== normKey(subject) &&
    isEntityLabel(guest) &&
    isEditorialTitle(subject, guest)
  ) {
    return {
      displayTitle: guest,
      displaySubtitle: formatSubtitle(subject, mergeFraming(guestRole, framing)),
      displayGuest: null,
      displayGuestRole: guestRole,
    };
  }

  if (guest && looksLikePersonName(guest) && subject && normKey(guest) !== normKey(subject)) {
    const company = companyHeadline(subject);
    if (company && normKey(company) !== normKey(guest)) {
      return {
        displayTitle: company,
        displaySubtitle: formatSubtitle(guest, mergeFraming(guestRole, framing)),
        displayGuest: guest,
        displayGuestRole: guestRole,
      };
    }
  }

  const { headline, tagline } = headlineFromSubject(subject);
  const subtitle = tagline
    ? formatSubtitle(tagline, mergeFraming(guestRole, framing))
    : mergeFraming(guestRole, framing);

  return {
    displayTitle: headline,
    displaySubtitle: subtitle,
    displayGuest: null,
    displayGuestRole: guestRole,
  };
}

/** @param {string} title @returns {ParsedTitle} */
function parseTitle(title) {
  title = norm(title);
  let m = title.match(/^(.+?)\s+CEO\s+(.+)$/i);
  if (m) return { company: m[1], person: m[2], role: "CEO" };
  m = title.match(/^(.+?)\s+with\s+(.+)$/i);
  if (m) return { company: m[1], person: m[2] };
  m = title.match(/^([^:]+):\s*(.+)$/);
  if (m) return { company: m[1], tagline: m[2] };
  return { company: title };
}

/** @param {string} title @param {string} guest @param {string} guestRole */
function resolveBusinessBreakdownsTitles(title, guest, guestRole) {
  const parsed = parseTitle(title);
  const headline = parsed.company;
  let displayGuest = null;
  let displayGuestRole = guestRole;

  if (parsed.person) {
    displayGuest = parsed.person;
    displayGuestRole = parsed.role || guestRole;
    return {
      displayTitle: headline,
      displaySubtitle: formatSubtitle(parsed.person, displayGuestRole, guestRole),
      displayGuest,
      displayGuestRole,
    };
  }

  if (guest && !titlesRedundant(title, guest) && normKey(guest) !== normKey(headline)) {
    displayGuest = guest;
    return {
      displayTitle: headline,
      displaySubtitle: formatSubtitle(guest, guestRole, parsed.tagline || ""),
      displayGuest,
      displayGuestRole,
    };
  }

  return {
    displayTitle: headline,
    displaySubtitle: formatSubtitle(parsed.tagline || "", guestRole),
    displayGuest,
    displayGuestRole,
  };
}

/**
 * @param {string} podcastId
 * @param {string} title
 * @param {string} guest
 * @param {string} [guestRole]
 */
export function resolveDisplayTitles(podcastId, title, guest, guestRole = "") {
  title = norm(title);
  guest = norm(guest);
  guestRole = norm(guestRole);

  if (ACQUIRED.has(podcastId)) {
    return resolveAcquiredTitles(title, guest, guestRole);
  }

  if (COMPANY_FIRST.has(podcastId)) {
    return resolveBusinessBreakdownsTitles(title, guest, guestRole);
  }

  const headline = guest || title;
  let subtitle = title;
  let displayGuest = guest || null;
  const displayGuestRole = guestRole;

  if (titlesRedundant(title, guest)) {
    subtitle = guestRole;
  } else if (guest && title.toLowerCase().startsWith(guest.toLowerCase())) {
    const m = title.match(/^(.+?)\s*[:—–-]\s*(.+)$/);
    if (m) {
      const rest = norm(m[2]);
      if (rest) {
        subtitle = rest;
        if (podcastId === "founders" && guestRole && !rest.toLowerCase().includes(guestRole.toLowerCase())) {
          subtitle = formatSubtitle(rest, guestRole);
        }
      } else {
        subtitle = guestRole;
      }
    }
  }

  if (subtitle && normKey(subtitle) === normKey(headline)) subtitle = guestRole;

  return {
    displayTitle: headline,
    displaySubtitle: subtitle || "",
    displayGuest,
    displayGuestRole,
  };
}

#!/usr/bin/env python3
"""Restore ILTB approved JSON from pre-expansion outputs markdown."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"
OUTPUTS = ROOT / "outputs"

CORRUPT_MARKERS = (
    "Transcript detail",
    "full transcript has",
    "2331-line",
    "2413-line",
    "Transcript evidence reinforces",
    "Transcript expansion note",
    "decision hygiene",
    "stress-test financing",
    "Related data point",
    "I think a fun place to begin",
)


def _is_corrupt(data: dict) -> bool:
    text = json.dumps(data)
    return any(m in text for m in CORRUPT_MARKERS)


def _blockquotes(section: str) -> list[str]:
    lines = []
    for line in section.splitlines():
        line = line.strip()
        if line.startswith(">"):
            lines.append(line.lstrip("> ").strip())
    return [ln for ln in lines if ln and not ln.startswith("#") and ln != "---"]


def _section(md: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}[^\n]*\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, md, re.DOTALL)
    return m.group(1) if m else ""


def _conclusion(md: str) -> str:
    sec = _section(md, "Background")
    # conclusion is before Background in template
    m = re.search(r"> ### Conclusion\s*\n>\s*\n>(.*?)(?=\n---|\n## )", md, re.DOTALL)
    if not m:
        return ""
    return " ".join(_blockquotes(m.group(1)))


def _background(md: str) -> str:
    quotes = _blockquotes(_section(md, "Background"))
    return "\n\n".join(quotes)


def _facts(md: str) -> list[str]:
    sec = _section(md, "Key Facts")
    facts = []
    for m in re.finditer(r">\s*\*\*F\d+\*\*\s*(.+?)(?=\n\n|>\s*\*\*F|\Z)", sec, re.DOTALL):
        fact = " ".join(line.strip().lstrip("> ") for line in m.group(1).splitlines() if line.strip())
        if fact:
            facts.append(fact)
    return facts[:3]


def _mental_model(md: str) -> dict:
    sec = _section(md, "Mental Model")
    name_m = re.search(r"Mental Model\s*·\s*\*([^*]+)\*", md) or re.search(r"\*([^*]+)\*", sec)
    name = name_m.group(1).strip() if name_m else ""
    comp_m = re.search(r">\s*\*\*Components\*\*\s*\n>(.*?)(?=\n>\s*\*\*Application\*\*)", sec, re.DOTALL)
    app_m = re.search(r">\s*\*\*Application\*\*\s*\n>(.*?)(?=\n---|\n## |\Z)", sec, re.DOTALL)
    components = " ".join(_blockquotes(comp_m.group(1))) if comp_m else ""
    application = " ".join(_blockquotes(app_m.group(1))) if app_m else ""
    return {"name": name, "components": components, "application": application}


def _insights(md: str) -> list[dict]:
    sec = _section(md, "Key Insights")
    chunks = re.split(r">\s*\*\*\d+\.\*\*", sec)
    insights = []
    for chunk in chunks[1:]:
        view_m = re.search(r"^\s*(.+?)(?=\n)", chunk.strip())
        q_m = re.search(r">\s*\*\*Q\*\*\s*(.+?)(?=\n)", chunk)
        a_m = re.search(r">\s*\*\*A\*\*\s*(.+?)(?=\n\n|>\s*\*\*\d+\.|\Z)", chunk, re.DOTALL)
        if view_m and q_m and a_m:
            answer = " ".join(line.strip().lstrip("> ") for line in a_m.group(1).splitlines() if line.strip())
            insights.append(
                {
                    "view": view_m.group(1).strip(),
                    "question": q_m.group(1).strip(),
                    "answer": answer,
                }
            )
    return insights[:3]


def _investments(md: str) -> list[dict]:
    sec = _section(md, "Investment Ideas")
    rows = []
    for m in re.finditer(
        r">\s*\*\*(\d+)\.\s*([^*]+)\*\*\s*·\s*([🟢🔴🟡]+)\s*([A-Z]+)\s*·\s*([●○]+)\s*(\w+)\s*\n>\s*\n>(.*?)(?=\n\n|>\s*\*\*\d+\.|\Z)",
        sec,
        re.DOTALL,
    ):
        thesis = " ".join(line.strip().lstrip("> ") for line in m.group(7).splitlines() if line.strip())
        direction = m.group(4).title()
        conf = m.group(6).title()
        rows.append(
            {
                "ticker": m.group(2).strip(),
                "direction": direction,
                "confidence": conf,
                "thesis": thesis,
            }
        )
    return rows[:3]


def _quotes(md: str) -> list[str]:
    return _blockquotes(_section(md, "Golden Quotes"))[:3]


def _chronology(md: str) -> dict:
    sec = _section(md, "Chronology")
    subject_m = re.search(r">\s*\*([^*]+)\*", sec)
    subject = subject_m.group(1).strip() if subject_m else ""
    events = []
    for m in re.finditer(r">\s*\*\*([^*]+)\*\*\s*(.+?)(?=\n\n|>\s*\*\*|\Z)", sec, re.DOTALL):
        event = " ".join(line.strip().lstrip("> ") for line in m.group(2).splitlines() if line.strip())
        events.append({"date": m.group(1).strip(), "event": event})
    return {"subject": subject, "events": events}


def _output_path(episode_id: str) -> Path | None:
    num = episode_id.replace("ep", "")
    matches = list(OUTPUTS.glob(f"EP{num}_{episode_id}.md"))
    return matches[0] if matches else None


def restore_episode(path: Path, *, dry_run: bool = False) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("podcast") != "Invest Like the Best":
        return False
    if not _is_corrupt(data):
        return False
    out_md = _output_path(path.stem)
    if not out_md:
        print(f"no output md for {path.stem}", file=sys.stderr)
        return False
    md = out_md.read_text(encoding="utf-8")
    restored = {
        **data,
        "conclusion": _conclusion(md) or data.get("conclusion", ""),
        "background": _background(md) or data.get("background", ""),
        "important_facts": _facts(md) or data.get("important_facts", []),
        "mental_model": _mental_model(md) or data.get("mental_model", {}),
        "key_insights": _insights(md) or data.get("key_insights", []),
        "top_investment_implications": _investments(md) or data.get("top_investment_implications", []),
        "golden_quotes": _quotes(md) or data.get("golden_quotes", []),
        "chronology": _chronology(md) or data.get("chronology", {}),
        "review_notes": (data.get("review_notes") or "Manual GPT batch v4.7").split("|")[0].strip(),
        "extraction_meta": {
            **(data.get("extraction_meta") or {}),
            "restored_from_outputs": True,
        },
    }
    # strip expansion marker if restored
    restored["extraction_meta"].pop("expanded_by", None)
    if dry_run:
        print(f"would restore {path.stem} from {out_md.name}")
        return True
    path.write_text(json.dumps(restored, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"restored {path.stem}")
    return True


def main() -> int:
    dry = "--dry-run" in sys.argv
    restored = 0
    for path in sorted(APPROVED.glob("ep*.json")):
        if restore_episode(path, dry_run=dry):
            restored += 1
    print(f"done: {restored} restored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

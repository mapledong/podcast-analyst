#!/usr/bin/env python3
"""Seed metadata-only approved JSON for 8 new Chinese podcast episodes (batch 3)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZH = ROOT / "data" / "approved" / "zh"
EN = ROOT / "data" / "approved"

ZJ_POD = "https://www.xiaoyuzhoufm.com/podcast/626b46ea9cbbf0451cf5a962"
TZS_POD = "https://www.xiaoyuzhoufm.com/podcast/643cdf1ad3d94ec2ad39ae94"
ZJ_APPLE = "https://podcasts.apple.com/cn/podcast/id1634356920"
TZS_APPLE = "https://podcasts.apple.com/cn/podcast/id1718660227"


def _placeholder_body(ticker: str = "GOOGL") -> dict:
    return {
        "conclusion": "占位",
        "background": "占位",
        "important_facts": ["占位"],
        "mental_model": {"name": "占位", "components": "占位", "application": "占位"},
        "key_insights": [{"view": "占位", "question": "占位", "answer": "占位"}],
        "top_investment_implications": [
            {"ticker": ticker, "direction": "Watch", "confidence": "Low", "thesis": "占位"}
        ],
        "golden_quotes": ["占位"],
        "chronology": {"subject": "占位", "events": [{"date": "2026", "event": "占位"}]},
    }


def _en_placeholder_body(ticker: str = "GOOGL") -> dict:
    return {
        "conclusion": "placeholder",
        "background": "placeholder",
        "important_facts": ["placeholder"],
        "mental_model": {"name": "placeholder", "components": "placeholder", "application": "placeholder"},
        "key_insights": [{"view": "placeholder", "question": "placeholder", "answer": "placeholder"}],
        "top_investment_implications": [
            {"ticker": ticker, "direction": "Watch", "confidence": "Low", "thesis": "placeholder"}
        ],
        "golden_quotes": ["placeholder"],
        "chronology": {"subject": "placeholder", "events": [{"date": "2026", "event": "placeholder"}]},
    }


EPISODES = {
    "zj-ep136": {
        "zh": {
            "episode_id": "zj-ep136",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 136,
                "title": "全球大模型季报第9集：和广密聊，Coding是AGI第二幕、硅谷御三家真相、模型正成为新一代OS",
                "guest": "广密",
                "guest_role": "AI 行业观察者",
                "date": "2026-04-14",
                "duration_minutes": 83,
                "youtube_url": "https://www.youtube.com/watch?v=u1Lzp-7Ybn8",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=u1Lzp-7Ybn8",
                    "apple_podcasts": ZJ_APPLE,
                    "xiaoyuzhou": ZJ_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "MSFT", "OPENAI", "Coding Agents", "AI OS"],
            **_placeholder_body("GOOGL"),
        },
        "en": {
            "episode_id": "zj-ep136",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 136,
                "title": "Global LLM Quarterly Ep.9: Coding as AGI Act II, Silicon Valley Big Three, Models as Next OS",
                "guest": "Guangmi",
                "guest_role": "AI Industry Observer",
                "date": "2026-04-14",
                "duration_minutes": 83,
                "youtube_url": "https://www.youtube.com/watch?v=u1Lzp-7Ybn8",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=u1Lzp-7Ybn8",
                    "apple_podcasts": ZJ_APPLE,
                    "xiaoyuzhou": ZJ_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "MSFT", "OPENAI", "Coding Agents", "AI OS"],
            **_en_placeholder_body("GOOGL"),
        },
    },
    "zj-ep137": {
        "zh": {
            "episode_id": "zj-ep137",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 137,
                "title": "对洪乐潼4小时访谈：AI for Math、Lean、数学天书",
                "guest": "洪乐潼",
                "guest_role": "AI for Math 研究者",
                "date": "2026-04-20",
                "duration_minutes": 264,
                "youtube_url": "https://www.youtube.com/watch?v=bv8ghyTFF9w",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=bv8ghyTFF9w",
                    "apple_podcasts": ZJ_APPLE,
                    "xiaoyuzhou": ZJ_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "AI for Math", "Lean", "形式化证明"],
            **_placeholder_body("GOOGL"),
        },
        "en": {
            "episode_id": "zj-ep137",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 137,
                "title": "4-Hour Interview with Hong Letong: AI for Math, Lean, and the Math Canon",
                "guest": "Hong Letong",
                "guest_role": "AI for Math Researcher",
                "date": "2026-04-20",
                "duration_minutes": 264,
                "youtube_url": "https://www.youtube.com/watch?v=bv8ghyTFF9w",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=bv8ghyTFF9w",
                    "apple_podcasts": ZJ_APPLE,
                    "xiaoyuzhou": ZJ_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "AI for Math", "Lean", "Formal Proof"],
            **_en_placeholder_body("GOOGL"),
        },
    },
    "zj-ep138": {
        "zh": {
            "episode_id": "zj-ep138",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 138,
                "title": "对罗福莉3.5小时访谈：OpenClaw、Agent范式、后训练、组织平权",
                "guest": "罗福莉",
                "guest_role": "AI 研究员",
                "date": "2026-04-24",
                "duration_minutes": 217,
                "youtube_url": "https://www.youtube.com/watch?v=vG1RBqn1sG4",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=vG1RBqn1sG4",
                    "apple_podcasts": ZJ_APPLE,
                    "xiaoyuzhou": ZJ_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "Agent", "OpenClaw", "后训练"],
            **_placeholder_body("GOOGL"),
        },
        "en": {
            "episode_id": "zj-ep138",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 138,
                "title": "3.5-Hour Interview with Luo Fuli: OpenClaw, Agent Paradigm, Post-Training, Org Flattening",
                "guest": "Luo Fuli",
                "guest_role": "AI Researcher",
                "date": "2026-04-24",
                "duration_minutes": 217,
                "youtube_url": "https://www.youtube.com/watch?v=vG1RBqn1sG4",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=vG1RBqn1sG4",
                    "apple_podcasts": ZJ_APPLE,
                    "xiaoyuzhou": ZJ_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "Agent", "OpenClaw", "Post-Training"],
            **_en_placeholder_body("GOOGL"),
        },
    },
    "zj-ep139": {
        "zh": {
            "episode_id": "zj-ep139",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 139,
                "title": "【Agent综述】和苏煜聊Agent技术史、OpenClaw Moment",
                "guest": "苏煜",
                "guest_role": "Agent 技术专家",
                "date": "2026-05-01",
                "duration_minutes": 138,
                "youtube_url": "https://www.youtube.com/watch?v=Xxz5uh0L1mE",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=Xxz5uh0L1mE",
                    "apple_podcasts": ZJ_APPLE,
                    "xiaoyuzhou": ZJ_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "Agent", "OpenClaw", "技术史"],
            **_placeholder_body("GOOGL"),
        },
        "en": {
            "episode_id": "zj-ep139",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 139,
                "title": "Agent Survey: Tech History and the OpenClaw Moment with Su Yu",
                "guest": "Su Yu",
                "guest_role": "Agent Technology Expert",
                "date": "2026-05-01",
                "duration_minutes": 138,
                "youtube_url": "https://www.youtube.com/watch?v=Xxz5uh0L1mE",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=Xxz5uh0L1mE",
                    "apple_podcasts": ZJ_APPLE,
                    "xiaoyuzhou": ZJ_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "Agent", "OpenClaw", "Tech History"],
            **_en_placeholder_body("GOOGL"),
        },
    },
    "tzs-ep178": {
        "zh": {
            "episode_id": "tzs-ep178",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 178,
                "title": "解码潮玩：工艺、生意、取舍，泡泡玛特",
                "guest": "Kevin、Johnny",
                "guest_role": "潮玩行业研究者",
                "date": "2026-04-07",
                "duration_minutes": 142,
                "youtube_url": "https://www.youtube.com/watch?v=bMR2Xk9DxbM",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=bMR2Xk9DxbM",
                    "apple_podcasts": TZS_APPLE,
                    "xiaoyuzhou": TZS_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9992.HK", "潮玩", "IP"],
            **_placeholder_body("9992.HK"),
        },
        "en": {
            "episode_id": "tzs-ep178",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 178,
                "title": "Decoding Designer Toys: Craft, Business, Trade-offs — Pop Mart",
                "guest": "Kevin, Johnny",
                "guest_role": "Designer-Toy Industry Researchers",
                "date": "2026-04-07",
                "duration_minutes": 142,
                "youtube_url": "https://www.youtube.com/watch?v=bMR2Xk9DxbM",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=bMR2Xk9DxbM",
                    "apple_podcasts": TZS_APPLE,
                    "xiaoyuzhou": TZS_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9992.HK", "Designer Toys", "IP"],
            **_en_placeholder_body("9992.HK"),
        },
    },
    "tzs-ep181": {
        "zh": {
            "episode_id": "tzs-ep181",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 181,
                "title": "听友交流：宏观冲击、泡泡玛特、Ai投研",
                "guest": "听友",
                "guest_role": "投资实战派听众",
                "date": "2026-04-27",
                "duration_minutes": 85,
                "youtube_url": "https://www.youtube.com/watch?v=D8POUUBHgoU",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=D8POUUBHgoU",
                    "apple_podcasts": TZS_APPLE,
                    "xiaoyuzhou": TZS_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9992.HK", "宏观", "AI 投研"],
            **_placeholder_body("9992.HK"),
        },
        "en": {
            "episode_id": "tzs-ep181",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 181,
                "title": "Listener Q&A: Macro Shocks, Pop Mart, AI Research Workflows",
                "guest": "Listeners",
                "guest_role": "Practical Investments Audience",
                "date": "2026-04-27",
                "duration_minutes": 85,
                "youtube_url": "https://www.youtube.com/watch?v=D8POUUBHgoU",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=D8POUUBHgoU",
                    "apple_podcasts": TZS_APPLE,
                    "xiaoyuzhou": TZS_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9992.HK", "Macro", "AI Research"],
            **_en_placeholder_body("9992.HK"),
        },
    },
    "tzs-ep182": {
        "zh": {
            "episode_id": "tzs-ep182",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 182,
                "title": "创新药实战复盘：估值与BD逻辑",
                "guest": "嘉宾",
                "guest_role": "创新药投资者",
                "date": "2026-05-04",
                "duration_minutes": 87,
                "youtube_url": "https://www.youtube.com/watch?v=suCMElcAOo0",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=suCMElcAOo0",
                    "apple_podcasts": TZS_APPLE,
                    "xiaoyuzhou": TZS_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["2171.HK", "创新药", "BD"],
            **_placeholder_body("2171.HK"),
        },
        "en": {
            "episode_id": "tzs-ep182",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 182,
                "title": "Innovative Drug Post-Mortem: Valuation and BD Logic",
                "guest": "Guest",
                "guest_role": "Biotech Investor",
                "date": "2026-05-04",
                "duration_minutes": 87,
                "youtube_url": "https://www.youtube.com/watch?v=suCMElcAOo0",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=suCMElcAOo0",
                    "apple_podcasts": TZS_APPLE,
                    "xiaoyuzhou": TZS_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["2171.HK", "Biotech", "BD"],
            **_en_placeholder_body("2171.HK"),
        },
    },
    "tzs-ep183": {
        "zh": {
            "episode_id": "tzs-ep183",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 183,
                "title": "投资的周期思维，亏钱学到的事儿",
                "guest": "永庆、吴晓波",
                "guest_role": "投资实战派联合创始人、财经作家",
                "date": "2026-05-11",
                "duration_minutes": 120,
                "youtube_url": "https://www.youtube.com/watch?v=-wsUV8jbDxE",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=-wsUV8jbDxE",
                    "apple_podcasts": TZS_APPLE,
                    "xiaoyuzhou": TZS_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["周期思维", "价值投资", "仓位管理"],
            **_placeholder_body("BRK.B"),
        },
        "en": {
            "episode_id": "tzs-ep183",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 183,
                "title": "Cycle Thinking in Investing — Lessons from Losing Money",
                "guest": "Yongqing, Wu Xiaobo",
                "guest_role": "Practical Investments Co-founder, Financial Author",
                "date": "2026-05-11",
                "duration_minutes": 120,
                "youtube_url": "https://www.youtube.com/watch?v=-wsUV8jbDxE",
                "links": {
                    "youtube": "https://www.youtube.com/watch?v=-wsUV8jbDxE",
                    "apple_podcasts": TZS_APPLE,
                    "xiaoyuzhou": TZS_POD,
                },
            },
            "episode_rating": {"overall": 3},
            "keywords": ["Cycle Thinking", "Value Investing", "Position Sizing"],
            **_en_placeholder_body("BRK.B"),
        },
    },
}

if __name__ == "__main__":
    ZH.mkdir(parents=True, exist_ok=True)
    for eid, pair in EPISODES.items():
        (ZH / f"{eid}.json").write_text(
            json.dumps(pair["zh"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        (EN / f"{eid}.json").write_text(
            json.dumps(pair["en"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"wrote {eid}")

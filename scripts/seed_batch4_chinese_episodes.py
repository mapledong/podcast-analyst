#!/usr/bin/env python3
"""Seed metadata-only approved JSON for 10 new Chinese podcast episodes (batch 4)."""

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


def _links(youtube: str | None = None) -> dict:
    links = {"apple_podcasts": ZJ_APPLE, "xiaoyuzhou": ZJ_POD}
    if youtube:
        links["youtube"] = youtube
    return links


def _tzs_links(youtube: str) -> dict:
    return {
        "youtube": youtube,
        "apple_podcasts": TZS_APPLE,
        "xiaoyuzhou": TZS_POD,
    }


EPISODES = {
    "zj-ep121": {
        "zh": {
            "episode_id": "zj-ep121",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 121,
                "title": "对DeepMind谭捷的访谈：机器人、跨本体、世界模型、Gemini Robotics 1.5和Google",
                "guest": "谭捷",
                "guest_role": "Google DeepMind 机器人团队高级研究科学家兼技术负责人",
                "date": "2025-11-28",
                "duration_minutes": 126,
                "youtube_url": "https://www.youtube.com/watch?v=2o281Zy5aZE",
                "links": _links("https://www.youtube.com/watch?v=2o281Zy5aZE"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "Gemini Robotics", "具身智能", "世界模型"],
            **_placeholder_body("GOOGL"),
        },
        "en": {
            "episode_id": "zj-ep121",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 121,
                "title": "DeepMind's Tan Jie on Robotics, Cross-Embodiment, World Models, Gemini Robotics 1.5, and Google",
                "guest": "Tan Jie",
                "guest_role": "Google DeepMind Senior Research Scientist & Robotics Tech Lead",
                "date": "2025-11-28",
                "duration_minutes": 126,
                "youtube_url": "https://www.youtube.com/watch?v=2o281Zy5aZE",
                "links": _links("https://www.youtube.com/watch?v=2o281Zy5aZE"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["GOOGL", "Gemini Robotics", "Embodied AI", "World Models"],
            **_en_placeholder_body("GOOGL"),
        },
    },
    "zj-ep120": {
        "zh": {
            "episode_id": "zj-ep120",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 120,
                "title": "小鹏新上任的刘先明首次访谈：Language是毒药、拆掉L、简单即美、换帅、小鹏的AI转型",
                "guest": "刘先明",
                "guest_role": "小鹏汽车自动驾驶中心负责人",
                "date": "2025-10-30",
                "duration_minutes": 109,
                "youtube_url": "",
                "links": {"apple_podcasts": ZJ_APPLE, "xiaoyuzhou": ZJ_POD},
            },
            "episode_rating": {"overall": 3},
            "keywords": ["XPEV", "VLA", "物理 AI", "自动驾驶"],
            **_placeholder_body("XPEV"),
        },
        "en": {
            "episode_id": "zj-ep120",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 120,
                "title": "XPeng's Liu Xianming on Removing Language from VLA, Physical AI, and the AI Transformation",
                "guest": "Liu Xianming",
                "guest_role": "XPeng Autonomous Driving Center Head",
                "date": "2025-10-30",
                "duration_minutes": 109,
                "youtube_url": "",
                "links": {"apple_podcasts": ZJ_APPLE, "xiaoyuzhou": ZJ_POD},
            },
            "episode_rating": {"overall": 3},
            "keywords": ["XPEV", "VLA", "Physical AI", "Autonomous Driving"],
            **_en_placeholder_body("XPEV"),
        },
    },
    "zj-ep109": {
        "zh": {
            "episode_id": "zj-ep109",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 109,
                "title": "机器人遭遇数据荒？与谢晨聊：仿真与合成数据、Meta天价收购和Alexandr Wang",
                "guest": "谢晨",
                "guest_role": "光轮智能创始人兼CEO",
                "date": "2025-06-20",
                "duration_minutes": 101,
                "youtube_url": "https://www.youtube.com/watch?v=pWY0HVUH8GA",
                "links": _links("https://www.youtube.com/watch?v=pWY0HVUH8GA"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["META", "NVDA", "合成数据", "具身智能"],
            **_placeholder_body("META"),
        },
        "en": {
            "episode_id": "zj-ep109",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 109,
                "title": "Robot Data Famine? Xie Chen on Simulation, Synthetic Data, Meta's Scale AI Deal, and Alexandr Wang",
                "guest": "Xie Chen",
                "guest_role": "Lightwheel Intelligence Founder & CEO",
                "date": "2025-06-20",
                "duration_minutes": 101,
                "youtube_url": "https://www.youtube.com/watch?v=pWY0HVUH8GA",
                "links": _links("https://www.youtube.com/watch?v=pWY0HVUH8GA"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["META", "NVDA", "Synthetic Data", "Embodied AI"],
            **_en_placeholder_body("META"),
        },
    },
    "zj-ep104": {
        "zh": {
            "episode_id": "zj-ep104",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 104,
                "title": "和Rokid祝铭明聊，吴妈、阿里、硬件创业黑森林的第11年",
                "guest": "祝铭明",
                "guest_role": "Rokid 创始人",
                "date": "2025-05-15",
                "duration_minutes": 129,
                "youtube_url": "https://www.youtube.com/watch?v=qW-kgogQwJc",
                "links": _links("https://www.youtube.com/watch?v=qW-kgogQwJc"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["BABA", "Rokid", "智能眼镜", "硬件创业"],
            **_placeholder_body("BABA"),
        },
        "en": {
            "episode_id": "zj-ep104",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 104,
                "title": "Rokid's Zhu Mingming on Alibaba, Smart Glasses, and 11 Years in Hardware's Dark Forest",
                "guest": "Zhu Mingming (Misa)",
                "guest_role": "Rokid Founder",
                "date": "2025-05-15",
                "duration_minutes": 129,
                "youtube_url": "https://www.youtube.com/watch?v=qW-kgogQwJc",
                "links": _links("https://www.youtube.com/watch?v=qW-kgogQwJc"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["BABA", "Rokid", "Smart Glasses", "Hardware"],
            **_en_placeholder_body("BABA"),
        },
    },
    "zj-ep83": {
        "zh": {
            "episode_id": "zj-ep83",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 83,
                "title": "黄仁勋和3万亿美元英伟达是如何炼成的？",
                "guest": "王亚军、译者",
                "guest_role": "《英伟达之道》译者及嘉宾",
                "date": "2024-12-10",
                "duration_minutes": 104,
                "youtube_url": "https://www.youtube.com/watch?v=h21t9FgGtOs",
                "links": _links("https://www.youtube.com/watch?v=h21t9FgGtOs"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["NVDA", "CUDA", "黄仁勋", "半导体"],
            **_placeholder_body("NVDA"),
        },
        "en": {
            "episode_id": "zj-ep83",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 83,
                "title": "How Jensen Huang and the $3 Trillion NVIDIA Were Built",
                "guest": "Wang Yajun & Translators",
                "guest_role": "The Nvidia Way Translators & Guests",
                "date": "2024-12-10",
                "duration_minutes": 104,
                "youtube_url": "https://www.youtube.com/watch?v=h21t9FgGtOs",
                "links": _links("https://www.youtube.com/watch?v=h21t9FgGtOs"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["NVDA", "CUDA", "Jensen Huang", "Semiconductors"],
            **_en_placeholder_body("NVDA"),
        },
    },
    "tzs-ep176": {
        "zh": {
            "episode_id": "tzs-ep176",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 176,
                "title": "如何打造超级IP？泡泡玛特和中国潮玩15年｜永庆对话陈格雷",
                "guest": "陈格雷",
                "guest_role": "《超级IP孵化原理》作者、盒成动漫创始人",
                "date": "2026-01-31",
                "duration_minutes": 101,
                "youtube_url": "https://www.youtube.com/watch?v=lqMnWASTTvk",
                "links": _tzs_links("https://www.youtube.com/watch?v=lqMnWASTTvk"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9992.HK", "IP 孵化", "潮玩"],
            **_placeholder_body("9992.HK"),
        },
        "en": {
            "episode_id": "tzs-ep176",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 176,
                "title": "Building Super IP: Pop Mart and 15 Years of China's Art-Toy Industry | Chen Grey Chan",
                "guest": "Chen Grey Chan",
                "guest_role": "Author of Super IP Incubation Principles",
                "date": "2026-01-31",
                "duration_minutes": 101,
                "youtube_url": "https://www.youtube.com/watch?v=lqMnWASTTvk",
                "links": _tzs_links("https://www.youtube.com/watch?v=lqMnWASTTvk"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9992.HK", "IP Incubation", "Art Toys"],
            **_en_placeholder_body("9992.HK"),
        },
    },
    "tzs-ep170": {
        "zh": {
            "episode_id": "tzs-ep170",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 170,
                "title": "深聊苹果：乔布斯、企业文化、竞争优势｜实战派好友胡维分享",
                "guest": "胡维",
                "guest_role": "投资实战派好友、苹果研究者",
                "date": "2026-02-02",
                "duration_minutes": 236,
                "youtube_url": "https://www.youtube.com/watch?v=zYdRq7lGjcE",
                "links": _tzs_links("https://www.youtube.com/watch?v=zYdRq7lGjcE"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["AAPL", "企业文化", "护城河"],
            **_placeholder_body("AAPL"),
        },
        "en": {
            "episode_id": "tzs-ep170",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 170,
                "title": "Deep Dive on Apple: Jobs, Culture, and Competitive Moat | Hu Wei",
                "guest": "Hu Wei",
                "guest_role": "Practical Investments Friend & Apple Researcher",
                "date": "2026-02-02",
                "duration_minutes": 236,
                "youtube_url": "https://www.youtube.com/watch?v=zYdRq7lGjcE",
                "links": _tzs_links("https://www.youtube.com/watch?v=zYdRq7lGjcE"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["AAPL", "Corporate Culture", "Moat"],
            **_en_placeholder_body("AAPL"),
        },
    },
    "tzs-ep167": {
        "zh": {
            "episode_id": "tzs-ep167",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 167,
                "title": "茅台和拼多多：白酒新周期、渠道新变革｜永庆对话15年从业者阿杜酒哥",
                "guest": "阿杜酒哥",
                "guest_role": "前拼多多酒行业负责人、15年酒水电商操盘手",
                "date": "2026-01-11",
                "duration_minutes": 141,
                "youtube_url": "https://www.youtube.com/watch?v=KR4aulvfQto",
                "links": _tzs_links("https://www.youtube.com/watch?v=KR4aulvfQto"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["PDD", "600519.SZ", "白酒", "渠道变革"],
            **_placeholder_body("PDD"),
        },
        "en": {
            "episode_id": "tzs-ep167",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 167,
                "title": "Moutai and Pinduoduo: Baijiu Cycle, Channel Reform | Du Jiuge",
                "guest": "Du Jiuge",
                "guest_role": "Former PDD Alcohol Category Lead, 15-Year Liquor E-commerce Operator",
                "date": "2026-01-11",
                "duration_minutes": 141,
                "youtube_url": "https://www.youtube.com/watch?v=KR4aulvfQto",
                "links": _tzs_links("https://www.youtube.com/watch?v=KR4aulvfQto"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["PDD", "600519.SZ", "Baijiu", "Channel Reform"],
            **_en_placeholder_body("PDD"),
        },
    },
    "tzs-ep158": {
        "zh": {
            "episode_id": "tzs-ep158",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 158,
                "title": "英伟达站上5万亿市值巅峰，我为何看空？",
                "guest": "大卫",
                "guest_role": "投资实战派主理人",
                "date": "2025-11-11",
                "duration_minutes": 51,
                "youtube_url": "https://www.youtube.com/watch?v=OSxQnF4sIz8",
                "links": _tzs_links("https://www.youtube.com/watch?v=OSxQnF4sIz8"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["NVDA", "估值", "做空"],
            **_placeholder_body("NVDA"),
        },
        "en": {
            "episode_id": "tzs-ep158",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 158,
                "title": "NVIDIA at $5T Peak — Why I Am Bearish",
                "guest": "David",
                "guest_role": "Practical Investments Host",
                "date": "2025-11-11",
                "duration_minutes": 51,
                "youtube_url": "https://www.youtube.com/watch?v=OSxQnF4sIz8",
                "links": _tzs_links("https://www.youtube.com/watch?v=OSxQnF4sIz8"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["NVDA", "Valuation", "Short Thesis"],
            **_en_placeholder_body("NVDA"),
        },
    },
    "tzs-ep126": {
        "zh": {
            "episode_id": "tzs-ep126",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 126,
                "title": "比亚迪：地表最强制造业龙头or汽车业恒大？",
                "guest": "大卫",
                "guest_role": "投资实战派主理人",
                "date": "2025-08-15",
                "duration_minutes": 93,
                "youtube_url": "https://www.youtube.com/watch?v=4NDIYC9mOFM",
                "links": _tzs_links("https://www.youtube.com/watch?v=4NDIYC9mOFM"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["BYDDY", "制造业", "新能源汽车"],
            **_placeholder_body("BYDDY"),
        },
        "en": {
            "episode_id": "tzs-ep126",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 126,
                "title": "BYD: World's Strongest Manufacturer or Auto Industry's Evergrande?",
                "guest": "David",
                "guest_role": "Practical Investments Host",
                "date": "2025-08-15",
                "duration_minutes": 93,
                "youtube_url": "https://www.youtube.com/watch?v=4NDIYC9mOFM",
                "links": _tzs_links("https://www.youtube.com/watch?v=4NDIYC9mOFM"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["BYDDY", "Manufacturing", "EV"],
            **_en_placeholder_body("BYDDY"),
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

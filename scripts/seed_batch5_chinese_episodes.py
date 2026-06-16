#!/usr/bin/env python3
"""Seed metadata-only approved JSON for 10 new Chinese podcast episodes (batch 5)."""

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


def _tzs_links(youtube: str | None = None) -> dict:
    links = {
        "apple_podcasts": TZS_APPLE,
        "xiaoyuzhou": TZS_POD,
    }
    if youtube:
        links["youtube"] = youtube
    return links


EPISODES = {
    "zj-ep118": {
        "zh": {
            "episode_id": "zj-ep118",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 118,
                "title": "对李想的第二次3小时访谈：CEO大模型、MoE、梁文锋、VLA、能量、记忆、对抗人性、亲密关系、人类的智慧",
                "guest": "李想",
                "guest_role": "理想汽车创始人兼CEO",
                "date": "2025-10-30",
                "duration_minutes": 166,
                "youtube_url": "https://www.youtube.com/watch?v=RxXVq7-sJzM",
                "links": _links("https://www.youtube.com/watch?v=RxXVq7-sJzM"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["LI", "CEO大模型", "VLA", "MoE"],
            **_placeholder_body("LI"),
        },
        "en": {
            "episode_id": "zj-ep118",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 118,
                "title": "Second 3-Hour Interview with Li Xiang: CEO LLM, MoE, VLA, Energy, Memory, and Human Nature",
                "guest": "Li Xiang",
                "guest_role": "Li Auto Founder & CEO",
                "date": "2025-10-30",
                "duration_minutes": 166,
                "youtube_url": "https://www.youtube.com/watch?v=RxXVq7-sJzM",
                "links": _links("https://www.youtube.com/watch?v=RxXVq7-sJzM"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["LI", "CEO LLM", "VLA", "MoE"],
            **_en_placeholder_body("LI"),
        },
    },
    "zj-ep108": {
        "zh": {
            "episode_id": "zj-ep108",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 108,
                "title": "余凯口述30年史：世界不止刀光剑影，是一部人来人往的江湖故事",
                "guest": "余凯",
                "guest_role": "地平线创始人兼CEO",
                "date": "2025-07-07",
                "duration_minutes": 177,
                "youtube_url": "https://www.youtube.com/watch?v=853ETjAecz4",
                "links": _links("https://www.youtube.com/watch?v=853ETjAecz4"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9660.HK", "地平线", "自动驾驶", "芯片"],
            **_placeholder_body("9660.HK"),
        },
        "en": {
            "episode_id": "zj-ep108",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 108,
                "title": "Kai Yu's 30-Year Oral History: Horizon Robotics and China's AD Chip Journey",
                "guest": "Kai Yu",
                "guest_role": "Horizon Robotics Founder & CEO",
                "date": "2025-07-07",
                "duration_minutes": 177,
                "youtube_url": "https://www.youtube.com/watch?v=853ETjAecz4",
                "links": _links("https://www.youtube.com/watch?v=853ETjAecz4"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9660.HK", "Horizon Robotics", "Autonomous Driving", "Chips"],
            **_en_placeholder_body("9660.HK"),
        },
    },
    "zj-ep96": {
        "zh": {
            "episode_id": "zj-ep96",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 96,
                "title": "和郎咸朋聊，自动驾驶10年演进史、关键技术细节和特斯拉",
                "guest": "郎咸朋",
                "guest_role": "理想汽车智能驾驶负责人",
                "date": "2025-03-16",
                "duration_minutes": 120,
                "youtube_url": "https://www.youtube.com/watch?v=qtugoE1xQZk",
                "links": _links("https://www.youtube.com/watch?v=qtugoE1xQZk"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["TSLA", "自动驾驶", "FSD", "VLA"],
            **_placeholder_body("TSLA"),
        },
        "en": {
            "episode_id": "zj-ep96",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 96,
                "title": "Lang Xianpeng on a Decade of Autonomous Driving, Key Technical Details, and Tesla",
                "guest": "Lang Xianpeng",
                "guest_role": "Li Auto Intelligent Driving Head",
                "date": "2025-03-16",
                "duration_minutes": 120,
                "youtube_url": "https://www.youtube.com/watch?v=qtugoE1xQZk",
                "links": _links("https://www.youtube.com/watch?v=qtugoE1xQZk"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["TSLA", "Autonomous Driving", "FSD", "VLA"],
            **_en_placeholder_body("TSLA"),
        },
    },
    "zj-ep122": {
        "zh": {
            "episode_id": "zj-ep122",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 122,
                "title": "朱啸虎现实主义故事的第三次连载：人工智能的盛筵与泡泡",
                "guest": "朱啸虎",
                "guest_role": "金沙江创投主管合伙人",
                "date": "2025-12-09",
                "duration_minutes": 48,
                "youtube_url": "https://www.youtube.com/watch?v=wK0-m3rKgZ0",
                "links": _links("https://www.youtube.com/watch?v=wK0-m3rKgZ0"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["META", "GOOGL", "AI应用", "泡沫"],
            **_placeholder_body("META"),
        },
        "en": {
            "episode_id": "zj-ep122",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 122,
                "title": "Zhu Xiaohu on AI Feast and Bubble — Third Installment of China Realism",
                "guest": "Zhu Xiaohu",
                "guest_role": "GSR Ventures Managing Partner",
                "date": "2025-12-09",
                "duration_minutes": 48,
                "youtube_url": "https://www.youtube.com/watch?v=wK0-m3rKgZ0",
                "links": _links("https://www.youtube.com/watch?v=wK0-m3rKgZ0"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["META", "GOOGL", "AI Apps", "Bubble"],
            **_en_placeholder_body("META"),
        },
    },
    "zj-ep125": {
        "zh": {
            "episode_id": "zj-ep125",
            "podcast": "张小珺商业访谈录",
            "host": "张小珺",
            "metadata": {
                "episode_number": 125,
                "title": "Freda的投资札记第1集：下注OpenAI、Robinhood往事，美国资本坏小孩、算盘与泡沫",
                "guest": "Freda",
                "guest_role": "光速创投合伙人",
                "date": "2025-12-16",
                "duration_minutes": 84,
                "youtube_url": "https://www.youtube.com/watch?v=k82iFzvKFCQ",
                "links": _links("https://www.youtube.com/watch?v=k82iFzvKFCQ"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["META", "HOOD", "OpenAI", "Token经济"],
            **_placeholder_body("META"),
        },
        "en": {
            "episode_id": "zj-ep125",
            "podcast": "Zhang Xiaojun Podcast",
            "host": "Zhang Xiaojun",
            "metadata": {
                "episode_number": 125,
                "title": "Freda's Investment Notes #1: Betting on OpenAI, Robinhood History, and US Capital Bad Boys",
                "guest": "Freda",
                "guest_role": "Lightspeed Venture Partners Partner",
                "date": "2025-12-16",
                "duration_minutes": 84,
                "youtube_url": "https://www.youtube.com/watch?v=k82iFzvKFCQ",
                "links": _links("https://www.youtube.com/watch?v=k82iFzvKFCQ"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["META", "HOOD", "OpenAI", "Token Economics"],
            **_en_placeholder_body("META"),
        },
    },
    "tzs-ep156": {
        "zh": {
            "episode_id": "tzs-ep156",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 156,
                "title": "段永平买茅台，我们要跟着买吗？|David对谈金舆资产创始人孟平",
                "guest": "孟平",
                "guest_role": "金舆资产创始人",
                "date": "2025-11-09",
                "duration_minutes": 96,
                "youtube_url": "",
                "links": _tzs_links(),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["600519.SZ", "段永平", "茅台", "价值投资"],
            **_placeholder_body("600519.SZ"),
        },
        "en": {
            "episode_id": "tzs-ep156",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 156,
                "title": "Duan Yongping Bought Moutai — Should We Follow? | David & Meng Ping",
                "guest": "Meng Ping",
                "guest_role": "Jinyu Asset Founder",
                "date": "2025-11-09",
                "duration_minutes": 96,
                "youtube_url": "",
                "links": _tzs_links(),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["600519.SZ", "Duan Yongping", "Moutai", "Value Investing"],
            **_en_placeholder_body("600519.SZ"),
        },
    },
    "tzs-ep146": {
        "zh": {
            "episode_id": "tzs-ep146",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 146,
                "title": "畅聊新消费王者F4 | 泡泡玛特、老铺黄金、蜜雪冰城、毛戈平",
                "guest": "大卫",
                "guest_role": "投资实战派主理人",
                "date": "2025-09-08",
                "duration_minutes": 76,
                "youtube_url": "",
                "links": _tzs_links(),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9992.HK", "新消费", "IP", "潮玩"],
            **_placeholder_body("9992.HK"),
        },
        "en": {
            "episode_id": "tzs-ep146",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 146,
                "title": "New Consumer Kings F4: Pop Mart, Laopu Gold, Mixue, and Maogeping",
                "guest": "David",
                "guest_role": "Practical Investments Host",
                "date": "2025-09-08",
                "duration_minutes": 76,
                "youtube_url": "",
                "links": _tzs_links(),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["9992.HK", "New Consumer", "IP", "Art Toys"],
            **_en_placeholder_body("9992.HK"),
        },
    },
    "tzs-ep115": {
        "zh": {
            "episode_id": "tzs-ep115",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 115,
                "title": "拼多多，竞争优势、财报、复盘、市场，2025年4月28日",
                "guest": "永庆",
                "guest_role": "投资实战派嘉宾、精选50策略",
                "date": "2025-04-30",
                "duration_minutes": 45,
                "youtube_url": "https://www.youtube.com/watch?v=4TMveqX62rA",
                "links": _tzs_links("https://www.youtube.com/watch?v=4TMveqX62rA"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["PDD", "电商", "Temu", "财报"],
            **_placeholder_body("PDD"),
        },
        "en": {
            "episode_id": "tzs-ep115",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 115,
                "title": "Pinduoduo: Competitive Edge, Earnings, Review, and Market — Apr 28, 2025",
                "guest": "Yongqing",
                "guest_role": "Practical Investments Guest, Curated 50 Strategy",
                "date": "2025-04-30",
                "duration_minutes": 45,
                "youtube_url": "https://www.youtube.com/watch?v=4TMveqX62rA",
                "links": _tzs_links("https://www.youtube.com/watch?v=4TMveqX62rA"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["PDD", "E-commerce", "Temu", "Earnings"],
            **_en_placeholder_body("PDD"),
        },
    },
    "tzs-ep109": {
        "zh": {
            "episode_id": "tzs-ep109",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 109,
                "title": "美团，商业模式、财报解读和投资思考 | 精选50系列，2025年4月2日",
                "guest": "大卫",
                "guest_role": "投资实战派主理人",
                "date": "2025-04-02",
                "duration_minutes": 35,
                "youtube_url": "https://www.youtube.com/watch?v=IUuUJZlPNxY",
                "links": _tzs_links("https://www.youtube.com/watch?v=IUuUJZlPNxY"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["3690.HK", "本地生活", "外卖", "财报"],
            **_placeholder_body("3690.HK"),
        },
        "en": {
            "episode_id": "tzs-ep109",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 109,
                "title": "Meituan: Business Model, Earnings Read, and Investment View | Curated 50, Apr 2, 2025",
                "guest": "David",
                "guest_role": "Practical Investments Host",
                "date": "2025-04-02",
                "duration_minutes": 35,
                "youtube_url": "https://www.youtube.com/watch?v=IUuUJZlPNxY",
                "links": _tzs_links("https://www.youtube.com/watch?v=IUuUJZlPNxY"),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["3690.HK", "Local Services", "Delivery", "Earnings"],
            **_en_placeholder_body("3690.HK"),
        },
    },
    "tzs-ep34": {
        "zh": {
            "episode_id": "tzs-ep34",
            "podcast": "投资实战派",
            "host": "永庆 & 大卫",
            "metadata": {
                "episode_number": 34,
                "title": "理想汽车：狂奔的李想能否打赢第二场关键战争？当前投资价值&风险？ | 聊透全球50家公司系列",
                "guest": "大卫",
                "guest_role": "投资实战派主理人",
                "date": "2024-04-14",
                "duration_minutes": 129,
                "youtube_url": "",
                "links": _tzs_links(),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["LI", "新能源汽车", "智能驾驶", "估值"],
            **_placeholder_body("LI"),
        },
        "en": {
            "episode_id": "tzs-ep34",
            "podcast": "Practical Investments",
            "host": "Yongqing & David",
            "metadata": {
                "episode_number": 34,
                "title": "Li Auto: Can Li Xiang Win the Second Critical War? Investment Value & Risks",
                "guest": "David",
                "guest_role": "Practical Investments Host",
                "date": "2024-04-14",
                "duration_minutes": 129,
                "youtube_url": "",
                "links": _tzs_links(),
            },
            "episode_rating": {"overall": 3},
            "keywords": ["LI", "EV", "Intelligent Driving", "Valuation"],
            **_en_placeholder_body("LI"),
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

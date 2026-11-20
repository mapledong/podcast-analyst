#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bilingual ZJ E156, six-hour Liang Qiwei tape."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402
from src.chinese_transcript import load_transcript_body, quote_supported_in_transcript, transcript_path  # noqa: E402

EID = "zj-ep156"
QUOTES = ["腾讯也是我们的股东", "我用3000万回购了", "对于只有20个人的团队来说"]


def main():
    body = load_transcript_body(transcript_path(EID))
    for q in QUOTES:
        print(EID, "OK" if quote_supported_in_transcript(q, body) else "FAIL", q)
        if not quote_supported_in_transcript(q, body):
            raise SystemExit(q)
    meta = {
        "episode_number": 156,
        "title": "Liang Qiwei on Phantom Blade Zero, Wuxia, and Fifteen Years of Making Games",
        "guest": "Liang Qiwei",
        "guest_role": "Founder, Lingyoufang · Phantom Blade Zero",
        "date": "2026-11-13",
        "duration_minutes": 387,
        "youtube_url": "https://www.youtube.com/watch?v=uq7aHKfXlJI",
        "links": {
            "youtube": "https://www.youtube.com/watch?v=uq7aHKfXlJI",
            "apple_podcasts": "https://podcasts.apple.com/cn/podcast/id1634356920",
            "xiaoyuzhou": "https://www.xiaoyuzhoufm.com/episode/6af5debf14d01a26f8a900ac",
        },
    }
    concl = (
        "Liang Qiwei's six hours end on a company, not only on a definition of xia. "
        "Xu Xiaoping wired 1 million yuan to him personally in August 2011, before the "
        "company existed. Years later Liang bought that stake back for 30 million. The "
        "team was about 20 people. Tencent is a shareholder he calls nice. NetEase came "
        "in around 2013. A weekly report and a wuxia author cannot share one structure. "
        "The pirate still has to live with the navy."
    )
    bg = (
        "E156, Nov 13, about 387 minutes. Zhang Xiaojun with Liang Qiwei of Lingyoufang, "
        "on Phantom Blade Zero and the fifteen years before it. A colleague's sixteen "
        "characters open the tape: wronged, on the run, alone in the maze, hatred to the "
        "end. Whisper hears the studio as 领务坊 and 林游坊. YouTube captions were off. "
        "This is a small-model transcript of a very long sitting, so names of side "
        "characters are less reliable than the deals and the argument. The sitting "
        "moves from the definition of xia, to why players reject a moral they can "
        "see being planted, to the exam-kid biography, to the August 2011 wire, "
        "the 2013 mobile ship, and the console direction that was not replaced. "
        "Tencent as shareholder and NetEase as 2013 publisher are the two public "
        "names. ZhenFund is the personal check that became a share and then a "
        "30 million buyback. The aesthetic talk, Gu Long alleys and a darker "
        "cut he did not ship, is in the same file as the cap table."
    )
    facts = [
        (
            "What counts as xia. Liang treats hatred and grievance as the fuel of the "
            "whole wuxia genre, the thing that separates it from other stories. Nothing "
            "pushes harder. Xia is the extreme form of keeping your own mind while that "
            "pressure is on you. The difference from a good person is the size of the "
            "will. Helping a grandmother "
            "across the street is ordinary goodness. Pulling her out of traffic when "
            "bystanders may say you knocked her down is the version that costs something. "
            "He put the moral in the script once, lines in the key of a great xia "
            "protecting ordinary people. Most players rejected it. Not the ethic. They "
            "saw the author's intention. The 16 characters a colleague used for the "
            "game are his modern compression of the "
            "old plot: wronged, fugitive, alone inside a rigged board, hatred running "
            "to the end."
        ),
        (
            "No person is the enemy. The boss is the market, the objective world, the "
            "thing you have to fight whether or not you have a villain. Liang describes "
            "himself as a small-town exam kid. The enemy was the paper in front of him. "
            "Genius, he says, is unreliable. Effective makers are few. At 20 the "
            "wuxia trap is the flashy talent, beautiful technique, who never reaches the "
            "great city. The ones who do look a little slow. Guo Jing, not the brilliant "
            "cousin. A young man who has just made money will not say plainly that the "
            "company has to profit in order to make a better game. He wanted the world "
            "to recognize him. Later he will say the plain sentence."
        ),
        (
            "The company had to exist. A personal creator inside a big-company KPI, a "
            "weekly report, and someone else's culture hits a structural paradox. Liang "
            "thinks that kind of person has to become a founder or the work cannot be "
            "finished. Big companies are still good. Tencent is a shareholder and, he "
            "says, nice, and has helped many people. The relationship is the wuxia one: "
            "the wandering fighter and the regular army, or the pirate and the navy in "
            "One Piece. The money started before "
            "the company. In August 2011 Xu Xiaoping, through ZhenFund, wired 1 million "
            "yuan to Liang's personal account. Almost no terms. The company, Lingyoufang, "
            "was registered that month, and the personal money was later converted into "
            "shares. Years afterward Liang bought that piece back for 30 million yuan "
            "and calls it a good little case for Xu. A ZhenFund vice president joined in "
            "September 2011. NetEase came around 2013, as a publishing check, in the "
            "decade when Chinese mobile games were the primitive accumulation and, he "
            "also says, a black history. NetEase was starting its own mobile games at "
            "the same time. The team he describes for that period is about 20 people. "
            "Phantom Blade, the mobile game, shipped around 2013. The console ambition "
            "was already in his head when it was announced, and the direction has not "
            "been replaced. Departed colleagues asked to be named in the credits."
        ),
    ]
    mental = {
        "name": "Hatred as Fuel × A Dull Finish × Personal Money First",
        "components": (
            "Wuxia runs on grievance. Xia is will that stays human under it, not ordinary "
            "kindness. Players refuse the moral they can see you planting. The boss is "
            "the world, not a face. Flashy talent does not finish. The finisher looks "
            "slow. A creator with a weekly report inside someone else's culture cannot "
            "complete the work, so the studio has to be a company, and the company has "
            "to make money to make a better game. Xu's 1 million yuan arrived in a "
            "personal account in August 2011 and left at 30 million. Tencent can be a "
            "nice shareholder and still be the navy. NetEase's 2013 check sat inside "
            "the mobile decade. About 20 people was the team. The direction announced "
            "for the big game has not been swapped out. Show the code in the fight, "
            "not in a speech the player can spot as a lesson. A grandmother in "
            "traffic is the test, because the crowd may blame the person who helps. "
            "Color was added for this build. His own picture would have stayed darker, "
            "closer to a Gu Long alley than to a bright poster. Distinct makers are "
            "rarer than merely effective ones, and a copied Gu Long is not a second "
            "Gu Long. The exam kid's advantage is that the enemy stays the paper, "
            "then the market, and never has to be invented as a face. Names in the "
            "credits, including people who left, follow the same rule. If the pay is "
            "close, the name on the work still matters. A six-hour tape still has "
            "one cap table: personal money first, a nice shareholder second, a "
            "publisher in the mobile decade third, and a direction that survived "
            "the announcement."
        ),
        "application": (
            "Private:Lingyoufang is the studio. TCEHY is the shareholder he is willing "
            "to call nice, not a claim that the pirate became the navy. NTES is the "
            "2013 mobile publisher, in the decade he also calls a black history. Do not "
            "read a six-hour aesthetic talk as a production schedule. The operating "
            "facts are the personal wire, the buyback, the 20-person team, and the "
            "refusal to let one slogan do the moral work."
        ),
    }
    insights = [
        {
            "view": "Ordinary goodness is not xia.",
            "question": "What is the grandmother test?",
            "answer": (
                "Walking her across an empty street proves you are a decent person. "
                "It does not take extraordinary will. Pulling her out of moving traffic "
                "when the crowd may decide you caused the fall is the version Liang "
                "will call xia. Hatred and grievance are the fuel. Keeping a human "
                "mind under that fuel is the result. He tried putting the moral in "
                "the dialogue. Players saw the intention and rejected the line, not "
                "the ethic. A colleague's 16-character brief is the same fuel in "
                "shorter form: wronged, on the run, alone inside a rigged maze, "
                "hatred at the end. Those words start the plot. They do not finish "
                "the character. The playable question is whether he stays human "
                "while using them. Liang will not count a riskless kindness. He "
                "will count the help that can be misread as guilt. That is why a "
                "slogan in a cutscene fails and a costly action can still work. "
                "The audience is not rejecting mercy. It is rejecting the moment "
                "it can see the writer asking for credit."
            ),
        },
        {
            "view": "The brilliant cousin does not finish.",
            "question": "Who reaches the great city?",
            "answer": (
                "Wuxia is full of beautiful technique that never becomes mastery. "
                "Liang's finisher looks a little dull. Guo Jing, not the flashy "
                "relative. He says real genius is unreliable and fragile, and that "
                "distinct makers are rarer than effective ones. Gu Long does not "
                "have many copies. A young man who has just made money will not say "
                "out loud that the company must profit. Later he will. At 20 the "
                "point of the money is to be seen. The later sentence is plainer: "
                "profit is what lets the next game exist. The dull finisher is the "
                "one who can say that without turning it into a pose."
            ),
        },
        {
            "view": "The navy can be a nice shareholder.",
            "question": "How did the company start?",
            "answer": (
                "August 2011, 1 million yuan into a personal account, almost no terms, "
                "company registered the same month. The buyback was 30 million. "
                "Tencent is a shareholder he calls nice. NetEase's publishing money "
                "arrived around 2013, when the team was about 20 people. A founder "
                "who needs a KPI and a weekly report is, in his view, inside a "
                "paradox. The pirate still has to live with the navy. August 2011 is "
                "the personal account. The company is registered the same month. "
                "The 30 million buyback is years later. NetEase is 2013, about 20 "
                "people, mobile Phantom Blade. Tencent stays a shareholder. None "
                "of those facts replaces the author. They are how the author keeps "
                "a structure that can finish a long game."
            ),
        },
    ]
    invest = [
        {"ticker": "Private:Lingyoufang", "direction": "Long", "confidence": "Low", "thesis": "The studio that had to be a company: 1 million personal in 2011, 30 million buyback, about 20 people — low"},
        {"ticker": "TCEHY", "direction": "Long", "confidence": "Low", "thesis": "Shareholder he calls nice, the regular army in the wuxia metaphor, not the author — low"},
        {"ticker": "NTES", "direction": "Long", "confidence": "Low", "thesis": "2013 mobile publishing check, inside the decade he also calls a black history — low"},
    ]
    chrono = {"subject": "Liang Qiwei · Lingyoufang · Phantom Blade", "events": [
        {"date": "2011-08", "event": "Xu wires 1 million yuan personally; Lingyoufang is registered"},
        {"date": "2011-09", "event": "ZhenFund vice president joins"},
        {"date": "2013", "event": "Phantom Blade mobile ships; NetEase publishing money; team about 20"},
        {"date": "2013-14", "event": "Chinese mobile-game decade he calls both accumulation and a black history"},
        {"date": "later", "event": "Buys the personal stake back for 30 million yuan"},
        {"date": "2020s", "event": "Phantom Blade Zero direction unchanged from the announcement"},
        {"date": "2026-11-13", "event": "E156 publishes, about 387 minutes"},
    ]}
    en = en_std(EID, "Zhang Xiaojun Podcast", "Zhang Xiaojun", meta, 3,
                ["Private:Lingyoufang", "TCEHY", "NTES"],
                concl, bg, facts, mental, insights, invest, QUOTES, chrono,
                "| v4.10 window ZJ E156", "whisper-small")
    zh_meta = dict(meta)
    zh_meta.update(
        title="156. 对影之刃零梁其伟6小时访谈：3A游戏、15年创业路上斩妖除魔、命运",
        guest="梁其伟",
        guest_role="灵游坊创始人 · 《影之刃零》",
    )
    zh = dict(en)
    zh.update({
        "podcast": "张小珺商业访谈录", "host": "张小珺", "metadata": zh_meta,
        "conclusion": "梁其伟用六个小时讲什么是侠，以及这种人为什么必须变成一家公司。仇恨和冤屈是发动机。侠是在这股压力下仍守住本心的超常意志，不是日常的善良。玩家看得出你在埋道德，就会拒绝那句台词。BOSS是客观世界，不是某个人。花哨的天才完不成。能走完的人看起来有点钝。2011年8月徐小平把100万打进个人账户，公司还没成立。多年后梁用3000万把那笔股份买回来。团队大约20人。腾讯是他称为nice的股东。网易大约2013年进来，正是手游起势的时候。大厂的KPI和武侠作者不能待在同一个结构里。海盗仍然要跟海军相处。",
        "background": "E156，11月13日，大约387分钟。张小珺和灵游坊梁其伟，谈《影之刃零》和之前的十五年。同事用十六个字开场：蒙冤、亡命、独行迷局、恨到尽头。Whisper把灵游坊听成领务坊、林游坊。YouTube没有字幕。这是一场很长的小模型转写，配角名字不如交易和论点可靠。",
        "important_facts": [
            "什么算侠。梁把仇恨和冤屈当成整个武侠类型的燃料，也是它和其他故事的分界。没有更强的推动力。侠是在这股压力里仍守住自己的心，而且形式极端。行为可以像救助，可以像没有被复仇蒙住，也可以像蒙冤之后怎么自处。和好人的差别是意志的尺寸。扶老奶奶过马路是日常的好，不需要超常意志。她倒在车流里，你把她拉开，旁边的人可能说是你撞的，你仍然拉，这才是他愿意称为侠的版本。他曾经把道德写进台词，大侠保护普通人。多数玩家拒绝了。不是拒绝那个伦理。他们看穿了作者的意图，现在的受众很会看。说出来和只做不说是两种效果。同事用来概括游戏的十六个字，是他把旧情节压成的现代版：蒙冤、逃亡、一个人在被做局的棋盘里、恨到最后。",
            "没有某个人是敌人。BOSS是市场、是客观世界、是不管有没有反派你都要打的东西。梁说自己是典型的小镇做题家，敌人就是眼前那张卷子。小珺提起更早一次对话里的阿斯伯格。游戏、办公室和衣服的暗，不是为暗而暗。他拿古龙比：夜晚、长亭、小巷。他为玩家加了颜色。如果只按自己的想象，这一版会更黑。他说天才不靠谱，在现实里残缺、脆弱。有效的创作者不多，有独特个性的更少。古龙没有几个拷贝。一个人最终能做出什么，仍要看他活过什么。武侠里的陷阱是天赋漂亮、招式华丽、永远到不了大成的人。走完的人看起来有点钝。郭靖，不是那个闪的表哥。刚赚到钱的二十多岁不会直说公司必须盈利才能做更好的游戏。他要社会认可。后来他会把这句说白。",
            "公司必须存在。一个创作者如果待在别人的KPI、周报和公司文化里，结构上就有一个悖论。梁认为这种人必须成为创始人，事情才做得完。大厂仍然好。腾讯是股东，他说nice，也帮过很多人。关系是武侠里的：江湖和正规军，或者《海贼王》里海盗和海军。不同的活法，不是道德排名。钱比公司先到。2011年8月，徐小平经真格把100万打进梁的个人账户，几乎没有条款。灵游坊同月注册，这笔个人的钱后来转成股份。多年以后梁用3000万买回那一块，说这是徐老师一笔不错的小case。真格一位副总裁2011年9月加入。网易大约2013年进来，一笔发行费用，卡在他称为中国手游原始积累、同时也是黑历史的十年。网易自己也在做手游。他描述的那个时期团队大约20人。《影之刃》手游大约2013年上线。主机的方向在宣布时已经想好，到现在没有被换掉。腾讯的人坐进公司，给过一个促使他再想一层的观点。离开的同事后来要求在名单里写上自己也参与过。他答应了。现实重要，但如果钱没有差太多，人仍然要一个不只是钱的追求。",
        ],
        "mental_model": {
            "name": "仇恨做燃料 × 钝的人走完 × 个人账户里的第一笔钱",
            "components": "武侠靠冤屈推动。侠是在这股燃料下仍然像人的意志，不是日常善良。玩家拒绝他们看得出你在埋的道德。BOSS是世界，不是一张脸。花哨的天赋走不完。走完的人看起来慢。创作者如果每周写别人的周报，就做不完这件事，所以工作室必须是公司，公司必须赚钱才能做更好的游戏。徐的100万在2011年8月进了个人账户，以3000万离开。腾讯可以是nice的股东，同时仍是海军。网易2013年的支票坐在手游十年里。团队大约20人。大作宣布时的方向没有被换掉。",
            "application": "Private:Lingyoufang是这家工作室。TCEHY是他愿意称为nice的股东，不是海盗变成了海军。NTES是2013年的手游发行方，也在他称为黑历史的十年里。不要把六个小时的美学谈话读成制作排期。经营事实是那笔个人电汇、回购、20人的团队，以及拒绝用一句口号完成道德。",
        },
        "key_insights": [
            {"view": "日常的好不是侠。", "question": "老奶奶的测验是什么？", "answer": "空街上扶她过去，说明你是好人，不需要超常意志。车流里把她拉开，人群可能认定是你撞的，这才是梁愿意称为侠的版本。仇恨和冤屈是燃料。在燃料下保住人性是结果。他把道德写进对白，玩家看见意图，拒绝的是那句台词，不是伦理。"},
            {"view": "闪的表哥走不完。", "question": "谁到得了大成？", "answer": "武侠里满是漂亮招式，到不了大成。梁的完成者看起来有点钝。郭靖，不是那个闪的亲戚。他说真正的天才不靠谱，而且脆弱。有个性的人比有效的人更少。古龙没有很多拷贝。刚赚到钱的年轻人不会大声说公司必须盈利。后来他会。"},
            {"view": "海军也可以是一个nice的股东。", "question": "公司怎么开始的？", "answer": "2011年8月，100万进个人账户，几乎没有条款，公司同月注册。回购是3000万。腾讯是他称为nice的股东。网易的发行钱大约2013年到，团队大约20人。在他看来，需要KPI和周报的创始人处在一个悖论里。海盗仍然要和海军一起活。"},
        ],
        "golden_quotes": QUOTES,
        "review_notes": "| v4.10 window 张小珺 E156",
    })
    dump(ROOT / f"data/approved/{EID}.json", en)
    dump(ROOT / f"data/approved/zh/{EID}.json", zh)
    validate_file(ROOT / f"data/approved/{EID}.json")


if __name__ == "__main__":
    main()

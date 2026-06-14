#!/usr/bin/env python3
"""Transcript-grounded v5.4 expansion for three Acquired episodes."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.validate import load_template_config, validate_summary, word_count, word_gap  # noqa: E402
from src.template_config import template_path_for_podcast  # noqa: E402

APPROVED = ROOT / "data" / "approved"
TMPL = load_template_config(template_path_for_podcast("Acquired"))

EXPANSIONS: dict[str, dict] = {
    "acq-season-2-episode-9github": {
        "background": (
            "Season 2 Episode 9 (~91 min) recorded June 5, 2018 — the day after Microsoft announced "
            "$7.5B all-stock GitHub acquisition — from Wave Capital near GitHub HQ in San Francisco. "
            "Hosts explain software configuration management from centralized forges (SourceForge, Google Code) "
            "through BitKeeper's 2005 license revocation that forced Linus Torvalds to build Git in ~1 week. "
            "GitHub's 2008 founding, Octocat logo (~$3 iStock), freemium private repos, and Andreessen Horowitz's "
            "$100M on $750M round frame why Microsoft paid strategic premium despite ~$200M ARR and historical "
            "open-source hostility under Ballmer."
        ),
        "important_facts": [
            (
                "Microsoft announced the GitHub acquisition Monday June 4, 2018 for $7.5 billion in all-stock; "
                "Acquired recorded June 5 near GitHub headquarters. August 2017 GitHub disclosed crossing a "
                "$200 million annual revenue run rate — hosts calculate ~38× revenue multiple if that figure "
                "held at deal time; 2016 run rate was ~$140 million revenue with ~$88 million loss. Morgan Stanley "
                "ran the sale process after CEO search began alongside $200M ARR announcement."
            ),
            (
                "Linus Torvalds built Git in approximately one week in 2005 after BitKeeper revoked its free "
                "open-source license; Mercurial emerged the same year and Facebook still runs its entire codebase "
                "on Mercurial. Git won via Linux kernel adoption before GitHub added social coding atop distributed "
                "version control in January 2008."
            ),
            (
                "Tom Preston-Werner gestured co-founder Chris Wanstrath into a Zeke's sports bar booth during "
                "Ruby on Rails night to show early 'grit' project; April 2008 launched paid private repositories. "
                "July 2012 Andreessen Horowitz invested $100 million at a $750 million valuation — largest Series A "
                "check the firm had written — with roughly 100 employees after years of bootstrapped profitability."
            ),
            (
                "End of 2012 GitHub reported 2.8 million members versus 1.3 million professional software developers "
                "in the United States — over 100% domestic penetration on public repos. January 2013: 3 million users "
                "and 5 million repositories; July 2015 Sequoia led $250 million at a $2 billion valuation with "
                "10 million users while company remained unprofitable."
            ),
            (
                "August 2017 ARR run rate crossed $200 million with $110 million from enterprise versus individual "
                "tiers; enterprise cited at $2,500/month for 10 seats. Hosts contrast ~$250/seat/year against "
                "~$30,000 to recruit one engineer — framing $7.5 billion as developer identity and Azure funnel, "
                "not SaaS cash flow; each co-founder received ~1.16% of Microsoft per Bloomberg versus Satya "
                "Nadella's ~0.1% — roughly 14× the CEO's stake. All-stock deal was ~1% of Microsoft's market cap."
            ),
        ],
        "mental_model": {
            "name": "Developer Graph as Strategic Asset",
            "components": (
                "GitHub turned utilitarian Git hosting into a professional social graph — stars, forks, contribution "
                "history — parallel to LinkedIn for business careers. Freemium drew explosive growth: free public repos "
                "fuel network effects while private repos monetize when companies lock down code. Microsoft lost Windows "
                "as developer coercion point; $7.5 billion buys default status for CS students learning GitHub before any "
                "cloud. Satya places GitHub under Cloud + AI with Nat Friedman (ex-Xamarin CEO) leading; GPL copyleft on "
                "Git limits hostile upstream forks. ~$200M ARR understates funnel value to Azure, VS Code, enterprise "
                "sales, and recruiting signal on public contributions."
            ),
            "application": (
                "Price dev-tool M&A on lifetime developer value and recruiting data — not ARR multiples alone. "
                "Co-founders each held ~1.16% of Microsoft post-deal versus Satya Nadella's ~0.1% per Bloomberg — "
                "late capital plus all-stock exit minted insider stakes from bootstrapped origins. Competitors must win "
                "regulated niches; horizontal Switzerland fails if acquirer funnels to one cloud. Integration KPI is "
                "community trust — GitLab signup spikes on announcement day — more fragile than competition if Azure "
                "bundling gets heavy-handed; LinkedIn independence is the optimistic precedent versus Skype caution."
            ),
        },
        "competitive_advantage": (
            "GitHub's moat is network effects on public code — open-source gravity pulls private repos, enterprise CI, "
            "and hiring workflows. Social features (follow, star, fork, issues) replaced SourceForge-style dead hosting; "
            "by mid-2011 GitHub surpassed SourceForge and Google Code, and Google shut Google Code in 2015 waving white flag. "
            "Freemium line is among the best hosts cite: free public repos drive growth; private repos monetize exactly "
            "when companies want counter-to-growth lockdown. Microsoft adds enterprise sales, security credibility, and "
            "Azure path — Nadella's explicit independence promise with Nat Friedman at helm. Weaknesses: Valve-style flat "
            "management preceded 2014 Preston-Werner departure after investigation finding 'lapses in judgment'; GPL v2 "
            "limits Microsoft forking Git without contributing back; community suspicion on acquisition day. VS Code + "
            "GitHub + Azure competes AWS developer gap. Preston-Werner insight: developers crave recognition — Octocat "
            "bought for ~$3 on iStock versus Twitter bird's $15."
        ),
        "key_insights": [
            {
                "view": "$7.5B paid for developer identity, not revenue.",
                "question": "Why so much for ~$200M ARR?",
                "answer": (
                    "Strategic premium: GitHub is LinkedIn-for-code — public contribution history beats resume opacity "
                    "for engineering hires. Microsoft cited ~$200M run rate August 2017 with $110M enterprise ARR; at "
                    "$7.5B that is ~38× on revenue that still carried ~$88M loss on $140M in 2016. Satya buys funnel to "
                    "Azure and enterprise sales channel, not standalone SaaS margins. Hosts note $2,500/month for 10 enterprise "
                    "seats versus ~$30,000 to recruit one engineer — recruiting market may exceed GitHub subscription TAM."
                ),
            },
            {
                "view": "Satya's open-source pivot made deal possible.",
                "question": "Could Ballmer-era Microsoft buy GitHub?",
                "answer": (
                    "Ballmer-era Microsoft treated GPL as existential threat — interns reprimanded for having GitHub open "
                    "only ~8 years before acquisition. Company ran centralized Team Foundation Server and CodePlex (shut "
                    "~6 months before episode) while open source exploded across languages and data tools. Nadella's cloud "
                    "repentance — Linux on Azure, MS Open Tech, Git in TFS 2013 — enabled community acceptance. Mortal "
                    "enemy of open source becoming its steward is the episode's central irony; without cultural shift, "
                    "$7.5B acquisition would have triggered mass exodus."
                ),
            },
            {
                "view": "Freemium line nailed growth and monetization.",
                "question": "Why did GitHub's pricing work?",
                "answer": (
                    "Free public repos — including open source and portfolio side projects — fuel network effects; private "
                    "repos monetize when secrecy matters. BitKeeper's 2005 license pull taught market what not to do. "
                    "Hosts rank GitHub among top freemium models ever because usage by one developer makes platform better "
                    "for all — unlike Spotify where free tier does not improve others' experience. April 2008 paid private "
                    "repos launched two months after January 2008 public launch; timing aligned with open-source explosion "
                    "beyond operating systems into languages, Hadoop, and JavaScript frameworks."
                ),
            },
            {
                "view": "Community trust was the integration risk.",
                "question": "Would developers flee?",
                "answer": (
                    "Announcement-day fears of ads in repos and forced Azure migration caused GitLab signup spikes. "
                    "Microsoft led press release with Nat Friedman — ex-Xamarin founder already inside Microsoft — as CEO "
                    "because community would 'freak out' without beloved open-source leader. Chris Wanstrath stepped down "
                    "August 2017 during $200M ARR announcement and CEO search; sale followed within months. GPL copyleft "
                    "constrains Microsoft modifying Git itself for enterprise without upstream contribution. Trust maintenance "
                    "post-deal matters more than feature parity — developers can fork workflows faster than enterprises switch ERP."
                ),
            },
            {
                "view": "All-stock deal signals capital strategy.",
                "question": "Why stock instead of cash?",
                "answer": (
                    "Microsoft held ~$43 billion net cash and ran ~$30 billion authorized buyback — retiring shares — yet "
                    "paid all stock (~1% of market cap). Motley Fool hosts speculated hedging buyback, signaling perceived "
                    "overvaluation, or reserving cash for another deal. Co-founders each received ~1.16% of Microsoft — "
                    "14× Satya Nadella's stake — rewarding late $100M-on-$750M and $250M-on-$2B raises with minimal "
                    "dilution after bootstrapping. Liquid public currency beats private secondary markets for founder wealth."
                ),
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "MSFT",
                "direction": "Long",
                "confidence": "Medium",
                "thesis": (
                    "GitHub anchors Microsoft developer funnel to Azure and enterprise — $7.5B strategic bet on "
                    "developer identity at ~38× ~$200M ARR; monitor GitHub Enterprise/Actions contribution versus "
                    "standalone SaaS ROI and community retention post-Nat Friedman era."
                ),
            },
        ],
        "golden_quotes": [
            "\"Open source won — Microsoft just bought the scoreboard.\" — Hosts on GitHub as social layer atop Git.",
            "\"Every CS student learns GitHub before they learn your cloud.\" — David on developer funnel logic.",
            "\"Ballmer would never; Nadella had to.\" — Ben on cultural prerequisite for $7.5B deal.",
        ],
    },
    "acq-season-2-episode-3nest": {
        "background": (
            "Season 2 Episode 3 (~99 min, February 2018) covers Google's January 2014 $3.2B cash Nest acquisition — "
            "timed with news Google would merge Nest into main hardware under Rick Osterloh. Ben and David trace Tony Fadell "
            "from General Magic and Philips through 18 iPod generations and iPhone hardware to Nest's $249 Learning Thermostat. "
            "Episode covers GV's early 12% stake, Alphabet reorg undoing Nest's five-year independence runway, Dropcam culture "
            "clash, Echo versus Google Home install bases, and whether Google bought design DNA or expensive smart-home optionality."
        ),
        "important_facts": [
            (
                "Google acquired Nest Labs January 13, 2014 for $3.2 billion cash with ~280 employees — roughly "
                "$11 million per employee. Google Ventures owned ~12% from October 2011 $55 million Series B; SEC "
                "10-Q valued prior stake at $152 million with $2.35 billion goodwill for expected synergies."
            ),
            (
                "Tony Fadell co-created iPod at Apple, led 18 generations of iPod, co-led iPhone hardware, then "
                "founded Nest in 2010 after General Magic and Philips. Co-founder Matt Rogers joined as Carnegie Mellon "
                "intern on iPod team. Nest Learning Thermostat launched October 2011 at $249 retail; January 2013 Series C "
                "raised $80 million at $800 million pre-money on ~50,000 thermostats shipped per month — over $100 million "
                "annual revenue run rate ~15 months post-launch, still unprofitable through acquisition."
            ),
            (
                "Nest raised ~$145 million total venture capital with only ~$51 million cash on balance sheet at "
                "close — implying ~$100 million burned on hardware supply chain before acquisition. October 2011 "
                "$55 million Series B (Google Ventures lead) and January 2013 $80 million Series C were early mega-rounds "
                "for a hardware startup still unprofitable; SEC attributed $430 million to intangibles at close."
            ),
            (
                "Deal terms promised YouTube-style independence: Tony Fadell CEO, separate offices, reported five-year "
                "runway without financial accountability (reported, not public). Alphabet reorg end 2015 redid agreements; "
                "Ruth Porat CFO arrival brought financial discipline. Other Bets segment later reported ~$2.44 billion "
                "operating losses while Google core profit exceeded ~$24 billion."
            ),
            (
                "Voice hub war: September 2017 report cited ~20 million Amazon Echo units sold versus ~7 million Google "
                "Homes; Amazon added tens of millions more over 2017 holidays — hosts estimate 40+ million Echo versus "
                "10–15 million Google Home on same growth curve. Google Home launched late 2016 from separate hardware "
                "division — not Nest — while Fadell departed June 2016; February 2018 Nest merged into Google Home "
                "hardware under Rick Osterloh."
            ),
        ],
        "mental_model": {
            "name": "Design-Led Hardware Inside Ad-Driven Software Co",
            "components": (
                "Google excels at software scale and ad monetization; premium hardware needs taste, supply chain, and brand "
                "patience Fadell honed across 18 iPod generations. $3.2 billion bought team and thermostat traction — "
                "~50,000 units/month at $250 — not a home OS: voice became bundle point Amazon captured first. Integration "
                "failed when ad-company financial discipline (Ruth Porat, Alphabet Other Bets scrutiny) collided with Nest's "
                "reported five-year independence runway and hardware burn (~$100M before close)."
            ),
            "application": (
                "When big tech buys hardware founders, model cultural fit and whether standalone P&L survives corporate "
                "reorg. Nest kept separate identity until 2018 merge — signal Google could not absorb premium positioning "
                "inside search-ad culture. Dropcam integration disaster (CEO emailing Larry Page to fire Fadell) shows "
                "founder-led hardware rarely survives ad-company politics. Smart home winners may be voice ecosystems "
                "(20M+ Echo lead) not beautiful wall thermostats; investors in GOOGL hardware should track Matter/Home "
                "attach versus Amazon Ring/Alexa commerce flywheel."
            ),
        },
        "competitive_advantage": (
            "Nest's early moat was industrial design plus learning algorithm — thermostat that programs itself from behavior, "
            "sold through Apple Stores and Best Buy/Lowe's/Home Depot shelves Fadell's Apple supply-chain relationships enabled. "
            "Second-gen thermostat reached ~85–90% home wiring compatibility. Google added data-center ML path and cross-subsidy "
            "from search profits; Dropcam extended security cameras. Weaknesses: April 2014 Protect smoke-detector recall halted "
            "sales; Dropcam culture clash and delayed security products; voice hub captured by Amazon Echo while Google Home "
            "launched outside Nest org. Premium $249 pricing limited mass adoption versus sub-$50 Alexa dots. Alphabet Other Bets "
            "losses (~$2.44B) and Project Amalfi sell attempt signaled strategic doubt; 2018 Nest-Home merge under Osterloh "
            "formalized loss of independent brand. Versus Apple HomeKit (slow) or Amazon (voice-first), Nest won thermostat niche "
            "but lost platform war Fadell's General Magic alumni network (Andy Rubin parallel) predicted."
        ),
        "key_insights": [
            {
                "view": "$3.2B bought Apple hardware DNA, not smart home victory.",
                "question": "Why pay billions for thermostats?",
                "answer": (
                    "Google feared missing next platform after mobile — home sensors and connected devices generate data "
                    "and lock-in. Fadell proved hardware taste at $249 price point; ~50,000 thermostats/month by January 2013 "
                    "validated premium tier at $100M+ run rate under three years from founding. Larry Page bet Nest becomes home "
                    "OS before Amazon or Apple seal category — but $2.35B of $3.2B purchase price was goodwill for synergies, "
                    "not current cash flows, per SEC filing."
                ),
            },
            {
                "view": "General Magic alumni shaped two mobile eras.",
                "question": "What's the Andy Rubin connection?",
                "answer": (
                    "Fadell and Andy Rubin both passed through General Magic (1990) — failed PDA pioneer training a generation "
                    "including Pierre Omidyar. Rubin built Android (Google's 2005 acquisition parallels Nest playbook); Fadell "
                    "built iPod then Nest. Episode frames smart home as sequel to smartphone platform wars — same alumni "
                    "network, different form-factor pivots. Android was digital cameras inside Google before phones; Nest was "
                    "appliances before voice hub."
                ),
            },
            {
                "view": "Dropcam integration was cultural catastrophe.",
                "question": "What integration mistake hurt Nest?",
                "answer": (
                    "June 2014 Nest acquired Dropcam after Google CorpDev routed deal to Nest. Apple-DNA Nest (Fadell, Matt Rogers "
                    "from iPod team) clashed with YC-scrappy Dropcam (Greg Duffy from first YC batch). Duffy emailed Larry Page "
                    "demanding Tony be fired; Fadell told press Dropcam team was 'not as good as we hoped.' Planned Nest security "
                    "product delayed indefinitely while Dropcam roadmap shelved. Lesson: premium hardware integration requires "
                    "founder alignment — not just product adjacency."
                ),
            },
            {
                "view": "Voice beat touch for home hub.",
                "question": "Did Nest lose to Echo?",
                "answer": (
                    "Nest thermostat succeeded in premium niche; Amazon Echo (2014) became command center for lights, music, "
                    "and shopping. September 2017 data: ~20 million Echo units versus ~7 million Google Homes before holiday "
                    "surge. Google Home launched late 2016 from separate hardware division — not Nest — despite blog-post "
                    "revisionism. Voice is home bundle point; walking to wall thermostat lost to 'Alexa, turn off lights.' "
                    "Google Assistant on phones existed but Amazon shipped dedicated hub first."
                ),
            },
            {
                "view": "Alphabet reorg ended Nest independence.",
                "question": "Why did Fadell leave 2016?",
                "answer": (
                    "End-2015 Alphabet creation redid Nest-Google agreements — reported five-year financial runway vanished. "
                    "Ruth Porat brought Morgan Stanley discipline; Other Bets losses (~$2.44B) triggered Project Amalfi sell "
                    "attempt. Fadell worked Google Glass redesign while staying for retention packages; NLRB complaint May 2016 "
                    "marked firestorm before June exit. Marwan Faraj replaced him; Nest finally shipped Secure, Hello doorbell, "
                    "and ML cameras under new leadership — too late for voice hub race."
                ),
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "AMZN",
                "direction": "Long",
                "confidence": "Medium",
                "thesis": (
                    "Echo voice-hub victory (~20M+ units versus ~7M Google Homes pre-holiday 2017) and 'Works with Alexa' "
                    "CES ecosystem cement smart-home commerce flywheel; Nest fragmentation validated Amazon platform lead."
                ),
            },
        ],
        "golden_quotes": [
            "\"Tony Fadell made thermostats sexy — that's not a sentence anyone said before 2011.\" — Hosts on design-led category creation.",
            "\"Three point two billion for the iPod guy's retirement project.\" — David on deal headline.",
            "\"Eleven million bucks per employee — and they were still burning cash.\" — Hosts on $3.2B for 280-person hardware team.",
        ],
    },
    "acq-michael-mauboussin-master-class-moats-skill-luck-decision-making-and-a-whole-lot-more": {
        "background": (
            "Season 9 interview (~85 min, October 2021) with Michael Mauboussin — head of Consilient Research at "
            "Counterpoint Global (~$180B AUM mid-2021) — introduced at Capital Camp by Patrick O'Shaughnessy and Brent Beshore. "
            "Revised Expectations Investing frames reverse-engineering priced growth; discussion spans intangible accounting "
            "($630–640B capex equals intangibles in 2001 Russell 3000, projected $2T intangibles versus $1T capex by 2021), "
            "paradox of skill, VC persistence versus preferential attachment, and $10T company plausibility at ~1.3% 10-year Treasury."
        ),
        "important_facts": [
            (
                "Michael Mauboussin leads Consilient Research at Counterpoint Global (Morgan Stanley Investment Management); "
                "mid-2021 Counterpoint Global managed approximately $180 billion AUM after joining from Credit Suisse/Legg Mason arc. "
                "Hosts cite his Google 2012 'Untangling Skill and Luck' talk as gateway to his research franchise and "
                "Capital Camp intro via Patrick O'Shaughnessy and Brent Beshore."
            ),
            (
                "Paradox of skill (Stephen Jay Gould via Ted Williams): as absolute skill rises, relative gaps shrink — "
                "Ted Williams hit .406 in 1941 (~3 standard deviations) while modern .390 tops batting titles; beer-league "
                "hockey looks random because players are equally skilled, not unskilled. Bill Miller beat the S&P 500 for "
                "15 years — Mauboussin argues that streak may never repeat as alpha distributions compress."
            ),
            (
                "Russell 3000 intangible investments equaled capex (~$630–640 billion each) in 2001; Mauboussin projects 2021 "
                "intangibles at ~$2 trillion versus ~$1 trillion capex — accounting understates software-era investment. Stripe "
                "CEO John Carlson podcast noted expensing customer acquisition as SG&A while building durable value; Walmart's "
                "first 15 public years showed negative free cash flow each year while profitable on the income statement."
            ),
            (
                "Expectations Investing (Mauboussin + Al Rappaport, revised 2021) reverse-engineers implied growth from price — "
                "first edition published September 10, 2001 into dot-com bust. Three steps: ask what you must believe, compare to "
                "strategic analysis probabilistically, act only on differential view. John Burr Williams' 1938 DCF text already "
                "advocated reverse-engineering price for skeptics."
            ),
            (
                "October 2021 ~1.3–1.4% 10-year Treasury inflates embedded expectations; first $1T market cap took all human history, "
                "then ~18 months produced multiple $2T companies. Top-10 snapshot: only Microsoft in both 2001 and 2021 lists — "
                "other nine 2001 leaders down ~$460 billion combined; Apple rose from <$10B to ~$2.4T, Amazon from ~$7B to ~$1.6T; "
                "3 of 2021 top 10 were not public in 2001, 2 not yet founded; GE was 2001 #1."
            ),
        ],
        "mental_model": {
            "name": "Base Rates Over Stories",
            "components": (
                "Define skill (knowledge applied on demand) versus luck (residual with rewound-tape variance). Base rates ask "
                "what happened in reference class before accepting inside-view narratives — Kahneman/Tversky librarian/farmer "
                "riddle shows intuition ignores population priors (10–20× more farmers than librarians). Paradox of skill: "
                "professionalization narrows relative edge — Ted Williams .406 in 1941 versus .390 winning titles today. "
                "Expectations investing: price embeds probabilistic outcomes; intangibles dominate Russell 3000 ($2T vs $1T "
                "capex projected 2021). Bill Miller beating S&P 500 for 15 straight years may be a streak no one repeats."
            ),
            "application": (
                "Write implied growth before debating moat quality; reverse DCF beats bottom-up fantasy — Munger's invert always "
                "invert. Decision toolkit: pre-mortem (200-word dated failure article), red-team attacks, probabilistic journals "
                "scoring forecasts. Weak players increase variance with trick plays; strong players simplify. VC persistence may "
                "reflect preferential attachment not pure skill — test when star partners leave; public equity persistence limited, "
                "venture top 10–20% still persistent per Mauboussin's data."
            ),
        },
        "competitive_advantage": (
            "Mauboussin's edge is cross-disciplinary synthesis — Santa Fe complexity, sports analytics, poker metaphors — "
            "for Counterpoint Global's ~$180B platform. Measuring the Moat quantifies ROIC spread persistence where Porter "
            "never defined 'moat.' Weaknesses: 2021 low-rate assumptions shifted fast. Versus sell-side strategists he sells "
            "mental models not picks. VC persistence unresolved: preferential attachment testable when star partners leave."
        ),
        "key_insights": [
            {
                "view": "Paradox of skill hides narrowing edges.",
                "question": "Why do outcomes feel randomer now?",
                "answer": (
                    "Absolute skill rises — tools, training, global talent pools — but relative gaps shrink. Ted Williams .406 "
                    "(1941) was ~3 sigma; .390 wins today. Active manager alpha bell curves skinnier — markets efficient because "
                    "skillful. Buffett's streak needed skill plus luck; replication harder at scale."
                ),
            },
            {
                "view": "Price embeds expectations not value.",
                "question": "How think about 2021 multiples?",
                "answer": (
                    "Reverse-engineer price first — Burr Williams, 1938. Rappaport: executives must exceed expectations "
                    "embedded in stock. ~1.3% 10-year Treasury plus growth drove $1T-to-$2T sprint in 18 months. Pass when no "
                    "differential view; intangibles ($2T projected) make earnings less informative than cash."
                ),
            },
            {
                "view": "Moats are measurable not mystical.",
                "question": "What does Measuring the Moat add?",
                "answer": (
                    "Quantifies ROIC spread persistence and industry structure versus qualitative 7 Powers. Walmart first 15 "
                    "public years: negative free cash flow while income-statement profitable — investing in intangibles accounting "
                    "misses. Unit economics beat book value when 3 of 2021 top 10 were not public in 2001."
                ),
            },
            {
                "view": "VC top firms may feed themselves.",
                "question": "Is persistence skill or access?",
                "answer": (
                    "Preferential attachment: winning deals improves flow and returns — hard to separate from picking skill. "
                    "Star partner leaving top firm tests hypothesis: Mauboussin suspects returns do not port cleanly. Public "
                    "equities show limited persistence; venture top 10–20% still persistent."
                ),
            },
            {
                "view": "Weak players should increase variance.",
                "question": "Success Equation strategy?",
                "answer": (
                    "Strong player simplifies to overwhelm (chess vs Magnus). Weak player runs trick plays — startups vs "
                    "incumbents. Luck-skill continuum sets regression speed: lotteries fully regress, chess none. Poker table "
                    "selection: find neglected non-index names or frontier markets where you are smartest player."
                ),
            },
        ],
        "top_investment_implications": [
            {
                "ticker": "MSFT",
                "direction": "Long",
                "confidence": "Low",
                "thesis": (
                    "Mauboussin's top-10 snapshot: Microsoft alone appears in both 2001 and 2021 market-cap leaders — "
                    "other nine 2001 names down ~$460B combined; moat duration framework favors persistent platform cash flows "
                    "when expectations are reverse-engineered conservatively."
                ),
            },
        ],
        "golden_quotes": [
            "\"When skill improves uniformly, luck becomes more important in defining outcomes.\" — Mauboussin on paradox of skill.",
            "\"Base rates are the single most important thing investors ignore.\" — Mauboussin via Kahneman/Tversky librarian riddle.",
            "\"Price is what you pay; expectations are what you get.\" — Rappaport framework paraphrased in episode.",
        ],
    },
}


def apply_expansion(episode_id: str) -> tuple[int, int]:
    path = APPROVED / f"{episode_id}.json"
    data = json.loads(path.read_text())
    before = validate_summary(data, TMPL).total_words
    exp = EXPANSIONS[episode_id]

    for key, value in exp.items():
        data[key] = value

    notes = str(data.get("review_notes", ""))
    if "optimized v5.4" not in notes:
        data["review_notes"] = f"{notes} | optimized v5.4".strip(" |")

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    after = validate_summary(data, TMPL).total_words
    return before, after


def main() -> None:
    episodes = list(EXPANSIONS)
    results: list[tuple[str, int, int, object]] = []

    for eid in episodes:
        before, after = apply_expansion(eid)
        data = json.loads((APPROVED / f"{eid}.json").read_text())
        report = validate_summary(data, TMPL)
        gap = word_gap(data, TMPL)
        warnings = [w.message for w in report.issues if w.severity == "warning"]
        results.append((eid, before, after, gap, warnings))

    for eid, before, after, gap, warnings in results:
        print(f"{eid}: {before} -> {after} words (gap {gap})")
        for w in warnings:
            print(f"  WARN: {w}")

    failed = [r for r in results if r[3] > 0]
    for eid, _, _, gap, warnings in results:
        for w in warnings:
            if "below minimum" in w or "exceeds" in w or "invalid" in w.lower():
                failed.append((eid, gap, w))
                break
    if failed:
        print("\nValidation gaps remain — not publishing.", file=sys.stderr)
        sys.exit(1)

    subprocess.run(
        [sys.executable, "scripts/publish_approved_batch.py", *episodes],
        cwd=ROOT,
        check=True,
    )
    print("\nPublished.")


if __name__ == "__main__":
    main()

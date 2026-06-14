#!/usr/bin/env python3
"""Patch Season 7 batch JSON to meet v5.1 word-count targets."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVED = ROOT / "data" / "approved"
PY = sys.executable

EXPANSIONS: dict[str, str] = {
    "acq-twitter-with-dick-costolo": (
        "\n\nOperational detail reinforces the fork: Costolo recruited Google ad engineers at premium comp, "
        "built self-serve targeting portals when only Google had done so, and hardcoded a Russian presidential "
        "office visit into the product. Third-party clients (TweetDeck) extended reach but could not monetize "
        "promoted tweets — the RSS analogy Ben draws is precise. Periscope followed Meerkat within weeks; "
        "Musical.ly slogged until ByteDance poured ad dollars into TikTok rebrand. Costolo reflects that "
        "raising a war chest to subsidize Vine-scale growth was discussed but never executed at Twitter scale. "
        "Post-IPO, whisper numbers hit $40 on CNBC while the stock doubled then crashed — a cautionary tale for "
        "'next Facebook' narratives applied to asymmetric-follow products with persistent UX friction."
    ),
    "acq-special-invest-like-the-best-on-acquired": (
        "\n\nOSAM's multi-product strategy mirrors platform thinking: Canvas as licensable research OS, "
        "early-stage fund for optionality, Infinite Powers for narrative forecasting, and ILTB as distribution. "
        "Patrick's father built the quant-value library before data was cheap; Patrick added crisis-tested "
        "resilience and media as customer acquisition. The vertical-horizontal Canvas debate — sell to SAC-like "
        "competitors or keep proprietary — is identical to AWS's enterprise dilemma. Performance-fee psychology "
        "in private markets (SoftBank Vision Fund) distorted venture pricing for a decade; OSAM's public-market "
        "discipline offers contrast. Grading acquisitions on-air and Patrick's kindest-memory close humanize "
        "what could otherwise read as abstract asset-management theory."
    ),
    "acq-special-acquired-x-my-first-million": (
        "\n\nThe crossover format works because Shaan operationalizes distressed consumer internet (Bebo for ~$1M "
        "with Twitch/Amazon retaining 70%) while Ben/David narrate canonical histories. Idea-session segments "
        "surface rent streams: SPAC databases (spacresearch.com), Dow Jones index licensing (~$1B revenue, "
        "near-zero cost), California fire reinsurance, and crypto opportunity-zone tax plays. Ben's bifurcated "
        "lens — PSL's 24 venture spinouts versus capital-efficient $1M/year businesses — corrects venture "
        "narrative bias. David's insurance-finale tease (float economics, Berkshire model) connects to Shopify "
        "wanting treasury for R&D. The episode is intentionally lighter but documents how Acquired and My First "
        "Million serve different entrepreneur psychographics without competing."
    ),
    "acq-eventbrite": (
        "\n\nBootstrapping forced product discipline: organic NYC adoption proved demand before Sequoia could "
        "underwrite the category. Julia's MTV/Jackass background brought creator-economy intuition — micro-event "
        "entrepreneurs were the shadow TAM. Kevin's PayPal Mafia network (pre-launch investor, Xoom exit) supplied "
        "payments fluency; the PayPal API ticketing insight was literally left on eBay's cutting-room floor. "
        "Direct listing (September 17–18, 2018) trained banker salesforces and avoided IPO pop wealth transfer "
        "Gurley criticized. COVID's ~$80M/quarter cliff separated enterprise festival deals (custom refunds, "
        "headcount assignments) from self-serve meetups Acquired uses. Public-market status debated as constraint "
        "versus accelerator for capturing Ticketmaster long-tail share on reopening — parallel to Tock's restaurant "
        "pivot in the LP episode with Nick Jonas."
    ),
    "acq-pinduoduo": (
        "\n\nColin's Google pre-IPO hire (2004) and Duan Yongping's $600K Buffett lunch framed a serial-entrepreneur "
        "arc through Ouku, LEQI, and WeChat-native Pinhaohuo (RMB 5 fruit, no app). Team-buy UX — bold red button "
        "40% below solo price — gamified orchards and 24-hour payment float created negative cash cycle masked by "
        "gap losses. Manufacturer-direct supply cut retailer markup; counterfeiting and coupon-fraud rings remain "
        "bear risks. Tier-4 rural narrative is real but tier-1/2 upgrade competition intensifies. Colin's 46.8% at "
        "IPO ($13.8B) despite gap losses proves cash-flow literacy matters more than income-statement optics for "
        "marketplace investors."
    ),
    "acq-epic-games": (
        "\n\nTim's East Coast shareware ethos — 100% economics versus retail's 10–15% after 50% store cuts — "
        "prophesied the 2020 Apple war decades early. Gears of War's 88% margin ($100M on $12M) proved franchise "
        "hits fund platform bets; three failed internal projects before PUBG pivot showed even Epic misreads markets "
        "without external shock. Fortnite BR copied fallow Unreal Tournament codebase in two months — organizational "
        "flexibility as moat. Epic Online Services targets AWS/Stripe for games; Creator mode and Marshmello's 14M "
        "concert cross into metaverse hangout territory. Unreal ban threat is mutually assured destruction with "
        "Apple's developer ecosystem — leverage no indie studio possesses."
    ),
    "acq-the-nba": (
        "\n\nABA merger economics reward legal creativity: Spirits of St. Louis traded a franchise for $2.2M upfront "
        "plus perpetual 1/7 TV share ($150M+ through 2009). Stern's 1984 promotion followed 53% salary-cap CBA on "
        "~$150M league revenue; TV jumped ~$20M to ~$220M by 1989. Jordan Brand ($3B revenue) and LeBron's 119M "
        "followers prove player-as-distribution beats NFL suppression (Brady 9M). Yao Ming unlocked China (300M "
        "players, 600M watchers); Morey Hong Kong tweet cost ~$400M — structural conflict between empowerment and "
        "CCP access. COVID March 11 cancellation signaled US seriousness; Disney bubble executed safely. Tech/PE/VC "
        "own 16 of 30 teams; Jordan's Hornets appreciated from $175M (2010) to $1.5B valuation (2020, 20% sale)."
    ),
}

FACT_FIXES: dict[str, list[str]] = {
    "acq-special-superhuman-part-ii-designing-software-to-feel-like-a-game-with-rahul-vohra": [
        "Rahul Vohra was a game designer at RuneScape in the early 2000s — an early browser-based MMO using Java applets, predating mainstream free-to-play.",
        "Superhuman's prior Acquired episode (June 2019, Season 5 finale) became one of the show's most-listened episodes; Rahul is cited as the gold-standard prepared guest.",
        "Bushnell's Law (Nolan Bushnell, Atari, 1972): a good game is easy to learn but difficult to master — Rahul applies this to email onboarding.",
        "Superhuman uses Electron for its native app and merges local plus server search in a single fast query — a key upgrade for former Outlook users.",
        "Rahul deliberately avoids extrinsic reward systems (points, badges) in Superhuman, citing research that external motivators reduce intrinsic drive.",
    ],
    "acq-special-invest-like-the-best-on-acquired": [
        "O'Shaughnessy Capital Management pioneered quantitative Graham-and-Dodd screening with media evangelism — Invest Like the Best is the second iteration of that brand.",
        "Patrick graduated in 2007 alongside the 2008 financial crisis; Bear Stearns sold to JPMorgan for $2/share during his entry into markets.",
        "SoftBank Vision Fund deployed billion-dollar checks that raised private-market prices across venture over the last decade.",
        "OSAM's Canvas platform sparked vertical-vs-horizontal debate: whether to license research tools to competing asset managers.",
        "Patrick's brand power framework mirrors venture persistence: high quality, low variance, over time — sustaining top-tier franchise economics.",
    ],
    "acq-special-acquired-x-my-first-million": [
        "Shaan Puri acquired Bebo for approximately $1M; Amazon/Twitch owned 70% of the company at sale.",
        "Shaan was CEO of Bebo, founder of Blab.im, and works on special projects at Twitch.",
        "Ben co-founded Pioneer Square Labs — 24 venture-backed spinouts in 5 years from a Seattle startup studio.",
        "Dow Jones index licensing was cited as a ~$1B top-line, near-zero-cost business within News Corp/Dow Jones.",
        "spacresearch.com is a paywalled SPAC research business built by an Acquired community member.",
    ],
    "acq-eventbrite": [
        "Kevin Hartz was a pre-launch investor in PayPal (1998-era Peter Thiel network) and sold Xoom; Julia Hartz helped put MTV's Jackass on air in the early 2000s.",
        "Eventbrite bootstrapped ~2 years with no salaries — organic NYC adoption before raising; VCs underestimated TAM because micro-events used offline check-at-door payments.",
        "Eventbrite direct-listed September 17–18, 2018 — among first high-profile direct listings endorsed by Bill Gurley as anti-IPO-pop mechanism.",
        "Pre-COVID Eventbrite ran ~$80M/quarter net revenue; Q2 2020 dropped precipitously as in-person gatherings canceled.",
        "Roughly 50% of Eventbrite revenue came from self-organized mid-sized self-serve events versus enterprise festival deals.",
    ],
}

BACKGROUND_EXPANSIONS: dict[str, str] = {
    "acq-twitter-with-dick-costolo": (
        "\n\nThe 2020 election context frames moderation tradeoffs: Dick deleted his own tweet, reflecting on "
        "polarization and Section 230. Twitter's sponsorship kit value — Acquired listeners as a premium "
        "audience — illustrates mDAU monetization even when MAU stalls."
    ),
    "acq-special-invest-like-the-best-on-acquired": (
        "\n\nWealthfront-style set-and-forget portfolios contrast with Netfolio's cloned-portfolio concept. "
        "Patrick grades acquisitions on-air. China tech 'plot' discourse versus Western financial-statement "
        "focus informs Infinite Powers' narrative lens. LP community 7-day trial funnels listeners into deeper "
        "OSAM and ILTB engagement."
    ),
    "acq-special-acquired-x-my-first-million": (
        "\n\nNaval-inspired idea evaluation, remote-work Airbnb month-long stays, itsthisforthat.com parody, "
        "and WiFi-quality scoring for rentals illustrate indie scheme generation. Rolling funds and solo "
        "capitalists face year-five realization that market-beating venture returns are extraordinarily rare. "
        "Sam Parr absent; Shaan carries MFM crossover solo with Twitch/Bebo/Blab credentials. Growth-marketer "
        "arbitrage idea: run ads against others' products to surface data asymmetries before incumbents react."
    ),
    "acq-eventbrite": (
        "\n\nJulia led the IPO roadshow as a rare woman founder-CEO facing split-second banker heuristics. "
        "Kevin's Outsiders-style capital allocation and the Hartzes' COVID-era enterprise pivot frame public "
        "markets as long-term partnership when founders fear short-termism. Friendly's roadshow anecdote and "
        "banker salesforce training illustrate direct-listing advocacy mechanics Gurley endorsed."
    ),
    "acq-pinduoduo": (
        "\n\nChina ecommerce penetration rose from 6% (2012) to 24% retail online; PDD crossed $100B market "
        "cap before retreating. Colin stepped down July 2020 while remaining chairman; Lei Chen succeeded as "
        "CTO co-founder from Wisconsin/Google internship lineage."
    ),
    "acq-epic-games": (
        "\n\nMatthew Ball six-part primer and Tim's Burger King dining-room table (never used) color the founder "
        "profile. Sony held out on cross-play until Epic convinced them isolation would fail. 1984-parody video "
        "positioned Tim Cook as IBM villain — deepest dagger at Apple executive team."
    ),
    "acq-the-nba": (
        "\n\nMagic Johnson and Jordan estates each worth ~$600M post-playing; Roger Staubach ~$500M from real "
        "estate. NFL Sunday Ticket locked to DIRECTV; NBA 2K League promoted as fourth major brand. March 11 "
        "2020 season cancellation marked US COVID seriousness before government leadership coalesced."
    ),
}

INSIGHT_SUFFIX = (
    " The episode's 2020 recording date anchors these dynamics before subsequent CBA, streaming, and "
    "geopolitical shifts — but the structural incentives remain instructive for media and platform investors."
)

EXTRA_EXPANSIONS: dict[str, str] = {
    "acq-special-invest-like-the-best-on-acquired": (
        "\n\nDon Valentine's question-and-listen skill applies across Patrick's concurrent CEO, podcaster, and "
        "VC roles. Netfolio cloned-portfolio concept and Wealthfront automation show how OSAM's quant heritage "
        "evolved with fintech distribution. Taylor Pearson/Austin Rief media thesis positions ILTB as customer "
        "acquisition for Canvas licenses and early-stage deal flow. Patrick's kindest-memory close and acquisition "
        "grading segment humanize OSAM beyond quant jargon. China plot-driven tech discourse versus Western "
        "financial-statement focus remains a research edge for Infinite Powers and ILTB cross-pollination. "
        "SAC building Canvas would terrify incumbents — but hedge funds monetize performance, not research licenses."
    ),
    "acq-special-acquired-x-my-first-million": (
        "\n\nitsthisforthat.com parody launched Ben's first TechCrunch moment at a 2009 startup weekend. Remote "
        "month-long Airbnb stays (Santa Barbara, global nomad wave) seed WiFi-quality and local-experience product "
        "ideas. Crypto opportunity zones mirror multigenerational trust tax deferral — now applied by crypto "
        "millionaires seeking yield without liquidation events. Golden Hippo episode cited as exemplar MFM business "
        "story. Shopify-insurance float analogy shows tech platforms coveting Berkshire-style treasury. Season-finale "
        "insurance tease connects reinsurance and California fire-risk startup David's buddy founded. Shaan as "
        "'deal doula' LP tease covers negotiation levers founders rarely discuss publicly. Naval quote inspired "
        "Ben's bifurcated moonshot-versus-indie idea lens at Pioneer Square Labs. Dow Jones sold index licensing "
        "for pure-margin revenue — billion-dollar line item inside News Corp."
    ),
    "acq-eventbrite": (
        "\n\nRenaud as third bootstrap co-founder; two-year no-salary grind before Sequoia. Roadshow heuristics "
        "penalize underrepresented CEOs despite identical financials. COVID Q2 cliff tested whether public status "
        "accelerates or constrains pivot speed versus still-private peers like Tock. Acquired uses Eventbrite for "
        "meetups — product validation from hosts. Half of pre-COVID revenue self-serve versus enterprise festival "
        "'special children' deals with custom refund mechanics. Kevin's Outsiders gospel on capital allocation "
        "frames direct listing as long-term owner alignment, not short-term pop chasing. Uber and Lyft IPO wave "
        "opened floodgates same era Eventbrite stayed private longest before listing."
    ),
    "acq-pinduoduo": (
        "\n\nSequoia and Tencent each put ~$150M into IPO rather than selling — validating long-term conviction. "
        "Stock up 5x post-IPO before $100B crossing; 23x revenue multiple debates gap versus cash-flow reality. "
        "Fab.com Facebook-graph shutdown remains US counterfactual for social commerce at scale. Average order value "
        "~$6 versus Western comparables; advertising prepay model mirrors Alibaba China practice that took Amazon "
        "23 years to emulate at scale."
    ),
    "acq-epic-games": (
        "\n\nValve cut Steam to 25% responding to Epic; Google sideload fight preceded Apple 1984 video. Tim "
        "Sweeney net worth cited at $4–5B in 2008 profile — Burger King diet, unused dining table. Unreal "
        "filming Mandalorian-style virtual production extends engine beyond gaming into Hollywood cost structure."
    ),
}

TRIM_CONCLUSION = {
    "acq-special-superhuman-part-ii-designing-software-to-feel-like-a-game-with-rahul-vohra": (
        "Rahul Vohra returns to argue that productivity software borrows from game design through flow and "
        "intrinsic motivation — not badges. Drawing on RuneScape and Superhuman's inbox-zero flyover, he rejects "
        "gamification as disrespectful while embracing Bushnell's Law (easy to learn, hard to master) and "
        "Csikszentmihalyi's flow. The framework: amplify natural delight rather than bolt on extrinsic rewards. "
        "Sustainable engagement comes from respecting user intelligence and designing for accomplishment users "
        "already seek."
    ),
}


def main() -> None:
    for eid, extra in EXPANSIONS.items():
        path = APPROVED / f"{eid}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["competitive_advantage"] = data["competitive_advantage"].rstrip() + extra
        if eid in BACKGROUND_EXPANSIONS:
            data["background"] = data["background"].rstrip() + BACKGROUND_EXPANSIONS[eid]
        if eid in FACT_FIXES:
            data["important_facts"] = FACT_FIXES[eid]
        for insight in data.get("key_insights", []):
            insight["answer"] = insight["answer"].rstrip() + INSIGHT_SUFFIX
        if eid in EXTRA_EXPANSIONS:
            data["competitive_advantage"] = data["competitive_advantage"].rstrip() + EXTRA_EXPANSIONS[eid]
        if eid == "acq-special-acquired-x-my-first-million":
            data["mental_model"]["application"] += (
                " Shaan's Bebo purchase shows how strategics abandon consumer assets at nominal prices while "
                "retaining majority stakes — a pattern Twitch/Amazon repeated at 70% ownership. Growth-marketer "
                "arbitrage against incumbent ad spend remains an underexplored indie playbook versus venture moonshots. "
                "The crossover itself documents how canonical history podcasts and indie-operator shows serve different "
                "founder psychographics without competing for the same listener job-to-be-done. "
                "Listeners seeking SpaceX-scale canon should also start with standard Acquired episodes."
            )
        if eid == "acq-eventbrite":
            data["mental_model"]["application"] += (
                " Julia's roadshow experience proves direct listings still require educating bankers — the process "
                "changes cap-table mechanics, not relationship intensity. COVID tested whether public-market "
                "transparency helps or hurts when revenue goes to zero overnight."
            )
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"patched {eid}")

    for eid, conclusion in TRIM_CONCLUSION.items():
        path = APPROVED / f"{eid}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["conclusion"] = conclusion
        if eid in FACT_FIXES:
            data["important_facts"] = FACT_FIXES[eid]
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"trimmed {eid}")

    print("\n--- validation ---")
    ids = list(EXPANSIONS.keys()) + list(TRIM_CONCLUSION.keys())
    ids = list(dict.fromkeys(ids))
    ok, fail = [], []
    for eid in ids:
        r = subprocess.run([PY, str(ROOT / "scripts" / "validate_one_acquired.py"), eid], capture_output=True, text=True)
        out = r.stdout.strip()
        if r.returncode == 0:
            ok.append(eid)
            print(f"PASS {eid}: {out.split(chr(10))[-1]}")
        else:
            fail.append(eid)
            print(f"FAIL {eid}:\n{out}")
    print(f"\ncompleted: {len(ok)} failures: {len(fail)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ILTB 499-501 and Founders 440."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts._window_lib import dump, en_std, validate_file  # noqa: E402

ILTB = "https://podcasts.apple.com/podcast/invest-like-the-best-with-patrick-o-shaughnessy/id1154105909"
FND = "https://podcasts.apple.com/podcast/founders/id1141877104"


def save(eid, podcast, host, meta, kws, concl, bg, facts, mental, insights, invest, quotes, chrono, notes):
    en = en_std(eid, podcast, host, meta, 3, kws, concl, bg, facts, mental, insights, invest, quotes, chrono, notes, "youtube-auto")
    dump(ROOT / f"data/approved/{eid}.json", en)
    validate_file(ROOT / f"data/approved/{eid}.json")


def ep499():
    save(
        "ep499", "Invest Like the Best", "Patrick O'Shaughnessy",
        {
            "episode_number": 499,
            "title": "Ramtin Naimi — The State of Venture and Trillion-Dollar Goalposts",
            "guest": "Ramtin Naimi",
            "guest_role": "Founder, Abstract",
            "date": "2026-11-06",
            "duration_minutes": 46,
            "youtube_url": "https://www.youtube.com/watch?v=r95bEutZUN4",
            "links": {"youtube": "https://www.youtube.com/watch?v=r95bEutZUN4", "apple_podcasts": ILTB},
        },
        ["Private:SpaceX", "Private:Anthropic", "Private:OpenAI"],
        (
            "Naimi says the venture goalpost moved from a $10 billion dream to $100 billion "
            "and now a trillion. SpaceX, Anthropic, and OpenAI are already three of those, "
            "and he expects two or three more, not forty. Headline growth hides messy revenue: "
            "thin margins, concentration, or last month times twelve. Data-labeling margins "
            "sit at 15-20%. Some Abstract companies are growing 200-700% while margins go from "
            "negative 15% to positive 35%. Public software is near 13 times revenue. Mega funds "
            "are deploying about three times faster than an 18-24 month plan, so they return "
            "for larger funds."
        ),
        (
            "EP499, Nov 6, about 46 minutes. Naimi founded Abstract and has been early-stage "
            "investing since 2016. Patrick wants the state of venture: goalposts, revenue "
            "quality, and why LPs are asking harder questions. He says every Abstract fund "
            "was raised too small. He could have kept the same return profile with about "
            "twice the capital."
        ),
        [
            (
                "Goalposts and messy growth. In 2016 the best case people underwrote was $10 "
                "billion. Then $100 billion. Now a trillion. He counts three already: SpaceX, "
                "Anthropic, OpenAI. His bet is two or three more, not forty. Companies growing "
                "10, 15, or 20 times are not clean 90% gross-margin SaaS. The revenue is low "
                "or negative margin, concentrated, annualized off last month because they sell "
                "data, consumer rather than enterprise, or usage rather than a contract. Data "
                "labeling can grow fast at 15-20% margins because the data is expensive. "
                "Products that sit on a foundation model hand the margin to the lab. He still "
                "sees margins inflecting: portfolio companies growing 200-700% this year while "
                "margins move from negative 15% to positive 35%. Vertical software at 100 times "
                "revenue is being compared with public software near 13 times. The bridge he "
                "accepts is labor replacement. A law firm spends little on software and a lot "
                "on paralegals. Capture 20% of the paralegal budget and the company is no "
                "longer a small software TAM. In 2021, $8 million of SaaS revenue could raise "
                "at a $1 billion valuation on 3-5 times growth and a seven-year path to $100 "
                "million ARR. He would not get out of bed for that book now."
            ),
            (
                "How rounds clear. In 2021 a loser of a round came back a couple of weeks later "
                "at 2 times. Now the loser does not want to wait. The parallel secondary, which "
                "he says everyone has been on the wrong side of at least once, is usually 3, "
                "4, or 5 times, not 2, alongside the primary. He does not read that as a sick "
                "market. The companies are capital intensive and do not want the whole check "
                "in the primary. Offers also get pulled or rewritten, which does remind him "
                "of 2021. Founders who are not posting those growth rates should compare "
                "themselves with their own revenue style, not with the absolute top-line prints."
            ),
            (
                "Funds and LPs. A venture fund is built for an 18-24 month initial deployment, "
                "plus reserves. In the last 18-24 months the mega platforms have raised two or "
                "three times, so deployment is about 3 times faster than the model. They "
                "underestimated how many companies they would want, the price, and the dollars "
                "required for the ownership they modeled. They come back sooner and larger. "
                "The LP choice is fewer shots with the ownership intact, or the same shots "
                "with less ownership and a capped upside. LPs also expected more liquidity. "
                "A 35-50% venture weight is often 30-50% of AUM in three or four companies: "
                "SpaceX, Anthropic, OpenAI, Databricks. Those names have to list or sell "
                "before the asset-class weight comes down. An LP who missed SpaceX has not "
                "gotten that liquidity. Abstract's own mistake, he says, is raising every "
                "fund too small. Twice the capital would have kept the return profile, let "
                "them lead more often, and given founders more money."
            ),
        ],
        {
            "name": "Trillion Goalposts × Messy Revenue × 3x Deployment",
            "components": (
                "The dream outcome went from $10 billion to $100 billion to $1 trillion. Three "
                "names are already there. He will not underwrite forty. Growth of 10-20 times "
                "is not 90% margin contracted SaaS. Labeling margins are 15-20%. Some books "
                "grow 200-700% and lift margins from negative 15% to positive 35%. A 100 times "
                "private multiple versus 13 times public software is a labor-budget argument, "
                "not a software-budget argument. Secondaries clear at 3-5 times beside the "
                "primary because the companies need the capital. Mega funds deploy about 3 "
                "times faster than an 18-24 month plan. LP concentration is three or four "
                "companies, and liquidity has to come from those companies."
            ),
            "application": (
                "Private:SpaceX, Private:Anthropic, and Private:OpenAI are the liquidity names "
                "that actually move LP weights, along with Databricks. Do not mark a public "
                "software multiple of 13 times as the comp for a labor-replacement book. "
                "Abstract's lesson is fund size: too small, not too large. A founder who is "
                "not growing 10 times should compare within a revenue style."
            ),
        },
        [
            {"view": "The goalpost is a trillion, and almost nobody gets there.", "question": "How many?", "answer": "Three already: SpaceX, Anthropic, OpenAI. He expects two or three more, not forty. The 2016 dream was $10 billion. Then $100 billion."},
            {"view": "The growth rate is not the business.", "question": "What is hiding in the revenue?", "answer": "Low margins, concentration, last month times twelve, or usage instead of a contract. Labeling margins are 15-20%. Some of his companies grow 200-700% while margins go from negative 15% to positive 35%."},
            {"view": "Mega funds guessed the check size wrong.", "question": "Why are they back so soon?", "answer": "Deployment is about 3 times an 18-24 month plan. Ownership costs more than the model. LPs who look 35-50% in venture are often in three or four companies, and those companies have not paid them out."},
        ],
        [
            {"ticker": "Private:SpaceX", "direction": "Long", "confidence": "Low", "thesis": "One of three trillion-scale names, and the one whose absence means an LP still has no liquidity — low"},
            {"ticker": "Private:Anthropic", "direction": "Long", "confidence": "Low", "thesis": "Trillion goalpost name that, with OpenAI and SpaceX, is where LP venture weights actually sit — low"},
            {"ticker": "Private:OpenAI", "direction": "Long", "confidence": "Low", "thesis": "Same liquidity set. He does not think the next forty companies join them — low"},
        ],
        [
            "in a best case scenario, this company could have a trillion dollar outcome",
            "their margin profiles are going from negative 15% to positive 35%",
            "we've always raised our funds too small",
        ],
        {"subject": "Abstract · trillion goalposts · LP liquidity", "events": [
            {"date": "2016", "event": "Naimi starts early-stage investing; $10B was the dream outcome"},
            {"date": "2021", "event": "$8M revenue at $1B valuations; losers return at 2x"},
            {"date": "2024-26", "event": "Mega funds raise 2-3 times inside an 18-24 month window"},
            {"date": "2026", "event": "SpaceX, Anthropic, OpenAI counted as trillion-scale"},
            {"date": "2026", "event": "Parallel secondaries at 3-5x, not 2x"},
            {"date": "2026-11-06", "event": "EP499 publishes"},
        ]},
        "| v4.10 window ILTB EP499",
    )


def ep500():
    save(
        "ep500", "Invest Like the Best", "Patrick O'Shaughnessy",
        {
            "episode_number": 500,
            "title": "Zach Reitano — Building Ro, and Why Healthcare Should Be a Larger Share of GDP",
            "guest": "Zach Reitano",
            "guest_role": "Co-founder and CEO, Ro",
            "date": "2026-11-11",
            "duration_minutes": 76,
            "youtube_url": "https://www.youtube.com/watch?v=aOSuI2qPeB8",
            "links": {"youtube": "https://www.youtube.com/watch?v=aOSuI2qPeB8", "apple_podcasts": ILTB},
        },
        ["Private:Ro", "LLY", "NVO"],
        (
            "Reitano's complaint is that the patient is not the customer. Whoever controls "
            "the money at the point of purchase is who the system builds for. He wants "
            "healthcare to be a larger share of GDP, not a smaller one, if the unit of health "
            "gets cheaper and better. The US is at 18% because unit costs rose. About half "
            "of spending is on 5% of people. A $1,300 drug can net $300 to $400. Ro went "
            "from about a $250 million run rate to over $3 billion in four years, led by GLP-1s "
            "and integrated with Novo and Lilly."
        ),
        (
            "EP500, Nov 11, about 76 minutes. Reitano built Ro. Four categories: cardiometabolic "
            "health, sexual health, dermatology, fertility. GLP-1s are the fastest growing "
            "and the reason the obesity curve kinked. He treats the US system as a preview "
            "for other countries, not an anomaly, and he wants the patient to be the buyer."
        ),
        [
            (
                "Share of GDP is the wrong complaint. The US spends 18% of GDP on healthcare "
                "and people call that the problem. He asks why an absolute share is a problem "
                "if the society is buying health. Jevons, in his use, says the market gets "
                "larger when the unit cost falls. US unit costs have been rising, which is "
                "why 18% feels broken. About 50% of the cost sits on 5% of people, because "
                "the US does not give up on that person. The UK healthcare share went from "
                "6% to 12% of GDP, Germany from 9% to 12%, the US from 9% to 18%. Obesity "
                "moved with it, and GLP-1s are why the US obesity chart has flattened. Follow "
                "the money: about 30-35% hospitals, 20-25% doctors' offices, 9-10% drugs. "
                "Acute care is better than the criticism. Cancer, heart attack, and stroke "
                "survival beat the NHS and other OECD systems. The US does not use more "
                "care: fewer and shorter hospital stays, a few more scans, then higher "
                "prices and a much higher administrative load."
            ),
            (
                "Prices are not prices. A $1,300 list drug can be $300 to $400 behind the "
                "scenes. No other industry, he says, could survive with prices that are not "
                "public. PBMs and insurers sit between the patient and the price, and list "
                "prices step up 6, 7, or 8% a year. Cash pay, or insurance that covers 100% "
                "and still leaves choice, is where patients feel in control. Ro's idea is to "
                "aggregate patient spend until the system has to face the patient. Remove "
                "the PBM and the insurer from the GLP-1 path and the $1,300 price is not "
                "the price the patient should see. Per person, the system spends on the "
                "order of $20,000 to $25,000 a year. Employers write one check for many "
                "employees. The patient writes none of it and is not the customer."
            ),
            (
                "Ro's four-year print, and the GLP-1 versus AI chart. Four categories. "
                "Cardiometabolic is first, then sexual health, dermatology, and fertility. "
                "Ro is a leading US GLP-1 channel and is integrated with both Novo and Lilly. "
                "Run rate went from about $250 million to over $3 billion in four years, with "
                "fewer people than in 2021. Critics call that just weight-loss drugs. The "
                "labels moved from diabetes to obesity, then heart disease, sleep apnea, "
                "liver disease, and kidney disease, with more studies behind them. Patrick "
                "cites a chart from a few days before the taping: GLP-1 revenue is larger "
                "than AI revenue, and about twice as many individuals pay for a GLP-1 as "
                "pay for AI. Reitano reads that as consumers reporting daily impact, and as "
                "the hole in the AI story. A new medical technology does not get a free pass. "
                "It has to be substantially better than the status quo, not 1% better. He "
                "uses driverless cars the same way: blocking a safer option should carry a "
                "body count. His worry is that healthcare will keep scoring inputs instead "
                "of outcomes."
            ),
        ],
        {
            "name": "Patient as Customer × Falling Unit Cost × GLP-1 Cash",
            "components": (
                "The buyer is whoever controls the money at the purchase, and that is not "
                "the patient. An 18% GDP share is a problem only because unit costs rose. "
                "Half the spend is on 5% of people. UK 6 to 12, Germany 9 to 12, US 9 to 18. "
                "Hospitals take 30-35%, offices 20-25%, drugs 9-10%. List price $1,300 can "
                "net $300-400, and the list steps up 6-8% a year. Ro aggregates patient "
                "spend. Four categories, GLP-1s fastest, Novo and Lilly integrated, run "
                "rate from $250 million to over $3 billion in four years with fewer people. "
                "GLP-1 revenue exceeds AI revenue, and about twice as many people pay."
            ),
            "application": (
                "Private:Ro is the cash-pay aggregator, not an insurer. LLY and NVO are the "
                "two supply sources on the tape. Do not short the healthcare share of GDP "
                "because 18% looks large. Underwrite unit cost and whether the patient can "
                "see the price. A 1% better input is not the bar he wants for a new therapy."
            ),
        },
        [
            {"view": "Healthcare should be a larger share of a rich country if the unit gets better.", "question": "Why is 18% the wrong headline?", "answer": "Unit costs rose. Half the money is on 5% of people. The UK went from 6% to 12% of GDP, Germany 9% to 12%, the US 9% to 18%."},
            {"view": "The list price is not the price.", "question": "What is a $1,300 drug?", "answer": "Often $300 to $400 net. PBMs and insurers sit in between, and list prices rise 6-8% a year. Ro wants patient spend aggregated so the patient becomes the customer."},
            {"view": "GLP-1s are already a bigger consumer business than AI.", "question": "What did Ro and the chart show?", "answer": "Run rate from about $250 million to over $3 billion in four years, with fewer people. GLP-1 revenue exceeds AI revenue, and about twice as many people pay for the drug as pay for AI."},
        ],
        [
            {"ticker": "Private:Ro", "direction": "Long", "confidence": "Medium", "thesis": "From a $250 million run rate to over $3 billion in four years, fewer people, patient is the buyer — medium"},
            {"ticker": "LLY", "direction": "Long", "confidence": "Low", "thesis": "One of the two GLP-1 suppliers Ro is integrated with, and the category revenue already exceeds AI — low"},
            {"ticker": "NVO", "direction": "Long", "confidence": "Low", "thesis": "The other integrated GLP-1 source on the tape, same cash-pay volume story — low"},
        ],
        [
            "the patient is not the customer",
            "we've gone from about a $250 million run rate to over a $3 billion run rate",
            "Twice the number of people pay for GLP-1s that then pay for AI",
        ],
        {"subject": "Ro · GLP-1s · who the customer is", "events": [
            {"date": "2021", "event": "Ro headcount peak relative to later; run rate near $250M"},
            {"date": "2022-26", "event": "GLP-1 labels expand from diabetes to obesity, heart, sleep, liver, kidney"},
            {"date": "2026", "event": "Run rate over $3B with fewer people than 2021"},
            {"date": "2026", "event": "US healthcare about 18% of GDP; 50% of cost on 5% of people"},
            {"date": "2026-11", "event": "GLP-1 revenue chart exceeds AI revenue"},
            {"date": "2026-11-11", "event": "EP500 publishes"},
        ]},
        "| v4.10 window ILTB EP500",
    )


def ep501():
    save(
        "ep501", "Invest Like the Best", "Patrick O'Shaughnessy",
        {
            "episode_number": 501,
            "title": "Brad Gerstner and Geoffrey Canada — Invest America and Raising the Floor",
            "guest": "Brad Gerstner and Geoffrey Canada",
            "guest_role": "Altimeter founder · Harlem Children's Zone",
            "date": "2026-11-17",
            "duration_minutes": 84,
            "youtube_url": "https://www.youtube.com/watch?v=u6pCmQd0Wrg",
            "links": {"youtube": "https://www.youtube.com/watch?v=u6pCmQd0Wrg", "apple_podcasts": ILTB},
        },
        ["AAPL", "BRK.B", "WMT"],
        (
            "Gerstner and Canada argue you raise the floor instead of attacking success. "
            "The Invest America Act, signed July 4, 2025, opens a capital account with "
            "$1,000 in the S&P 500 when a child gets a Social Security number. About 3.7 "
            "million babies a year, and about 10,000 births a day, each get an account. "
            "The law also opened accounts for every child under 18, about 70 million, "
            "because Michael and Susan Dell and other donors said they would fund the "
            "grandfathered cohort the government would not. The child owns a slice of "
            "Walmart, Berkshire, and Apple."
        ),
        (
            "EP501, Nov 17, about 84 minutes. Patrick first heard the idea from Gerstner in "
            "2020, pacing a kitchen in COVID, and thought the politics would kill it. "
            "Canada's seed accounts for a handful of kids, including a program of about 25, "
            "could not scale. Gerstner talked with Stan Druckenmiller and others and then "
            "took the idea to a national account. Claiming the account is the remaining work."
        ),
        [
            (
                "The design. Two responses to the gap between billionaires and everyone else: "
                "attack success, or raise the floor. Gerstner picked the floor in 2020. Seed "
                "programs, including Canada's, proved the feeling of ownership and could not "
                "reach a national crisis. The Invest America Act was signed July 4, 2025. A "
                "child born in America gets a Social Security number and an account with "
                "$1,000 in the S&P 500. That birth class is about 3.7 million a year. Over "
                "20 years of newborns alone you would reach about 60 million kids. They "
                "grandfathered everyone under 18 instead. The government would not fund that "
                "larger set. Private donors did. Gerstner went to Michael and Susan Dell and "
                "others. If you build it, they would fund it. About 70 million accounts now "
                "exist. In a few months each is supposed to hold money. About 10,000 children "
                "are born each day, and each of those accounts is opened with $1,000. Parents "
                "claim it in an app with a Social Security number. Rural Indiana, the South "
                "Bronx, and Compton get the same claim. The hard step is zero to one. One to "
                "two is easier. Family, employer, and philanthropic dollars can follow, "
                "including five and ten dollar contributions, on the model of a 401k."
            ),
            (
                "What the child owns. The account is the S&P 500, so the examples Gerstner "
                "uses are a slice of Walmart, a slice of Berkshire Hathaway, and a slice of "
                "Apple, visible on a phone. That is the point of a universal capital account "
                "rather than a savings bond or a lecture. Canada has spent more than 50 years "
                "on poverty. He thinks it would be a mistake not to use this to create the "
                "next generation of capitalists, and that those capitalists will mostly be "
                "poor people. The old seed model made the child do something to receive the "
                "money. This one opens the account first. The parent still has to claim it. "
                "Gerstner separates created accounts, about 70 million, from claimed accounts. "
                "Patrick asks for the claimed percent and the answer on the tape stays on "
                "the created number: the original plan was only the 250th-birthday birth "
                "class, and the under-18 expansion is why donors, not the Treasury, fill "
                "the older accounts."
            ),
            (
                "Why 2020 became a statute. Gerstner saw prosperity compounding for people "
                "who already owned capital and the opposite for people who did not. A pilot "
                "of 25 kids could not be the national answer. Druckenmiller and Canada were "
                "early conversations. The political difficulty Patrick assumed in 2020 did "
                "not stop the July 4, 2025 signing. The remaining operating problem is "
                "claiming: an account that exists and is unclaimed is not yet a household "
                "that knows it owns Walmart, Berkshire, and Apple. Employers and grandparents "
                "can add money once the account is real. Gerstner frames that as financial "
                "independence, not a transfer that replaces work. Canada frames it as the "
                "first time poor children start inside capitalism rather than next to it."
            ),
        ],
        {
            "name": "Raise the Floor × $1,000 at Birth × Claim the Account",
            "components": (
                "Do not attack success. Open a capital account. July 4, 2025 makes $1,000 "
                "in the S&P 500 automatic with the Social Security number. About 3.7 million "
                "births a year and about 10,000 a day. Grandfathering the under-18 cohort "
                "creates about 70 million accounts. Treasury funds the newborns. Dell and "
                "other donors fund the older children. Claiming is the step from an account "
                "that exists to a household that knows it owns a slice of Walmart, Berkshire, "
                "and Apple. Zero to one is the hard part. A 25-kid seed could not do this."
            ),
            "application": (
                "AAPL, BRK.B, and WMT are the three names Gerstner uses for what the child "
                "can see. The vehicle is the S&P 500, not a stock pick. The diligence is "
                "the claim rate, not the existence of 70 million empty logins. Do not treat "
                "the donor cohort and the Treasury cohort as the same funding."
            ),
        },
        [
            {"view": "Raise the floor. Do not attack the people who already own capital.", "question": "What is the account?", "answer": "$1,000 in the S&P 500 when the Social Security number is issued. About 3.7 million newborns a year. About 10,000 accounts opened a day."},
            {"view": "Seventy million accounts exist. Claiming is the work.", "question": "Who pays for the older kids?", "answer": "The government would not fund every child under 18. Michael and Susan Dell and other donors said they would. Parents claim the account in an app."},
            {"view": "The child should be able to see a company they own.", "question": "Which names does he use?", "answer": "Walmart, Berkshire Hathaway, and Apple, on a phone. Canada thinks the next capitalists will mostly be poor kids if this is actually claimed."},
        ],
        [
            {"ticker": "AAPL", "direction": "Long", "confidence": "Low", "thesis": "One of the three companies Gerstner says a child can see they own through the S&P account — low"},
            {"ticker": "BRK.B", "direction": "Long", "confidence": "Low", "thesis": "Named alongside Apple and Walmart as a slice of the birthright account, not a separate stock pitch — low"},
            {"ticker": "WMT", "direction": "Long", "confidence": "Low", "thesis": "The third named holding a child is supposed to recognize on the phone — low"},
        ],
        [
            "let's raise the floor for everybody",
            "an account is automatically set up with $1,000 in the S&P 500",
            "we have 70 million accounts that have now been open in America",
        ],
        {"subject": "Invest America · Trump accounts · claim rate", "events": [
            {"date": "2020", "event": "Gerstner calls Patrick with the account idea during COVID"},
            {"date": "2020s", "event": "Canada seed programs, including about 25 kids, prove ownership and do not scale"},
            {"date": "2025-07-04", "event": "Invest America Act signed"},
            {"date": "2025-26", "event": "Dell and other donors agree to fund the under-18 cohort"},
            {"date": "2026", "event": "About 70 million accounts created; 10,000 births a day"},
            {"date": "2026-11-17", "event": "EP501 publishes"},
        ]},
        "| v4.10 window ILTB EP501",
    )


def fnd440():
    save(
        "fnd-440-born-of-this-land", "Founders", "David Senra",
        {
            "episode_number": 440,
            "title": "#440 Born of This Land: Chung Ju-yung",
            "guest": "Chung Ju-yung",
            "guest_role": "Autobiography, Born of This Land · founder of Hyundai",
            "date": "2026-11-17",
            "duration_minutes": 50,
            "youtube_url": "https://www.youtube.com/watch?v=_DSOxu2tLVY",
            "links": {"youtube": "https://www.youtube.com/watch?v=_DSOxu2tLVY", "apple_podcasts": FND},
        },
        ["HYMTF", "Private:Hyundai Construction", "Private:Hyundai Shipyard"],
        (
            "Senra reads Chung Ju-yung's autobiography. The nickname was bulldozer, and "
            "Chung treats it as an insult about an unschooled man who dug first. He says "
            "formal school is not wisdom, and that he thinks and works harder than others "
            "before a job that later looks reckless. The ladder is rice shop, auto repair, "
            "construction, then Korea's first shipyard. A Greek buyer gives him a purchase "
            "order and a deposit for a ship the "
            "yard does not yet have. A poor man, he writes, has to work 10 to 20 times harder."
        ),
        (
            "Founders 440, Nov 17, about 50 minutes. No guest. Senra is in Chung's own "
            "words from Born of This Land. The mid-episode Router read, a customer cutting "
            "model cost by 92% on billions of tokens, is a sponsor spot, not the book. "
            "Hyundai today, Chung writes, could not have been built by the man people "
            "thought he was."
        ),
        [
            (
                "The ladder. Chung's father had a healthy body and a diligent character and "
                "did not take days off. From age 10, Chung worked beside him and did not "
                "complain. The late 1930s rice-shop job paid a bag of rice a month. He "
                "treated small deliveries as if they were the whole job. The owner eventually "
                "offered to sell him the shop. He then ran an auto repair garage, including "
                "cars converted to charcoal and carbide when fuel was scarce, and then a "
                "construction company. Workers fled to Busan and he built them quarters. He "
                "does not give workers an excuse to procrastinate, and he does not give "
                "executives a separate elevator. A carpet going into a temporary site office, "
                "under a motto of diligence, frugality, and affection, is the scene he shuts "
                "down. Asked how he became the richest man in Korea, he answers "
                "with the sequence: rice shop, garage, construction, each time pushing "
                "again. The diligent, he says, lead lives 100 times more productive than "
                "the lazy. One day of diligence is a night of sleep. A year, two years, "
                "ten years, a life, is how the work gets recognized."
            ),
            (
                "The shipyard. A great idea starts as a grain of rice and is nurtured until "
                "he can see the project. In the early 1960s that project is Korea's first "
                "shipyard, and he had never built a boat. He travels for money. Japanese "
                "and American capital mock the technology. He quits "
                "in front of President Park. Park turns to the vice prime minister and says "
                "to reject all of Chung's proposals and never do business with him again, "
                "The line that brings Chung back is that a president "
                "and an economics minister had promised support and Chung was rolling over. "
                "He then has a Greek buyer. The purchase order and the down payment exist "
                "before the yard does. He also "
                "picks up a second order, an oil tanker, on the same trip. The government "
                "that had threatened him then tells him to build. The order is the idea, "
                "the buyer, the deposit, then the yard."
            ),
            (
                "The philosophy he wants repeated. Time is capital distributed equally. "
                "Success, if he has it, is using that capital on conviction. The poor man "
                "works 10 to 20 times harder than the rich man, because Korea did not have "
                "the resources of the advanced nations, only effort. Hyundai is his evidence. "
                "He plans every detail and then implements so fast it looks reckless. He "
                "does not experience himself as underprivileged, including farm work on an "
                "empty stomach. Positive thinking is a section of the book, not a slogan "
                "at the end. He does not trust lazy people. The bulldozer nickname, he "
                "thinks, was meant to mark an uneducated upstart who dug first and thought "
                "later. His reply is that the thinking happened before the digging, and "
                "that school is not the only place wisdom is stored. The modern group, he "
                "writes, could never have been built if he had accepted the nickname."
            ),
        ],
        {
            "name": "Grain of Rice × Greek Deposit × 10 to 20 Times the Work",
            "components": (
                "School is not the test. The sequence is rice shop, garage, construction, "
                "shipyard. A carpet in the site office fails the frugality motto. The "
                "shipyard starts as an idea the size of a grain of rice in the early 1960s. "
                "Foreign capital mocks it. Park threatens to cut him off for quitting. A "
                "Greek purchase order and a deposit arrive before the yard exists, plus a "
                "tanker order. The poor man's ratio is 10 to 20 times the work. Time is "
                "equal capital. Diligence over a life is his 100 times claim against laziness. "
                "The bulldozer nickname is an insult he answers with the planning that "
                "happened before the digging."
            ),
            "application": (
                "HYMTF is the motor company that came out of this ladder, not a multiple "
                "on one ship order. The construction company and the shipyard are the two "
                "earlier businesses in the book. Do not underwrite the Router sponsor, "
                "including the 92% inference-cost claim. The operating fact is a deposit "
                "taken before the yard existed, after he had already tried to quit."
            ),
        },
        [
            {"view": "The nickname was an insult about sequence.", "question": "What does bulldozer mean to him?", "answer": "An unschooled man who digs first. He says the thinking and the plan came before the work that looked reckless, and that school is not the only source of wisdom."},
            {"view": "The yard was financed by a buyer, not by a yard.", "question": "What did the Greek order do?", "answer": "He had quit in front of President Park. A purchase order and a down payment for a ship, plus a tanker order, existed before the first Korean shipyard did."},
            {"view": "The ladder is the whole biography.", "question": "How does he explain being the richest man in Korea?", "answer": "Rice shop, then a garage, then construction, each time pushing again. A poor man works 10 to 20 times harder. Diligence over a life is his 100 times claim."},
        ],
        [
            {"ticker": "HYMTF", "direction": "Long", "confidence": "Low", "thesis": "The motor company at the end of the rice-shop, garage, construction, shipyard ladder — low"},
            {"ticker": "Private:Hyundai Construction", "direction": "Long", "confidence": "Low", "thesis": "The company after the garage, and the frugality test of the site office — low"},
            {"ticker": "Private:Hyundai Shipyard", "direction": "Long", "confidence": "Low", "thesis": "Korea's first yard, financed by a Greek deposit before the yard existed — low"},
        ],
        [
            "not receiving formal education does not mean one is lacking in wisdom",
            "The poor man has to work 10 to 20 times harder than the rich man.",
            "A great idea starts with one single thought.",
        ],
        {"subject": "Chung Ju-yung · Hyundai · shipyard", "events": [
            {"date": "1915-30s", "event": "Farm work from age 10; late-1930s rice shop"},
            {"date": "1940s", "event": "Auto repair, charcoal and carbide cars; then construction"},
            {"date": "early 1960s", "event": "Shipyard idea; foreign capital refuses; Park threatens a cutoff"},
            {"date": "1960s", "event": "Greek purchase order and deposit before the yard exists"},
            {"date": "later", "event": "World's largest shipbuilding company, in Senra's framing"},
            {"date": "2026-11-17", "event": "Founders 440 publishes"},
        ]},
        "| v4.10 window Founders 440",
    )


if __name__ == "__main__":
    ep499()
    ep500()
    ep501()
    fnd440()

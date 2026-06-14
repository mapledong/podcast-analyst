"""Bodies for episodes 41–44 (imported by _write_acq_batch_ep37_44.py)."""

from scripts._write_acq_batch_491_500_common import base


META_OVERRIDES = {
    "acq-episode-41-bookingcom-with-jetsetter-room-77-ceo-drew-patterson": {
        "title": "Booking.com (with Drew Patterson)",
        "guest": "Drew Patterson",
        "guest_role": "Episode 41 · Guest",
    },
    "acq-episode-42-opsware-with-special-guest-michel-feaster": {
        "title": "Opsware (with Michel Feaster)",
        "guest": "Michel Feaster",
        "guest_role": "Episode 42 · Guest",
    },
    "acq-episode-43-the-square-ipo": {
        "title": "The Square IPO",
        "guest": "Square",
        "guest_role": "Episode 43",
    },
    "acq-episode-44-aol-time-warner-with-the-internet-history-podcast": {
        "title": "AOL–Time Warner (with Brian McCullough)",
        "guest": "Brian McCullough",
        "guest_role": "Episode 44 · Guest",
    },
}


def shell(ep_id: str, **body):
    ep = base(ep_id, review_notes="Manual GPT Acquired batch v5.1 — episodes 37–44", **body)
    ov = META_OVERRIDES.get(ep_id, {})
    for k, v in ov.items():
        ep["metadata"][k] = v
        if k == "title":
            ep["metadata"]["guest"] = ov.get("guest", v)
    return ep


EPISODES_41_44 = [
    shell(
        "acq-episode-41-bookingcom-with-jetsetter-room-77-ceo-drew-patterson",
        episode_rating={"overall": 4},
        keywords=["Online Travel", "Marketplace", "Agency Model"],
        conclusion=(
            "Priceline's 2005 purchase of Booking.com (~$135M) plus Active Hotels (~$155M combined ~$290M) imported "
            "Europe's agency-model OTA — hotels set price, Booking takes commission, travelers pay at stay with flexible "
            "cancellation — versus US merchant inventory risk. Geert-Jan Bruinsma bootstrapped Bookings.nl (1996) with "
            "~50K euros from 18 email contacts; Expedia diligenced six months then board-vetoed the deal. Private European "
            "investors held it until Glenn Fogel (Priceline M&A) championed acquisition; Priceline left Booking autonomous. "
            "Room nights grew from ~18.7M (2006) to 500M+ (2016); Booking drove ~$7.8B of ~$10.7B 2016 Priceline revenue. "
            "Market cap ~$91B (episode) — 'three Airbnbs.' Drew Patterson (Starwood, Kayak, Jetsetter, Room 77) explains "
            "GDS/long-tail hotel supply and why marketplace density beats feature wars."
        ),
        background=(
            "Guest Drew Patterson joins for OTA taxonomy: agency vs merchant (Amazon retail analogy), metasearch (Kayak) "
            "vs OTA conversion funnels. Booking solved multilingual European hotel calls by aggregating long-tail supply "
            "postcards couldn't reach via US GDS head — Google-longtail vs Yahoo-directory parallel.\n\n"
            "Expedia's pass looks like wholesale-model hubris; Fogel saw agency alignment with hotels and higher European "
            "travel frequency. Post-merger separation on financials preserved product/GTM independence — business-line "
            "acquisition. Tech themes: marketplace slog to tipping point, Google tax on travel keywords, Airbnb unlocking "
            "new supply, conversion as core marketplace product."
        ),
        important_facts=[
            "Priceline acquired Booking.com and Active Hotels in 2005 for a combined ~$290M ($133M + ~$155M cited).",
            "Room nights booked grew from ~18.7M in 2006 to 500M+ in 2016 — ~40%+ CAGR over a decade.",
            "2016 Priceline group revenue ~$10.7B; Booking.com contributed ~$7.8B — majority of the company.",
            "Founder Geert-Jan Bruinsma raised ~50,000 euros from 18 email contacts after mass-mailing acquaintances with email addresses.",
            "Expedia conducted ~6 months of diligence on Booking then US board rejected the deal over agency-model concerns.",
        ],
        mental_model={
            "name": "Agency Marketplace Alignment",
            "components": (
                "Merchant OTAs buy room blocks — better unit economics when markups work but misalign hotel risk and "
                "cancellation policy. Agency model: hotel sets rate, OTA earns commission, guest pays at property — "
                "negative working capital and hotel-friendly terms accelerate long-tail supply signup (postcards, fax era). "
                "Demand-side Google SEM scales only after supply density; Booking's European travel frequency beat US "
                "workaholic cohort. Priceline's M&A added a parallel business line rather than forcing merchant conversion."
            ),
            "application": (
                "When incumbents scoff at 'worse' unit economics (agency vs merchant, marketplace vs retail), check incentive "
                "alignment with supply — fragmented European hotels mirrored Amazon marketplace vs wholesale ebooks. "
                "Leave acquired winners autonomous until integration clearly improves conversion; Fogel→CEO lineage shows "
                "patience pays.",
            ),
        },
        competitive_advantage=(
            "Booking's moat is proprietary long-tail hotel supply across Europe — 500K+ global hotels, many absent from "
            "US GDS/merchant OTAs. Agency terms reduce hotel friction; SEM mastery captured high-intent 'hotel in Rome' "
            "queries. Expedia scale in US did not translate to European villa inventory.\n\n"
            "Priceline holding company structure preserved Booking brand and model — avoiding Expedia-style assimilation. "
            "Network effects: travelers go where supply is complete; hotels list where demand converts. Trivago/Expedia "
            "compete on marketing efficiency; Airbnb attacks different supply (homes).\n\n"
            "Weaknesses: Google keyword tax; industry insular talent pool; US share lagged Europe. Drew notes consolidation "
            "helps matching supply/demand but hotels may prefer direct — Hilton/Marriott vs 20-room Romania B&B value prop differs."
        ),
        key_insights=[
            {
                "view": "Expedia's pass is the counterfactual.",
                "question": "What if Expedia closed the deal?",
                "answer": "US board rejected agency economics after six-month diligence — merchant golden-goose bias. Likely Booking "
                "assimilated or starved; Priceline's willingness to run parallel models captured 500M room nights. Classic "
                "incumbent dismisses hard supply slog.",
            },
            {
                "view": "Long-tail supply beats directory head.",
                "question": "Why couldn't GDS cover Europe?",
                "answer": "US-centric GDS missed fragmented European hotels — Booking postcard MVP onboarded properties without "
                "internet. Google vs Yahoo metaphor: search won when head listings insufficient; specific European queries had "
                "one answer.",
            },
            {
                "view": "Autonomy preserved the growth engine.",
                "question": "Did Booking need Priceline capital?",
                "answer": "Agency model threw off cash; Priceline added SEM war chest and public currency but critical was "
                "Fogel leaving ops alone — separate reporting lines, no forced merchant flip. Integration of business lines "
                "often kills marketplace culture.",
            },
            {
                "view": "Conversion is the product.",
                "question": "How do OTAs win beyond ads?",
                "answer": "Bill Gurley/Rover lesson: marketplace product equals match rate × consummation. Booking instrumented "
                "keyword→booking LTV; Trivago excels at funnel math. Features matter less than completing transactions at scale.",
            },
            {
                "view": "Airbnb reshapes supply side.",
                "question": "Where is disruption now?",
                "answer": "OTAs optimized traveler experience with mixed hotel feelings; Airbnb aligned new supply (spare bedroom) "
                "with demand — different acquisition category but same travel wallet. Booking's hotel long-tail moat remains "
                "for traditional stays.",
            },
        ],
        top_investment_implications=[
            {
                "ticker": "BKNG",
                "direction": "Watch",
                "confidence": "Medium",
                "thesis": "Booking remains Priceline/Booking Holdings profit engine — marketplace density + agency alignment; "
                "watch Google/Meta CAC and regulatory pressure on OTAs; episode ~2017 framing at ~$91B mkt cap.",
            }
        ],
        golden_quotes=[
            '"He emailed everyone who he knew who had an email address because he figured if they had an email address, they at least knew something about the internet." — on Geert-Jan Bruinsma fundraising.',
            '"Booking or nothing." — David on European long-tail queries pre-Google ubiquity.',
            '"The product that you\'re building when you\'re at a marketplace company is essentially the matching of supply and demand." — Bill Gurley via David/Rover.',
        ],
        chronology={
            "subject": "Booking.com / Priceline",
            "events": [
                {"date": "1996", "event": "Geert-Jan Bruinsma founds Bookings.nl in Amsterdam"},
                {"date": "2000", "event": "Merger with Bookings Online → Booking.com name"},
                {"date": "2002", "event": "Expedia nears then aborts Booking acquisition"},
                {"date": "2002-2003", "event": "European private investors acquire majority stake"},
                {"date": "2005", "event": "Priceline acquires Booking.com and Active Hotels (~$290M total)"},
                {"date": "2006", "event": "Combined ~18.7M room nights booked post-merger"},
                {"date": "2016", "event": "~500M+ room nights; Booking ~$7.8B of ~$10.7B group revenue"},
                {"date": "2017", "event": "Episode records ~$91B Priceline market cap with Drew Patterson guest"},
            ],
        },
    ),
    shell(
        "acq-episode-42-opsware-with-special-guest-michel-feaster",
        episode_rating={"overall": 4},
        keywords=["Enterprise Software", "Data Center Automation", "Timing Risk"],
        conclusion=(
            "HP paid $1.6B in July 2007 for Opsware — Ben Horowitz and Marc Andreessen's Loudcloud pivot from 'internet OS' "
            "hosting to data-center automation software. Loudcloud (1999) sold to EDS for ~$63M after the bubble; internal "
            "Opsware tool provisioned servers LDAP inventor Tim Howes built became the whole company — market cap had sunk "
            "to ~$28M (~$40M below cash) before the turnaround. Guest Michel Feaster (HP product director, ex-Mercury; now "
            "Usermind CEO, a16z board) tells the buy-side: five-slide deck, build-vs-buy vs BladeLogic/BMC, sales-overlay "
            "integration, and market-leader status despite not-best product. Grades: Michel A, David A-, Ben B — HP got "
            "timing-right asset but lost cloud era to AWS; Puppet/Chef inherited config management."
        ),
        background=(
            "Episode flips The Hard Thing About Hard Things narrative to HP enterprise software (Mercury acquisition precedes "
            "Opsware). Loudcloud was AWS-before-AWS using Andreessen's 'electric grid' metaphor; without VMware-style "
            "virtualization and pre-cloud budgets, hosting failed. Public pivot to Opsware sold automation to enterprises "
            "with their own data centers.\n\n"
            "Feaster describes HP's manufacturing culture vs 10x software talent, overlay managers on acquired leaders, and "
            "why HP isn't among today's cloud big three. Tech theme: Sequoia-style timing studies — right product wrong clock; "
            "management pivots salvage option value. Category debate: product integration vs standalone business line."
        ),
        important_facts=[
            "HP acquired Opsware in July 2007 for $1.6B — roughly 50× the ~$28M market cap at the 2002 pivot trough.",
            "Loudcloud sold its hosting business to EDS for just over ~$63M; Opsware software was the remaining asset.",
            "At pivot, Opsware traded at ~$28M market cap with ~$60–70M cash in bank — negative enterprise value.",
            "Michel Feaster joined via Mercury Interactive (HP acquired); presented ~5 slides to justify Opsware buy vs build.",
            "BladeLogic (BMC competitor) was alternative; virtualization adoption ~2007 made data-center automation mandatory.",
        ],
        mental_model={
            "name": "Pivot Timing Over Funeral",
            "components": (
                "Loudcloud had correct thesis (utility compute) wrong decade — no virtualization, bubble capex, enterprise "
                "servers in closets. Horowitz/Andreessen kept the internal provisioning tool, fire-sold hosting, and rebuilt "
                "as enterprise ISV. HP bought market leadership + sales channel when virtualization forced every CIO to "
                "automate — not because Opsware had best UX. Enterprise wins often go to sales motion incumbents when "
                "category becomes checklist."
            ),
            "application": (
                "When macro timing kills v1, inventory internal tools that solved your pain — you are customer zero with "
                "perfect spec. Acquirers: buy when category inflection (virtualization) makes build-too-late; integrate via "
                "distribution overlay, not culture squash. Founders: HP's manufacturing HR model cannot retain 10x engineers — "
                "expect talent bleed post-deal.",
            ),
        },
        competitive_advantage=(
            "Opsware moat at sale: installed base + enterprise sales machine after Loudcloud scars — product led data-center "
            "orchestration before Puppet/Chef/docker era. HP's global CIO sales force could bundle with servers/services — "
            "classic enterprise channel advantage over startups.\n\n"
            "Versus BladeLogic/BMC, Opsware won deals via leadership perception and HP balance sheet, not pure product "
            "scores (Feaster admits). Loudcloud alumni seeded Andreessen Horowitz — acquisition created venture mafia value "
            "beyond HP P&L.\n\n"
            "Weaknesses: HP missed public cloud; config management moved to open-source; talent left incompatible culture. "
            "Michel: big cos treat engineers as interchangeable — fatal for software. Opsware did not make HP a hyperscaler; "
            "AWS/Google/Microsoft captured next wave."
        ),
        key_insights=[
            {
                "view": "Buy-side was channel + category fear.",
                "question": "Why $1.6B for automation?",
                "answer": "Feaster's team feared not playing data-center automation as virtualization hit — build would miss window; "
                "BladeLogic rival risk. Five-slide HP deck: market size in 5–10 years, cannot skip category. Price reflected "
                "turnaround story from negative EV, not Loudcloud hype.",
            },
            {
                "view": "Sales overlay beats culture merge.",
                "question": "How integrate Ben's team?",
                "answer": "HP sales learned Opsware SKU; overlay managers on acquired execs — not instant assimilation. Enterprise "
                "wins when global account reps can pitch automation alongside hardware — Opsware fine-tuned machine met HP "
                "portfolio breadth.",
            },
            {
                "view": "Best product ≠ winner in enterprise.",
                "question": "Was Opsware technically best?",
                "answer": "Feaster: market leader but not best product — Steve Jobs line that sales motion decides. BladeLogic "
                "lost despite features; same pattern in BMC/CA land. Lesson for founders: GTM and category timing stack with code.",
            },
            {
                "view": "Timing study validated.",
                "question": "Why Loudcloud fail but AWS win?",
                "answer": "Same grid metaphor — Andreessen 1999, Bezos mid-2000s with virtualization and capex appetite. Sequoia "
                "partner study cites timing as top VC decision factor; Horowitz pivoted instead of liquidating.",
            },
            {
                "view": "HP couldn't retain 10x talent.",
                "question": "Why isn't HP a cloud player?",
                "answer": "Manufacturing mindset + overlay bureaucracy; Michel swore too much for HP culture. Innovation needs "
                "courage and star retention — Mercury counterexample scaling 0→$1B. Cloud passed HP despite Opsware buy.",
            },
        ],
        top_investment_implications=[
            {
                "ticker": "HPE",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Opsware episode is historical HP enterprise software — illustrates channel M&A limits when platform shifts "
                "to public cloud; legacy read for infra investors tracking automation vs hyperscaler native tools.",
            }
        ],
        golden_quotes=[
            '"It\'s like providing the electric power grid and companies can plug in." — Marc Andreessen on Loudcloud (Bezos reused for AWS).',
            '"In the enterprise, it\'s not always the best product that wins." — Steve Jobs (via hosts) on Opsware vs BladeLogic.',
            '"Timing is everything." — David summarizing Sequoia partner study on venture outcomes.',
        ],
        chronology={
            "subject": "Loudcloud / Opsware / HP",
            "events": [
                {"date": "1999", "event": "Andreessen and Horowitz found Loudcloud"},
                {"date": "2000", "event": "Tech bubble peak; Loudcloud highly hyped pre-IPO"},
                {"date": "2002", "event": "Hosting sold to EDS for ~$63M; public pivot to Opsware software"},
                {"date": "2002", "event": "Opsware market cap ~$28M — below cash on hand"},
                {"date": "2007", "event": "Virtualization mainstream; data-center automation inflection"},
                {"date": "Jul 2007", "event": "HP acquires Opsware for $1.6B"},
                {"date": "2013", "event": "Michel Feaster founds Usermind; Ben Horowitz joins board via a16z"},
            ],
        },
    ),
    shell(
        "acq-episode-43-the-square-ipo",
        episode_rating={"overall": 4},
        keywords=["Fintech IPO", "Small Business", "Ratchet Mechanics"],
        conclusion=(
            "Square went public November 19, 2015 at $9/share (~$2.9B valuation) — below the $11–13 range and half the prior "
            "$6B Series E — amid Jack Dorsey becoming permanent CEO of Twitter and Square simultaneously. Origin myth: Jim "
            "McKelvey could not accept cards for $2K glass faucets; Jack Dorsey (ex-boss) cofounded mobile acceptance with "
            "professor Robert Morley's card-reader IP (later lawsuit/settlement). Square unlocked ~24M of ~30M US micro-merchants "
            "under $100K revenue excluded from legacy merchant accounts via ML underwriting — progressive trust limits vs "
            "Verifone/PayPal fraud losses. Starbucks 2012 deal forced enterprise-grade product but lost money per swipe. "
            "Goldman-led Series E ratchet ($93M extra stock at IPO) created perverse banker incentives. Hosts: fundamentals "
            "won — ~$10B market cap by episode (~$25.59) — but narrative was 'first dead unicorn.'"
        ),
        background=(
            "David traces St. Louis glassblower Jim McKelvey → Jack Dorsey (Twitter ousted, initially pitched electric cars) → "
            "Morley reader IP. Almost named Squirrel with acorn dongle until Scott Forstall flagged Apple café POS conflict. "
            "2010 launch: free reader, flat 2.75% pricing vs opaque interchange grids.\n\n"
            "Funding: Khosla A, Sequoia B, Kleiner $100M C, Sacca/Rizvi $200M, Starbucks strategic 2012. IPO chapter covers "
            "liquidation preference stacks, employee option underwater at $6B strike, and why late private rounds force public "
            "exit. Square reframed as merchant growth platform (Capital, Payroll, Register) monetizing via payments take rate."
        ),
        important_facts=[
            "At Square's start ~30M US businesses under $100K revenue; only ~6M could accept credit cards — ~24M excluded.",
            "Square IPO priced $9/share (Nov 19, 2015) for ~$2.9B valuation vs $6B Series E (~6 months prior).",
            "Series E ratchet granted ~20% IPO return; ~$93M additional stock issued to investors when pricing halved round valuation.",
            "Goldman Sachs invested in Series E (~$50M of $150M) and led IPO — banker fees ~$10M vs ratchet payout incentives.",
            "Starbucks invested and moved US store payments to Square (2012) — strategically valuable, financially loss-making per swipe.",
        ],
        mental_model={
            "name": "Underwriting as Product Moat",
            "components": (
                "Square's wedge was not the dongle — incumbents copied hardware. Risk engine granting incremental volume as "
                "merchants prove non-fraudulent behavior opened 24M excluded micro-merchants. Flat 2.75% vs 15-page interchange "
                "schedules reduced cognitive load. Free reader shifted capex to CAC; software (Register, Capital, Payroll) "
                "increased LTV while payments tax funded bundle. Starbucks forced enterprise reliability; hangover nearly "
                "killed IPO story until unit economics cleared."
            ),
            "application": (
                "In regulated rails (payments, lending), ML underwriting can be core IP — not a back-office cost center. "
                "Founders raising late mega-rounds: ratchets invert banker incentives; employees get diluted when strikes "
                "exceed public comps. IPO when private preference stacks threaten talent retention, not when vanity valuation "
                "demands it."
            ),
        },
        competitive_advantage=(
            "Square moat combines brand trust with micro-merchant risk models incumbents would not build — Verifone shut "
            "competing product after ~1% fraud losses. UX (Register, inventory, appointments) monetized via payments — "
            "AWS-style flywheel cited by hosts.\n\n"
            "Jack Dorsey storycraft ('Jim the glassblower') aligned GTM; design excellence masked young-company ops. "
            "Dual-CEO Twitter/Square split hurt IPO roadshow narrative but did not break transaction growth.\n\n"
            "Weaknesses: payments low margin; Starbucks mispricing; Goldman conflict optics; competition from Stripe/Clover. "
            "Episode documents ratchet era excess more than current Block valuation."
        ),
        key_insights=[
            {
                "view": "Founder stories are GTM infrastructure.",
                "question": "Morley lawsuit vs glassblower myth?",
                "answer": "Official story drives employee, investor, and customer alignment — hosts note reinvented founding narratives "
                "common (Zillow, etc.). Morley IP dispute settled; myth still explains mission better than cap table fights.",
            },
            {
                "view": "Ratchets invert banker alignment.",
                "question": "Why Goldman price low?",
                "answer": "Series E promised ~20% IPO return via extra shares — ~$93M transfer vs ~$10M underwriting fee. "
                "Participating as investor + lead underwriter creates incentive to price down; challenges 'let bank into last round' "
                "conventional wisdom.",
            },
            {
                "view": "Private preferences hide true dilution.",
                "question": "Why IPO below $6B?",
                "answer": "Liquidation stacks mean headline private valuations overstate common upside. Employees hired at $6B "
                "strike saw underwater options for months — retention risk forced public market despite bad press.",
            },
            {
                "view": "Enterprise detour via Starbucks.",
                "question": "Was Starbucks worth it?",
                "answer": "Lost money per transaction but accelerated Register/inventory enterprise features and credibility — "
                "strategic win, financial hangover. Classic big-partner forcing function.",
            },
            {
                "view": "Not a payments company — merchant OS.",
                "question": "How survive 'payments suck' narrative?",
                "answer": "S-1 frames access to capital, customers, loyalty — payments as monetization layer for software bundle "
                "analogous to AWS subsidizing tools. Fundamentals (transaction revenue ~$482M/qtr vs services) vindicated post-IPO.",
            },
        ],
        top_investment_implications=[
            {
                "ticker": "SQ",
                "direction": "Watch",
                "confidence": "Medium",
                "thesis": "2017 retrospective: IPO looked like unicorn collapse; underwriting + software bundle thesis aged well — "
                "episode teaches cap-table/ratchet mechanics more than near-term SQ rating (now Block).",
            }
        ],
        golden_quotes=[
            '"This is the first unicorn to die." — Press reaction to Square\'s 2015 IPO pricing.',
            '"Either revenue had to grow, or spending had to shrink." — Barry McCarthy (different episode); here Jack on dual-CEO scrutiny.',
            '"Can you imagine the credit industry being invented today?" — Ben on 3% interchange accepted over cash.',
        ],
        chronology={
            "subject": "Square IPO",
            "events": [
                {"date": "2008", "event": "McKelvey calls Dorsey; glass faucet card acceptance problem"},
                {"date": "2009", "event": "Square founded; Khosla Series A"},
                {"date": "2010", "event": "Square launches with free reader and 2.75% flat pricing"},
                {"date": "2011", "event": "Sequoia Series B; Kleiner $100M Series C in 2012"},
                {"date": "2012", "event": "Starbucks strategic investment and US store rollout"},
                {"date": "2014", "event": "Series E ($150M) at $6B valuation with IPO ratchet"},
                {"date": "Jun 2015", "event": "Dick Costolo exits Twitter; Dorsey interim CEO"},
                {"date": "Oct 2015", "event": "Dorsey named permanent CEO of Twitter and Square"},
                {"date": "2015-11-19", "event": "IPO at $9/share (~$2.9B); ratchet triggers ~$93M stock issuance"},
            ],
        },
    ),
    shell(
        "acq-episode-44-aol-time-warner-with-the-internet-history-podcast",
        episode_rating={"overall": 4},
        keywords=["Dot-Com Bubble", "Media Merger", "Platform vs Content"],
        conclusion=(
            "January 2000 AOL–Time Warner merger (~$350B combined, AOL ~55%) closed the bubble apex: Dulles 'growth hackers' "
            "meet Manhattan media. AOL's dial-up/subscription revenue (~$9.5B, much from dot-com ads recycling VC into portal "
            "slots) bought Time Warner's ~$25B+ real revenue — Jerry Levin accepted 'internet valuations.' AIM prefigured "
            "Facebook/WhatsApp; CD carpet-bombing was original performance marketing. Integration failed (fiefdoms, "
            "Passport vs internal politics); $99B write-down; spin 2009 (~$3B AOL). Brian McCullough guest; hosts grade "
            "AOL side C (buoyancy not acceleration) vs Time Warner F — yet AOL shareholders swapped into TWX then AT&T "
            "outcome better than standalone AOL→Verizon ~$4.4B. Lesson: platforms win by connecting people; buying "
            "content factories misunderstands zero marginal cost."
        ),
        background=(
            "Crossover format with Internet History Podcast — AOL history from Quantum/Compuserve rivalry, Virginia HQ, "
            "bundled walled garden (mail, AIM, channels) vs open web. 1998 AOL ~$30B 'insane'; 18 months later buying Time "
            "Warner. Revenue quality: portal ads from startups that went bust when LPs stopped funding ad buys.\n\n"
            "Tech themes: bundling/unbundling cycles; AOL CD growth hack commoditized; Facebook mobile-feed ad parallel. "
            "Counterfactual: Time Warner better without merger? AOL to zero alone? eBay would have been smarter target. "
            "2017 coda: AOL in Verizon; Time Warner selling to AT&T — phone companies own both merger children."
        ),
        important_facts=[
            "Announced January 2000: combined AOL Time Warner valued over ~$350B; AOL shareholders ~55%, Time Warner ~45%.",
            "Pre-merger AOL revenue under ~$5B (much from dot-com ad recycling); Time Warner revenue over ~$25B.",
            "Combined company later took ~$99B goodwill write-down; AOL spun 2009 at ~$3B valuation.",
            "AOL still earned ~$606.5M dial-up revenue as of Verizon bid era (May 2015) — decades-long tail.",
            "AIM had ~100M users cited — messaging/social graph AOL failed to monetize vs Facebook.",
        ],
        mental_model={
            "name": "Platform vs Factory Confusion",
            "components": (
                "AOL at peak was a connectivity + attention platform (AIM buddy lists, chat, email) with ad inventory sold "
                "to frothy startups — not durable like Google's intent ads. Time Warner was content factories (CNN, HBO, "
                "Warner Bros) with real P/E multiples. Merger applied tech P/E to industrial media and industrial management "
                "to zero-marginal-cost dreams. Winners on open internet connect users (Facebook, Google); losers buy more "
                "content manufacturing believing 'catalyst' slogans."
            ),
            "application": (
                "When strategic buyers chase 'internet speed,' ask if target revenue is circular (your advertisers' VC $) "
                "vs recurring consumer WTP. Acquiring stability (Time Warner) to exit bubble stock can grade A for sellers' "
                "wealth, F for product strategy. Growth hacks (CDs) expire — moats need retention loops, not CPM arbitrage."
            ),
        },
        competitive_advantage=(
            "AOL's 1990s moat: dial-up bundling, AIM network effects (local dominance vs MSN Messenger by country), CD "
            "distribution arbitrage, and Virginia hustle — not technology depth. Walled garden unified mail/chat/news before "
            "open web habituation.\n\n"
            "Time Warner brought cable (later spun), HBO, Warner music/film, and journalism brands — manufacturing and "
            "affiliate-fee businesses misaligned with AOL product culture. Post-merger, neither side could execute OTT pivot; "
            "Google/Facebook took display; Netflix/streaming took video attention.\n\n"
            "Weaknesses: ad revenue evaporated with dot-com; Passport politics; Levin/Pittman 'catalyst' doublespeak. "
            "Verizon/AT&T endings show telecom capital won legacy media/internet assets — not Silicon Valley redemption."
        ),
        key_insights=[
            {
                "view": "Revenue quality killed the thesis.",
                "question": "Why classify as 'other' acquisition?",
                "answer": "AOL bought balance-sheet respectability and liquidity for bubble stock — not technology, people, or "
                "synergistic product. Time Warner side believed new valuation physics; both drank Kool-Aid per Kara Swisher.",
            },
            {
                "view": "AIM was the real social graph.",
                "question": "What did AOL squander?",
                "answer": "~100M users on buddy lists, away messages, profiles pre-Facebook — internal tool origin like Slack. "
                "Protocol wars blocked interoperability; no feed ads or mobile pivot. Facebook inherited attention AOL owned.",
            },
            {
                "view": "Growth hacks decay to CPM baseline.",
                "question": "What worked with CDs?",
                "answer": "Unconventional offline distribution + free hours exploited zero marginal cost before everyone copied — "
                "then customer acquisition commoditized like generic Facebook ads today.",
            },
            {
                "view": "Grades split by shareholder hat.",
                "question": "AOL A- or C?",
                "answer": "Hosts land C for AOL: preserved wealth via TWX/AT&T equity chain vs standalone path to Verizon ~$4.4B — "
                "buoyancy not NeXT/Instagram-style acceleration. Time Warner unquestioned F — destroyed value manufacturing content "
                "under bubble managers.",
            },
            {
                "view": "Phone companies inherit both legacies.",
                "question": "2017 epilogue?",
                "answer": "AOL sold to Verizon; Time Warner pending AT&T — joke that worst tech/media merger ends owned by telcos. "
                "Open-web platforms (Google/FB) captured ad dollars AOL recycled from VC.",
            },
        ],
        top_investment_implications=[
            {
                "ticker": "T",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "Episode frames TWX/AT&T arc as cautionary media consolidation — content factories vs platform economics; "
                "historical lens only post-WBD spinoffs.",
            },
            {
                "ticker": "VZ",
                "direction": "Watch",
                "confidence": "Low",
                "thesis": "AOL dial-up cash tail (~$600M+) surprised hosts — legacy ISP revenue durability vs zero strategic moat; "
                "Verizon media experiment read-through for telco content plays.",
            },
        ],
        golden_quotes=[
            '"This new world of valuations in the internet economy is something I accept." — Jerry Levin (Time Warner CEO), merger announcement.',
            '"All you need to do is put a catalyst to Time Warner and in a short period you can alter the growth rate." — Bob Pittman, AOL.',
            '"Two anchors tied to one another are just going to sink faster." — Brian McCullough on merger logic.',
        ],
        chronology={
            "subject": "AOL / Time Warner merger",
            "events": [
                {"date": "1985", "event": "Quantum Computer Services founded (becomes AOL)"},
                {"date": "1997", "event": "AIM scales; walled-garden peak usage"},
                {"date": "1998", "event": "AOL market cap under ~$30B — pre-bubble surge"},
                {"date": "2000-01", "event": "AOL–Time Warner merger announced (~$350B combined)"},
                {"date": "2001", "event": "Dot-com bust; AOL ad revenue collapses as VC-funded advertisers fail"},
                {"date": "2002", "event": "~$99B goodwill write-down begins era of merger regret"},
                {"date": "2009", "event": "AOL spun from Time Warner at ~$3B valuation"},
                {"date": "2015", "event": "Verizon acquires AOL (~$4.4B); dial-up still ~$606M revenue"},
                {"date": "2017", "event": "Episode records AT&T pending Time Warner acquisition"},
            ],
        },
    ),
]

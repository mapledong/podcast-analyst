"""Batch 2 episodes 4–10 (imported by _batch2_episodes.py)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DISCOVERED = json.loads((ROOT / "data" / "discovered" / "acquired_episodes.json").read_text())
META = {e["id"]: e for e in DISCOVERED["episodes"]}
LINKS_BASE = {
    "apple_podcasts": "https://podcasts.apple.com/podcast/acquired/id1050462261",
    "spotify": "https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx",
}


def base(ep_id: str, **kwargs) -> dict:
    ep = META[ep_id]
    return {
        "episode_id": ep_id,
        "podcast": "Acquired",
        "host": "Ben Gilbert & David Rosenthal",
        "metadata": {
            "episode_number": ep["episode_number"],
            "title": ep["title"],
            "guest": ep["guest"],
            "guest_role": ep["guest_role"],
            "date": ep["date"],
            "duration_minutes": ep["duration_minutes"],
            "youtube_url": ep.get("youtube_url") or "",
            "links": {
                "youtube": ep.get("youtube_url") or "",
                "acquired": ep["acquired_url"],
                **LINKS_BASE,
            },
        },
        "extraction_meta": {
            "model": "manual-gpt-agent-v4.7",
            "transcript_source": "acquired.fm",
            "status": "approved",
            "template_version": "5.1-acquired",
        },
        **kwargs,
    }


REST: dict[str, dict] = {}

REST["acq-tsmc-founder-morris-chang"] = base(
    "acq-tsmc-founder-morris-chang",
    episode_rating={"overall": 5},
    keywords=["Pure-Play Foundry", "Morris Chang", "Learning Curve"],
    conclusion="Morris Chang's Taipei interview explains TSMC's trillion-dollar outcome as pure-play foundry discipline plus learning-curve pricing. Founded at 56 in 1987 when fabless barely existed, TSMC served IDM overflow before NVIDIA, Qualcomm, and Apple arrived. The 2009 yield crisis never included layoffs; Chang settled NVIDIA's ~$100M dispute over dinner. The 28nm bet (~$6B CapEx in 2010 after 40nm stumbles) coincided with smartphones; Apple forced a 20nm detour (~$10B) before TSMC won all Apple Silicon. Gross margins mid-50s while customers earn 70–80% reflects value split with designers. Hsinchu Science Park ecosystem — ASML, Synopsys, ARM co-located — is unreplicable; Arizona fabs lack leading-edge volume. Semiconductor market grew $26B (1987) to ~$527B (2024); new fabs cost ~$20B heading to $100B — natural monopoly at the leading edge.",
    background="Ben and David record in Dr. Chang's Taipei office after four years studying semiconductors — TSMC, NVIDIA, Qualcomm, ARM, Synopsys. Volume two of Chang's autobiography (Traditional Chinese only) anchors the conversation: Jensen Huang partnership from RIVA 128, 2009 operational crisis, 28nm leadership bet, and Apple courtship via Jeff Williams.\n\nPost-interview playbook covers pure-play foundry as accident-then-strategy, Bill Bain/BCG learning-curve economics, and geographic cluster moats in Hsinchu — the most successful government industrial-park initiative Ben and David cite.",
    important_facts=[
        "TSMC founded 1987 when Morris Chang was 56; global semiconductor market ~$26B then vs ~$527B in 2024; TSMC is among few trillion-dollar companies not on US West Coast.",
        "2009 crisis: yield problems at 40nm; Chang returned as CEO, no layoffs ever under his watch, rehired departed staff; settled NVIDIA dispute ~$100M over family dinner — partnership resumed for billions in subsequent business.",
        "28nm node: CapEx jumped from ~$2–2.5B/year for a decade to ~$6B in 2010; node captured smartphone wave; Apple initially demanded 20nm (~$10B fabs) Intel had for Macs — TSMC bet company on Apple volume at half allocation.",
        "Learning-curve pricing (BCG/Bain with Chang at TI): win highest volume on each node to spread fixed fab cost; forecasting iPhone/NVIDIA AI demand becomes existential — 5–10% demand error tanks node profitability.",
        "Hsinchu Science Park: TSMC + MediaTek + Cadence + Synopsys + ARM + universities co-located; leading-edge fab construction ~football-field scale (~$20B+, trending toward $100B); Arizona expansion lacks Taiwan ecosystem density.",
    ],
    mental_model={
        "name": "Pure Play Foundry + Learning Curve",
        "components": "TSMC never competes with customers on chip design — structural trust Apple/NVIDIA require versus Intel/Samsung IDM conflicts. Winning each process node requires taking largest volume first to drive yields and lower $/wafer (learning curve). Early TSMC lived on IDMs' unwanted overflow; fabless revolution (NVIDIA 1987, ARM ecosystem) aligned with TSMC's model. CapEx tracks net income bars — reinvest everything each node. Geography compounds: Hsinchu integrates EDA, equipment, and PhD pipeline unreplicable by 'airlifting' fabs.",
        "application": "In capital-intensive component businesses, ask whether the vendor competes with its customers and who gets volume at node ramp. TSMC's moat strengthens as nodes cost $20B→$100B — fewer players, higher scale threshold. Investors in fabless (NVDA, AAPL silicon) inherit TSMC concentration risk; TSMC Taiwan cluster is geopolitical single point of failure.",
    },
    competitive_advantage="TSMC wins because it is the only leading-edge foundry with zero customer conflict. Intel and Samsung design their own chips; Apple will not trust Intel foundry with iPhone silicon. Chang rejected IDM path at founding — Taiwan lacked design talent anyway — and doubled down when fabless designers needed neutral manufacturing.\n\nLearning-curve execution lets TSMC price aggressively early on each node, capture Apple/NVIDIA/AMD volume, and fund the next R&D cycle while lagging competitors bleed margin on low utilization. Old fabs (Fab 2–3 from late 1980s still running) monetize trailing nodes for automotive/sensors — unlike Intel's habit of closing legacy fabs.\n\nWeaknesses: customer concentration (Apple, NVIDIA), geopolitical Taiwan exposure, and capital intensity — one mis-forecast node can freeze the game board. Samsung competes on leading edge but Apple rivalry limits share; Intel foundry rebuild unproven.\n\nVersus ASML (equipment monopoly) or ARM (architecture), TSMC captures manufacturing scale in the AI/smartphone era — ~55% gross margin while creating more customer value than it captures.",
    key_insights=[
        {
            "view": "Not competing with customers is TSMC's core invention.",
            "question": "Why does Apple trust TSMC but not Intel?",
            "answer": "Intel designs CPUs competing with Apple's in-house silicon; even 'foundry services' carry conflict. TSMC's original pitch slide (in TSMC museum) listed dedicated pure-play foundry — impossible to compete with Intel on design then, but fabless revolution made neutrality the winning model. Samsung makes phones competing with Apple. TSMC only manufactures — trust becomes moat.",
        },
        {
            "view": "28nm was the leadership inflection after 40nm crisis.",
            "question": "Why bet $6B CapEx in 2010?",
            "answer": "40nm yields nearly broke customer relationships (Qualcomm, NVIDIA); Chang returned, settled disputes, fired no one. 28nm coincided with smartphone AP demand — TSMC committed capacity before peers recovered. Learning curve required being largest volume player; hesitation would cede node to Samsung/Intel. Smartphones provided forecastable whale customer.",
        },
        {
            "view": "Apple deal was bet-the-company on 20nm.",
            "question": "What did Jeff Williams demand?",
            "answer": "After 28nm all-in, Apple wanted 20nm capacity Intel used for Macs — not in TSMC roadmap (~$10B incremental fabs). Chang offered half Apple's requested volume to manage risk; winning Apple validated foundry model at mobile scale. Intel lost iPhone forever; TSMC makes all Apple Silicon today.",
        },
        {
            "view": "Learning curve makes forecasting customer end-markets mandatory.",
            "question": "Why must TSMC predict iPhone sales?",
            "answer": "Fixed fab cost amortizes over wafer volume — largest player hits lowest cost, wins next node. Under-forecast → idle capacity destroys margin; over-forecast → existential debt. TSMC must model NVIDIA AI demand years ahead. 5–10% error on node demand wipes profitability for a generation — manufacturer as macro forecaster.",
        },
        {
            "view": "Hsinchu cluster cannot be replicated quickly.",
            "question": "Why are Arizona fabs secondary?",
            "answer": "Decades co-locating TSMC, EDA vendors, equipment partners, MediaTek, universities — daily collaboration on next-node specs. Ben/David describe science-park busses with ARM/Google backpacks. Arizona lacks volume, leading-edge scale, and ecosystem density; government industrial policy in Hsinchu is cited as history's most successful targeted innovation park.",
        },
    ],
    top_investment_implications=[
        {"ticker": "TSM", "direction": "Long", "confidence": "High", "thesis": "Pure-play foundry monopoly at leading edge; AI/GPU demand drives advanced node utilization; ~55% gross margins and learning-curve scale barriers ($20B+ fabs) limit competitors — geopolitical Taiwan risk is primary bear case."},
        {"ticker": "NVDA", "direction": "Watch", "confidence": "Medium", "thesis": "NVIDIA–TSMC partnership since RIVA 128; AI GPU demand depends on TSMC CoWoS/advanced packaging capacity — supply allocation is strategic bottleneck for AI capex cycle."},
    ],
    golden_quotes=[
        "\"You never did a layoff\" — Ben on Chang's 2009 return; rehired staff and settled NVIDIA ~$100M without arbitration.",
        "\"If you actually are good at all of this… the story of TSMC goes from surprising to an inevitability\" — Ben on learning-curve mastery.",
        "\"Semiconductor market grew from $26 billion to $527 billion\" — tailwind since TSMC's 1987 founding.",
    ],
    chronology={
        "subject": "Morris Chang · TSMC",
        "events": [
            {"date": "1987", "event": "TSMC founded in Hsinchu; pure-play foundry model pitched to Taiwan government"},
            {"date": "1990s", "event": "Early customers IDM overflow; fabless designers emerge"},
            {"date": "1998", "event": "NVIDIA RIVA 128 — TSMC fabs Jensen's chips; partnership begins"},
            {"date": "2009", "event": "40nm yield crisis; Chang returns as CEO; no layoffs"},
            {"date": "2010", "event": "CapEx ~$6B bet on 28nm node"},
            {"date": "2010–11", "event": "Apple/Jeff Williams talks; 20nm capacity commitment"},
            {"date": "2014", "event": "Apple A8 on TSMC; Intel loses iPhone foundry permanently"},
            {"date": "2017–20", "event": "7nm/5nm leadership; Apple Silicon transition"},
            {"date": "2020s", "event": "AI boom; NVIDIA/AMD advanced node demand surges"},
            {"date": "2025", "event": "Trillion-dollar market cap; 2nm fabs under construction in Hsinchu"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

REST["acq-mars-inc-the-chocolate-story"] = base(
    "acq-mars-inc-the-chocolate-story",
    episode_rating={"overall": 4},
    keywords=["Forrest Mars Sr.", "Confectionery", "Private Company"],
    conclusion="Mars Inc. crossed ~$50B sales as a family-owned confectionery and pet-food conglomerate built by Forrest Mars Sr.'s operational obsession. Frank Mars created the Milky Way (~1923); Forrest expanded US and UK businesses, copied European chocolate processes, and bought M&M's partner out for ~$1M (1949) for 20% stake valuing candy at ~$65M today-adjusted. Mars runs 18% return-on-assets targets (~5-year payback), time clocks for all employees including CEOs, and 30% fewer workers than Hershey with higher output per worker. Forrest's 1964 deal swapped Mars stock for Warren Buffett's See's Candies stake — Buffett later called it his worst trade. Pet food (Pedigree, Royal Canin) and Wrigley gum diversified beyond chocolate; company remains private with Mars family control and no public reporting.",
    background="Ben and David trace Mars from Frank Mars's 1911 Tacoma kitchen through Forrest's exile to England (~1932 with $50K and foreign Milky Way rights), M&M's wartime military channel, and the fractious family ownership leading to Buffett's See's swap.\n\nThe episode contrasts Hershey's milk-chocolate scale with Mars's engineering culture — Toyota Production System decades early, marketing discipline via Ted Bates research, and capital allocation insisting every factory earn 18% ROA within ~5 years.",
    important_facts=[
        "Mars ~$50B+ annual sales; top-five US private company; Mars family still owns; no public financials — contrast Hershey public ~$11B revenue.",
        "Milky Way drove Mar-O-Bar from ~$73K to ~$793K revenue in one year (1920s); by 1929 Mars produced ~20M Milky Way bars annually; Great Depression era Mars hit ~$25M revenue (1932) from ~$800K (1924).",
        "Forrest Mars Sr. bought Bruce Murrie's 20% of M&M's for ~$1M (1949) — implied ~$5M business value (~$65M inflation-adjusted); M&M's dominated WWII military rations (Air Force #1 customer).",
        "Mars targets 18% return on total assets per division (~4–5 year payback); pays ~10% above industry wages; all employees including CEO punch timecards — 10% bonus for perfect attendance.",
        "1964: Forrest traded Mars shares for Buffett's See's Candies stake; Buffett later regretted — See's generated massive cash; Mars operates ~30% fewer employees than Hershey with higher output per worker (Worldly Partners data).",
    ],
    mental_model={
        "name": "Factory ROA Discipline",
        "components": "Forrest Mars treated every plant as investment requiring ~18% ROA — not higher (under-utilized assets) or lower (bad project). Time clocks and frugality enforced accountability from CEO down. Marketing used research (Ted Bates 1950 study) not Milton Hershey's '4% growth' index card. Vertical integration when suppliers failed (own chocolate after Hershey disputes). Family ownership enabled decades-long compounding without quarterly pressure.",
        "application": "In private consumer businesses, measure output per employee and ROA by site — Mars proves operational culture can beat larger public rivals without stock-market capital. When evaluating confectionery/pet peers (HSY, Nestlé divisions), Mars's scale with privacy premium is inaccessible to public investors except via debt/supplier exposure.",
    },
    competitive_advantage="Mars competes on manufacturing efficiency and brand portfolio breadth, not single-product romance like Hershey's milk chocolate shrine. Snickers, M&M's, Twix, Pedigree, Royal Canin, and Wrigley create channel power in checkout, pet aisle, and gum rack — retail slotting scale private Mars hides from filings.\n\nForrest imported European conching/tempering expertise; M&M's candy shell solved chocolate melt in military logistics — distribution innovation. Refusal to go public avoided quarterly myopia; 18% ROA gate killed mediocre SKUs.\n\nWeaknesses: family governance complexity (1964 Buffett swap), Forrest's abusive management style driving talent out, and pet-food dependence for modern growth while candy faces health trends. Hershey remains US chocolate share leader but Mars leads global confectionery revenue.\n\nVersus Mondelez or Nestlé, Mars's private structure and pet mix (~50%+ of sales) diversify away from pure candy cyclicality; operational metrics (output/worker) exceed Hershey with fewer heads.",
    key_insights=[
        {"view": "Forrest Mars was an operator, not a chocolatier romantic.", "question": "How did Mars beat Hershey?", "answer": "Forrest studied European processes, enforced 18% ROA per factory, and clocked everyone including himself. While Hershey ran ~4% annual growth off Milton's note card, Mars used Ted Bates market research to set aggressive targets. Bought out M&M's partner after pushing Bruce Murrie out — control mattered more than partnership harmony."},
        {"view": "M&M's was a logistics product before a brand.", "question": "Why did the military adopt M&M's?", "answer": "Candy shell prevented melting in Pacific/European theaters — Air Force and Army bulk orders built habit. Mars and Hershey supplied WWII rations; post-war civilian demand followed distribution. Forrest saw manufacturing constraints as marketing problems."},
        {"view": "The Buffett–See's swap was history's expensive trade for Warren.", "question": "Why swap with Forrest?", "answer": "1964 Forrest needed control consolidation; traded Mars stock for Buffett's See's stake. See's threw off cash for decades; Mars compounded privately into ~$50B sales. Illustrates private family compounders vs public market optionality."},
        {"view": "Pet food is Mars's modern growth engine.", "question": "Is Mars still a chocolate story?", "answer": "Pedigree, Royal Canin, and Wrigley acquisitions diversified beyond candy — chocolate episode focuses origin but ~$50B revenue spans pet care and gum. Chocolate culture (quality, ROA) transferred to pet manufacturing."},
        {"view": "Privacy enables long-term factory bets.", "question": "Why stay private?", "answer": "No quarterly ROA hit from growth capex; family can run 5-year payback math across decades. Public Hershey faces activist and ESG pressure Mars avoids — but investors lack direct equity access."},
    ],
    top_investment_implications=[
        {"ticker": "HSY", "direction": "Watch", "confidence": "Medium", "thesis": "Public comp for US chocolate; Mars leads global confectionery with superior output/employee and private pet diversification — Hershey trades as pure-play with slower international scale."},
    ],
    golden_quotes=[
        "\"Mars crossed $50 billion in sales last year, and they're still completely privately owned\" — Ben opening frame.",
        "\"18% return on total assets… every investment needs to pay for itself in less than five years\" — Forrest Mars capital discipline.",
        "\"Gross sales 4% every year, and that was the plan\" — Hershey's index-card growth vs Mars research-driven targets.",
    ],
    chronology={
        "subject": "Forrest Mars Sr. · Mars Inc.",
        "events": [
            {"date": "1911", "event": "Frank Mars starts candy business in Tacoma"},
            {"date": "1923", "event": "Milky Way launches; Mar-O-Bar revenue surges"},
            {"date": "1932", "event": "Forrest exiled to UK with $50K and foreign Milky Way rights"},
            {"date": "1941", "event": "M&M's founded with Bruce Murrie; military sales dominate WWII"},
            {"date": "1949", "event": "Forrest buys Murrie's 20% for ~$1M; full M&M's control"},
            {"date": "1950", "event": "Ted Bates market study sets modern Mars marketing discipline"},
            {"date": "1964", "event": "Forrest swaps Mars stock for Buffett's See's Candies stake"},
            {"date": "1980s–2000s", "event": "Pet food expansion (Pedigree, Royal Canin); Wrigley acquisition"},
            {"date": "2024", "event": "Pet food expansion (Pedigree, Royal Canin); Wrigley acquisition"},
            {"date": "2024", "event": "~$50B+ sales; remains Mars family private"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

REST["acq-ikea"] = base(
    "acq-ikea",
    episode_rating={"overall": 4},
    keywords=["Flat-Pack Retail", "Ingvar Kamprad", "Cost Leadership"],
    conclusion="IKEA is the world's largest furniture retailer (~€50B+ revenue) built on Ingvar Kamprad's Lista frugality: only ~500 kronor (~$63) ever raised (1938), 100% family ownership until foundation transfer, and €25B+ cash with owned real estate. The 1956 flat-pack LÖVET table discovery — remove legs for transport — unlocked self-assembly, lower breakage, and catalog-showroom hybrid (1953 Älmhult exhibition). Poland sourcing (1960s) and board-on-frame LACK table (~$9.99 today) drove Scandinavian simple design into urbanizing Europe. Germany remains largest market; meatballs (~1B/year) increase dwell time. IKEA lacks a global scaled furniture competitor because flat-pack + owned stores + catalog UX is one integrated system — but e-commerce delivery erodes margin on the model Kamprad optimized for in-store pickup.",
    background="Ben and David begin in Småland, Sweden — Lista culture of minimum resources — tracing Kamprad's matchbox-to-pen mail-order trade (age 5–17), 1943 IKEA registration (Ingvar Kamprad Elmtaryd Agunnaryd), and 1950s furniture catalog price wars that forced the Älmhult showroom.\n\nFlat-pack, self-assembly, and supplier partnerships in Poland transformed mail-order into global big-box retail; Kamprad moved ownership into a foundation structure while remaining frugal icon until death (2018).",
    important_facts=[
        "Only capital ever injected: ~500 Swedish kronor loan (~$63, 1938) for fountain pens — repaid quickly; Ingvar owned 100% until foundation structure; IKEA holds ~€25B cash and owns most real estate (2024).",
        "1953 Älmhult showroom — first mail-order furniture business with physical exhibition; customers could see but not take home (Tesla/Bonobos model decades early); 1956 flat-pack LÖVET table after employee removes legs for transport.",
        "Revenue ~6M kronor (1955) to ~40M kronor (1961) after flat-pack scaling; LACK table ~$9.99 US (2024) uses board-on-frame Polish manufacturing — particle-board sandwich construction.",
        "Germany is IKEA's largest market (not Sweden/US/China); sells ~1B Swedish meatballs/year to extend in-store time; Kamprad dyslexia legend drives product names (Swedish places) vs SKUs.",
        "No global furniture retailer matches IKEA scale in 2024 — fragmented local competitors; model integrates catalog, owned stores, flat-pack logistics, and in-house design.",
    ],
    mental_model={
        "name": "Flat-Pack Cost Cascade",
        "components": "Removing air from furniture (knock-down/KD flat-pack) cuts shipping, damage, and warehouse cost — customer supplies assembly labor. Showroom catalog drives trip intent; meatballs increase dwell time and attachment rate. Vertical design (not just reselling) lets IKEA specify board-on-frame economics. Poland/low-cost sourcing after Swedish supplier boycott (1950s) cemented price leadership. Every margin layer returns to price for 'many people' — Kamprad's triangle: price > selection > convenience.",
        "application": "Retailers competing on convenience (same-day delivery) fight IKEA's optimized pickup model — margin structure assumes customer logistics. For investors, IKEA is inaccessible; watch home-furnishing beneficiaries (PTON-style fatigue inverse: affordable refresh cycles) and suppliers on IKEA volume.",
    },
    competitive_advantage="IKEA wins on integrated cost structure competitors cannot copy piecemeal. Flat-pack requires designing for KD from scratch — not bolting onto traditional furniture. Owned stores + catalog control customer journey; supplier boycott (1960s) forced in-house design and Eastern Europe manufacturing partnerships competitors lacked appetite for.\n\nScale in Germany and urban Europe funds global expansion; simple Scandinavian aesthetic became default modern furniture taste partly because IKEA trained consumers. Foundation ownership removes quarterly pressure; €25B cash buffer absorbs downturns.\n\nWeaknesses: e-commerce shipping of bulky KD boxes compresses margin; labor for assembly falls on customers (love or hate). No true global rival at same price-design-scale triangle — Wayfair asset-light differs (marketplace, delivery cost). Premium design brands (West Elm, MUJI) take upmarket, not volume.\n\nVersus Costco (Kamprad admired), both use loss-leader food (hot dogs/meatballs) and treasure-hunt catalog — IKEA adds self-assembly labor transfer unique to furniture.",
    key_insights=[
        {"view": "Flat-pack was logistics insight, not design fad.", "question": "Why remove table legs?", "answer": "1956 Gillis Lundgren couldn't fit table in car — removed legs, realized storage efficiency. IKEA went all-in on KD across range by late 1950s. Competitors mail-ordering assembled furniture paid breakage and freight — IKEA passed savings as lowest price for quality tier."},
        {"view": "Showroom without takeaway was intentional.", "question": "Why not sell in store initially?", "answer": "1953 Älmhult exhibition let customers touch catalog goods before mail ordering — trust in pre-credit-card era. Kamprad: 'Use catalog to tempt people to exhibition.' P.T. Barnum retail psychology; meatballs added reason to stay."},
        {"view": "Supplier boycott forced vertical design.", "question": "Why own product development?", "answer": "Swedish furniture makers blocked IKEA from trade fairs and pressured suppliers (1960s). Ingvar designed in-house, sourced Poland — board-on-frame LACK at ~$9.99 today. Adversity created moat competitors reselling catalogs couldn't match."},
        {"view": "500 kronor is the only outside capital.", "question": "How did IKEA scale without investors?", "answer": "Positive cash flow from matchboxes → pens → furniture reinvested over 81 years. Kamprad's Lista frugality and foundation structure avoided dilution — parallel Epic/Microsoft capital efficiency in retail."},
        {"view": "Germany scale beats home market.", "question": "Where is IKEA largest?", "answer": "Germany — not Sweden — proving export of Småland price obsession to urbanizing Europe. Urban apartments needed affordable, movable furniture as generational farms ended — IKEA rode 1960s–80s European urbanization."},
    ],
    top_investment_implications=[
        {"ticker": "HD", "direction": "Watch", "confidence": "Low", "thesis": "No public IKEA equity; ~€50B+ private retailer — home-improvement peers (Home Depot) correlate with housing cycles, not IKEA's flat-pack margin model."},
    ],
    golden_quotes=[
        "\"The only capital that ever goes into IKEA\" — 500 kronor (~$63) in 1938, repaid immediately.",
        "\"Use a catalog to tempt people to come to an exhibition, which today is our store\" — Ingvar Kamprad on modern IKEA concept (1953).",
        "\"There is not a single other globally-scaled furniture business in the world\" — Ben on 2024 competitive landscape.",
    ],
    chronology={
        "subject": "Ingvar Kamprad · IKEA",
        "events": [
            {"date": "1926", "event": "Ingvar Kamprad born in Småland, Sweden"},
            {"date": "1938", "event": "500 kronor loan; mail-order pen trading at age 12"},
            {"date": "1943", "event": "IKEA registered (name from initials + farm/village)"},
            {"date": "1947", "event": "Furniture added to mail-order catalog"},
            {"date": "1953", "event": "First Älmhult showroom; meatballs from day one"},
            {"date": "1956", "event": "Flat-pack LÖVET table insight; KD across range"},
            {"date": "1960s", "event": "Poland sourcing; supplier boycott overcome via in-house design"},
            {"date": "1980s", "event": "Global expansion; foundation ownership structure"},
            {"date": "1990s–2000s", "event": "US/China growth; LACK table mass production"},
            {"date": "2018", "event": "Ingvar Kamprad dies; ~€50B+ retailer with €25B cash"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

REST["acq-meta"] = base(
    "acq-meta",
    episode_rating={"overall": 5},
    keywords=["Social Graph", "Mark Zuckerberg", "Digital Advertising"],
    conclusion="Meta connects ~4B monthly and ~3.3B daily active users across Facebook, Instagram, WhatsApp, and Threads — more humans than any entity in history (Roman Empire peaked ~40% vs Meta ~50%). Mark Zuckerberg built on LAMP stack and AIM-era hacking culture; Facebook launched February 4, 2004 at Harvard with domain-gated identity and user-submitted photos. Feed ads and mobile pivot (post-2012 HTML5 miss) created one of two great performance-ad systems; US/Canada ARPU rose ~$11 at IPO to ~$227. Apple ATT (2021) erased ~$232B market cap in one day but Advantage+ restored targeting at scale. Reality Labs lost ~$60B since 2019 on AR/VR bet needing iPhone-level profits to break even. Mark's super-voting control enables turn-based strategy: copy Stories/TikTok, buy Instagram/WhatsApp, open-source Llama to commoditize AI complements. Company 'moves like water' — product as discovery, not pure invention.",
    background="Ben and David study Meta from Mark Zuckerberg's 1984 birth through Civilization/AIM programming, Harvard projects (CourseMatch, FaceMash, thefacebook.com), and expansion college-by-college preserving network quality.\n\nThey cover platform wars (Friendster, MySpace, iPhone), Instagram/WhatsApp acquisitions, mobile/HTML5 crisis at IPO, feed recommender AI, Cambridge Analytica/ATT privacy battles, TikTok competition, and Reality Labs/ORION AR glasses — framing Meta as Microsoft-like multi-bet platform company under founder control.",
    important_facts=[
        "~4B monthly active users, ~3.3B daily actives across family of apps — ~50% of humanity; only ~450M online non-users (~6%) outside China (1.4B) per Ben's TAM math at last reporting.",
        "Facebook launched Feb 4, 2004 at Harvard (harvard.edu emails only); FaceMash preceded it; Winklevoss ConnectU idea not novel — Yale Station, Club Nexus existed; LAMP stack cost ~$100/year to host.",
        "IPO May 2012 at ~$100B market cap; mobile HTML5 app caused ~50% drawdown — feed ads not yet invented; US/Canada ARPU ~$11 at IPO vs ~$227 today; global ARPU ~$44.",
        "Instagram (~$1B, 2012) and WhatsApp (~$19B, 2014) acquisitions; ATT (2021) triggered largest single-day market cap loss ~$232B (Feb 2022 earnings); stock fell ~72% in 2022 before rebound.",
        "Reality Labs ~$60B operating losses since 2019 separate reporting; Orion AR prototype compelling but needs iPhone-scale profits to repay investment; Llama open-source mirrors Open Compute playbook.",
    ],
    mental_model={
        "name": "Turn-Based Platform Discovery",
        "components": "Mark runs Meta like Civilization: maximize turns (engineering speed), learn more per turn than competitors, preserve degrees of freedom (super-voting). Product often discovered (Stories, Reels) not invented. Commoditize complements (LAMP, Llama, Open Compute) to deny suppliers leverage. Multiple parallel bets (AI, AR, ads, social graphs) under one roof because platform control never feels secure — iPhone, ATT, TikTok each existential. Cash generation from feed ads funds bets; founder control prevents Wall Street from starving Reality Labs.",
        "application": "When analyzing Meta, separate core cash machine (scale economies in ads + recommenders) from optionality portfolio (RL, Llama). Competitors need both social graph and AI GPU scale — high barrier. Investor thesis: can Advantage+ and Reels hold attention vs TikTok while RL proves ORION path?",
    },
    competitive_advantage="Meta wins on simultaneous scale in users, data, and ad infrastructure. ~3.3B DAU feeds AI recommenders (TikTok war) and targeting (Advantage+ post-ATT). Instagram/WhatsApp acquisitions removed horizontal social threats; network effects plus creator switching costs lock supply side.\n\nOpen-source Llama lowers AI input costs and prevents OpenAI/Google model tax — repeats Open Compute strategy. Integrity/safety at scale (Farsi hate-speech classifiers) is cornered resource startups cannot replicate.\n\nWeaknesses: brand toxicity, teen mental-health scrutiny, Apple platform tax/ATT, and Mark dependence. No love for Facebook brand but Instagram/WhatsApp usage remains. Reality Labs burns ~$15B+/year with unproven consumer AR timeline.\n\nVersus Google, Meta fights for attention time not search intent — different ad SKU. Versus TikTok, ByteDance matches recommender scale but lacks Meta's global app portfolio and messaging lock-in (WhatsApp).",
    key_insights=[
        {"view": "Meta connects more humans than any empire.", "question": "How does scale compare historically?", "answer": "Roman Empire ~40% of humans at peak; British ~23%; Meta ~4B MAU on ~8B humans — unprecedented reach. Daily actives ~3.3B show engagement not just registration. Growth now requires bringing countries online (internet.org) — only ~6% of online humans not on Meta outside China."},
        {"view": "Domain-gated launch was the seed insight.", "question": "Why beat Friendster/MySpace?", "answer": "thefacebook.com required harvard.edu email — real identity graph; user-submitted photos vs scraped books. Expansion college-by-college kept network dense: either unavailable or excellent. Friendster had scale but dating positioning and technical debt; Mark copied mechanics after seeing market discover them."},
        {"view": "Mobile HTML5 near-death at IPO.", "question": "What broke in 2012?", "answer": "Facebook built mobile in HTML5 pre-feed-ads; native rewrite plus mobile ads saved business. Mark ties this to AI urgency today — platform shifts require painful rewrites. IPO ~$100B → ~50% drawdown before mobile monetization."},
        {"view": "ATT hurt but scale won.", "question": "Did Apple break Meta?", "answer": "Feb 2022 ~$232B single-day cap loss; retail ads doubled in price for some advertisers. Meta's Advantage+ used other signals; most scale player still wins targeting wars. Real threat was TikTok stealing users, not ATT alone."},
        {"view": "Reality Labs is Mark's Blue Origin inside Meta.", "question": "Why spend ~$60B?", "answer": "Platform trauma — iPhone, ATT, Epic fights. Mark wants own hardware/AI stack; ORION glasses credible but financial return needs iPhone-level profit doubled with services. Super-voting lets him fund without activist pressure; ~1% tax on enterprise value annually."},
    ],
    top_investment_implications=[
        {"ticker": "META", "direction": "Long", "confidence": "Medium", "thesis": "~$47B operating income scale; Reels closed TikTok gap; Llama commoditizes AI inputs; RL optionality expensive but founder-controlled — watch teen regulation and Apple dependency."},
    ],
    golden_quotes=[
        "\"Four billion monthly active users… only eight billion humans on earth\" — Ben contextualizing Meta scale.",
        "\"Mark plays the company as if it's a turn-based strategy game\" — research source on Meta product development.",
        "\"Meta moves like water\" — Ben's quintessence after full episode analysis.",
    ],
    chronology={
        "subject": "Mark Zuckerberg · Meta",
        "events": [
            {"date": "1984", "event": "Mark Zuckerberg born; grows up on Long Island coding ZuckNet"},
            {"date": "Sep 1991", "event": "Civilization releases — shapes Mark's strategy metaphor"},
            {"date": "Feb 2004", "event": "thefacebook.com launches at Harvard"},
            {"date": "2005–06", "event": "Expands to colleges; rejects early acquisition offers"},
            {"date": "May 2012", "event": "IPO ~$100B; mobile HTML5 crisis"},
            {"date": "2012", "event": "Instagram acquired ~$1B"},
            {"date": "2014", "event": "WhatsApp ~$19B; FAIR AI lab; Oculus ~$2B"},
            {"date": "2016–18", "event": "Cambridge Analytica; privacy backlash intensifies"},
            {"date": "2021", "event": "Apple ATT implemented; ad targeting disrupted"},
            {"date": "2022", "event": "~72% stock drawdown; first QoQ user decline"},
            {"date": "2024", "event": "Llama open source; Orion AR demo; ~$1.5T market cap recovery"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

REST["acq-acquired-live-from-chase-center-with-daniel-ek-emily-chang-jensen-huang-and-mark-zuckerberg"] = base(
    "acq-acquired-live-from-chase-center-with-daniel-ek-emily-chang-jensen-huang-and-mark-zuckerberg",
    episode_rating={"overall": 4},
    keywords=["Live Special", "Spotify", "YouTube"],
    conclusion="Acquired's September 2024 Chase Center live show (~6,000 seats, JP Morgan Payments) blended podcast meta-commentary with on-stage updates. Daniel Ek revealed Spotify's podcast chart: organic doubling YoY since 2015, subscriber tailwind from Spotify entering podcasting (2019, market leader in ~3 years), and May 2024 Wall Street Journal article as first-ever 'kink' in the growth curve. Emily Chang grilled Ben/David on YouTube (~$5B revenue at episode time vs ~$35–40B now, 55% creator payout), LinkedIn (~$16B revenue, 5x since 2016 acquisition), SpaceX/Starlink (~$6.5B Starlink revenue), and Taylor Swift Inc (~$550M+ annual free cash flow — Eras tour ~$1.1B gross 2023). Jensen Huang corrected the viral 'enriched us all' clip. Mark Zuckerberg closed Act III on Meta strategy, Ray-Ban Meta glasses, and turn-based product discovery — same themes as the dedicated interview episode.",
    background="Ben and David host a three-act arena event in San Francisco: Act I with Jamie Dimon intro and Daniel Ek on podcasting/video strategy; Act II with Emily Chang 'Acquired canon' updates; Jensen Huang surprise; intermission; Act III Mark Zuckerberg interview (also released standalone).\n\nThe format shows Acquired's production (9-hour recordings edited to 3–5 hours) and audience scale — '400 years of listening' in one year per their chart — without replacing deep historical episodes.",
    important_facts=[
        "Chase Center capacity ~6,000; JP Morgan Payments/Jamie Dimon partnership; Acquired organic listener doubling YoY since 2015 per Daniel Ek data — WSJ May 2024 article caused first visible chart kink.",
        "Spotify entered podcasting 2019, became market leader in ~3 years; Ek noted social music (Facebook feed integration) deprioritized vs utility streaming — parallel to Mark platform lessons.",
        "YouTube revenue ~$5B at original Acquired episode vs ~$35–40B run rate at show; pays 55% long-form / 45% Shorts to creators — strategic value to Google exceeds standalone DCF per Ben.",
        "LinkedIn ~$16B revenue (~5x since ~$26B Microsoft acquisition 2016); engagement 5–10x Acquired's other social posts; SpaceX ~$36B valuation at episode vs Starlink alone ~>$36B today (~6,500 satellites).",
        "Taylor Swift ~$100M+ Spotify streaming alone (2023); Eras tour ~$1.1B gross 2023; David estimates ~$550M+ annual FCF — Forbes net worth ~$1.1B vs David's ~$11B EV at Disney 20x multiple debate.",
    ],
    mental_model={
        "name": "Canon Updates vs Origin Stories",
        "components": "Live show updates valuations on prior episodes (YouTube, LinkedIn, SpaceX, Taylor) without re-doing full history — audience present for corrections. Podcast growth benefits from platform expansion (Spotify) and cultural moments (WSJ profile). Founders on stage (Ek, Huang, Zuckerberg) reveal current strategy; Emily Chang adversarial format stress-tests old grades.",
        "application": "For media properties, live events monetize superfans and create marketing spikes — but cannot replace archival depth. Investors should treat on-stage numbers as directional updates; YouTube/LinkedIn strategic value to parent still exceeds reported segment profit.",
    },
    competitive_advantage="Acquired's live format leverages accumulated audience trust built over 9-hour research episodes — competitors cannot replicate overnight. Chase Center/JP Morgan association signals institutional credibility; surprise guests (Jensen) create viral clips feeding podcast funnel.\n\nWeaknesses: live pacing sacrifices narrative depth; arena economics depend on sponsorship; one-night event doesn't scale like software. Spotify relationship mutual — Ek gains prestige, Acquired gains distribution data story.\n\nVersus other business podcasts, Acquired's live show is rare at 6,000-seat scale — moat is brand + research depth + guest access (Mark, Jensen, Ek in one night).",
    key_insights=[
        {"view": "Spotify doubled Acquired's organic curve.", "question": "What did Ek's data show?", "answer": "Classic hockey-stick from 2015 with step-change when Spotify pushed podcasts (~2019) and WSJ May 2024 kink from mainstream press — first external event ever bent Acquired download chart in a decade."},
        {"view": "YouTube grade upgraded to A+ strategically.", "question": "Did Google make money on YouTube?", "answer": "Still unclear profit, but ~$35–40B revenue and AI training data + search second place make non-ownership existential risk for Google — Ben/David raise grade on strategic optionality not DCF."},
        {"view": "Taylor Swift is a cash-flow machine.", "question": "How big is Taylor Inc?", "answer": "Streaming ~$100M+/year from Spotify alone; Eras ~$1.1B gross 2023; David ~$550M FCF estimate vs Forbes ~$1.1B net worth — debate whether Disney 20x FCF multiple applies to single-artist IP."},
        {"view": "LinkedIn outperformed acquisition thesis.", "question": "What are numbers today?", "answer": "~$16B revenue vs ~$3B at acquisition; ads/content ~$5B built post-deal; Kevin Scott now Microsoft CTO — professional graph undervalued in 2016."},
        {"view": "Mark live reinforced Meta DNA.", "question": "What carried to standalone interview?", "answer": "Turn-based strategy, Ray-Ban Meta pivot to on-device AI, open source, Reality Labs conviction — Chase Center format let Mark address 6,000 builders; same through-lines as Mark-only episode."},
    ],
    top_investment_implications=[
        {"ticker": "GOOGL", "direction": "Watch", "confidence": "Medium", "thesis": "YouTube ~$35–40B revenue asset with strategic value (search #2, Shorts, AI data) likely under-earns in segment reporting — live show reaffirms A+ acquisition logic."},
        {"ticker": "MSFT", "direction": "Long", "confidence": "Medium", "thesis": "LinkedIn ~$16B revenue validates 2016 ~$26B deal; professional graph + AI hiring content moat compounding inside Microsoft."},
    ],
    golden_quotes=[
        "\"Over 400 years of Acquired listened to in the past year\" — Ben/David on cumulative listening time stat.",
        "\"YouTube was about $5 billion run rate… now $35–40 billion\" — Emily Chang segment update.",
        "\"Being the big daddy for all sporting events in India\" — Lalit Modi echo in cricket segment; live show cross-pollinates Acquired canon.",
    ],
    chronology={
        "subject": "Acquired · Chase Center Live",
        "events": [
            {"date": "Sep 2024", "event": "Acquired LIVE at Chase Center, San Francisco (~6,000 attendees)"},
            {"date": "Act I", "event": "Jamie Dimon intro; Daniel Ek on podcast growth and Spotify video"},
            {"date": "Act II", "event": "Emily Chang grills on YouTube, LinkedIn, SpaceX, Taylor Swift updates"},
            {"date": "Act II", "event": "Jensen Huang corrects viral clip from prior interview"},
            {"date": "Act III", "event": "Mark Zuckerberg interview — Meta strategy, glasses, AI"},
            {"date": "May 2024", "event": "Wall Street Journal Acquired profile — chart kink per Ek data"},
            {"date": "2019", "event": "Spotify podcast push — Acquired curve inflection"},
            {"date": "2015", "event": "Acquired founded; organic YoY doubling begins"},
            {"date": "2024", "event": "Full live video production released weeks after standalone Mark cut"},
            {"date": "2024", "event": "Hermes-dressed hosts; Jamie Dimon/JP Morgan headline sponsorship"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

REST["acq-the-mark-zuckerberg-interview"] = base(
    "acq-the-mark-zuckerberg-interview",
    episode_rating={"overall": 4},
    keywords=["Mark Zuckerberg", "Meta Strategy", "Open Source"],
    conclusion="The standalone Mark Zuckerberg Chase Center interview (~89 minutes) covers Meta's survival across nine 'death' narratives (MySpace through ChatGPT). Mark describes product creation as discovery chiseled from marble — Stories copied from Snapchat, engineering speed supplies turns. Built on LAMP stack; now largest modern open-source beneficiary via Llama. Mobile HTML5 at 2012 IPO caused ~50% drawdown before native + feed ads. Super-voting enables 20-year horizon — '20 years isn't that long.' Reality Labs spend is platform-independence bet like Blue Origin inside Amazon. Ray-Ban Meta glasses shipped pre-LLM; Mark called Saturday highway to add on-device Meta AI. Meta remains Mark amplifier — misunderstood vs Jobs/Ives or Jensen dynamics.",
    background="Ben and David release Mark's Chase Center Act III early as standalone episode before full live video. Conversation spans Greek motto shirt ('learning through suffering'), existential competition list, open-source philosophy, IPO/mobile crisis, self-criticism prompts, Reality Labs rationale, and founder advice — with post-show reflection on Mark's willingness to discuss history live.\n\nHosts note Meta executives and board attended; format forced unscripted performance unlike podcast retakes.",
    important_facts=[
        "Mark counts nine existential waves: MySpace, Twitter, Instagram, Snapchat, WhatsApp, TikTok, Apple ATT, ChatGPT, etc.; company ~3.3B daily actives across apps at recording.",
        "Ray-Ban Meta smart glasses shipped before public LLM moment; Mark called Ben on a Saturday highway drive to pivot glasses to on-device Meta AI — rapid iteration example.",
        "2012 IPO ~$100B valuation; mobile HTML5 strategy caused ~50% stock drawdown over ~3 months before native apps and feed ads; feed ad not invented pre-IPO.",
        "Meta described as largest beneficiary of modern open source (LAMP historically, Llama now); Mark aligns with commoditizing complements — Open Compute parallel.",
        "Reality Labs spending criticized as cash incineration (~$60B cumulative operating losses since 2019 segment reporting) but Mark frames as multi-decade AR/AI platform; super-voting blocks activist cuts.",
    ],
    mental_model={
        "name": "More Turns, More Learning",
        "components": "Meta wins turn-based strategy game vs competitors: ship fast, absorb brand damage from rough edges, copy what market discovers (Stories/Reels), buy threats (Instagram/WhatsApp). Engineering excellence buys iteration speed; founder control buys time. Open source reduces supplier rent (Llama vs closed AI). Platform independence trauma (iPhone, ATT) justifies RL hardware spend despite financial drag.",
        "application": "Founder-led consumer tech with super-voting can optimize for optionality over near-term EPS — but requires Mark-level learning rate. Investors weigh META core ads (high ROIC) vs RL call option with negative carry.",
    },
    competitive_advantage="Mark's sustained control and Meta's engineering density let the company copy and out-execute feature threats once identified — Snapchat Stories lag closed fast. WhatsApp/Instagram removed network competitors; Llama/open source lowers AI COGS vs closed-model rivals.\n\nLive arena interview itself signals confidence — Meta treats Acquired audience as strategic community. Weakness: public narrative lags Apple/NVIDIA on founder myth; brand damage from privacy eras persists.\n\nVersus TikTok, Meta matched recommender investment; vs Apple, still platform-dependent on iOS distribution and ATT rules.",
    key_insights=[
        {"view": "Product is discovery, not invention.", "question": "Is David inside the marble?", "answer": "Mark says market often discovers format (Stories); Meta's job is tooling + speed to chisel. Orion/VR requires invention; social software mostly fast following with superior execution — controversial but historically accurate for Meta."},
        {"view": "Open source is strategic defense.", "question": "Largest OSS beneficiary?", "answer": "Facebook built on LAMP; Llama open weights prevent OpenAI/Google model tax — repeats strategy of commoditizing complements per Joel Spolsky framework. Android parallel: open enough to deny rivals exclusive AI supply."},
        {"view": "IPO mobile miss informs AI urgency.", "question": "HTML5 lesson?", "answer": "2012 mobile web bet nearly broke company at ~$100B IPO valuation; native + ads recovery took years. Mark applies scar tissue to AI — cannot outsource core model capability."},
        {"view": "Meta is still Mark's amplifier.", "question": "Misunderstood vs Apple/NVIDIA?", "answer": "Ben/David post-show: public doesn't treat Meta as founder-driven genius narrative like Jobs/Jensen — but organization amplifies Mark output 10,000x; executive team all-in on live event."},
        {"view": "20 years is early innings.", "question": "Would rename Meta today?", "answer": "Mark commits to metaverse/AI name despite ridicule — super-voting lets him ignore short-term brand polls; compares duration to Buffett, not typical founder exit pattern."},
    ],
    top_investment_implications=[
        {"ticker": "META", "direction": "Long", "confidence": "Medium", "thesis": "Founder control + ~3.3B DAU + Llama hedge on AI supply; RL drag capped by Mark's commitment — interview confirms strategic patience beyond quarterly optics."},
    ],
    golden_quotes=[
        "\"By our count… more existential challenges than any meaningful company in history\" — David to Mark on nine platform waves.",
        "\"Those glasses… could we put Meta AI in them running on device\" — Mark's Saturday highway call on Ray-Ban pivot.",
        "\"Twenty years actually isn't that long\" — Mark on founder tenure at Chase Center.",
    ],
    chronology={
        "subject": "Mark Zuckerberg · Chase Center Interview",
        "events": [
            {"date": "Sep 2024", "event": "Live interview at Chase Center (~6,000 audience)"},
            {"date": "2004", "event": "Facebook founded at Harvard"},
            {"date": "May 2012", "event": "IPO ~$100B; mobile HTML5 crisis"},
            {"date": "2012–14", "event": "Instagram and WhatsApp acquisitions"},
            {"date": "2014", "event": "Oculus/FAIR bets on next platform"},
            {"date": "2016", "event": "Cambridge Analytica era privacy scrutiny begins"},
            {"date": "2021", "event": "Apple ATT privacy changes"},
            {"date": "2022", "event": "Meta stock ~72% drawdown; Reels vs TikTok"},
            {"date": "2023", "event": "Llama 2 open-source release; AI platform bet accelerates"},
            {"date": "2024", "event": "Ray-Ban Meta + Llama; Orion demo; live Acquired interview"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

REST["acq-microsoft-volume-ii"] = base(
    "acq-microsoft-volume-ii",
    episode_rating={"overall": 5},
    keywords=["Internet Explorer", "Antitrust", "Azure"],
    conclusion="Microsoft Volume II covers 1995–2014: Internet tidal wave, browser wars, antitrust breakup order, and Ballmer CEO era that tripled revenue while stock flatlined. Netscape IPO Aug 1995 at ~$3B cap; IE bundled free Dec 1995 — Netscape stock dropped ~33% and never recovered. Judge Jackson Nov 1999 found Windows monopoly; June 2000 ordered breakup — market cap fell ~$600B to ~$270B (~55%) before settlement. Steven Sinofsky's 1994 Cornell snowstorm memo sparked Bill's internet religion; Jay Allard's Jan 1994 memo laid embrace-extend strategy before Netscape existed. Ballmer inherited ~80x earnings peak, DOJ trauma, options mess — built Azure via Ray Ozzie skunkworks outside Server & Tools. Satya Feb 2014 CEO; MSFT ~$465/share, ~$3.5T cap ten years later with Azure ~half value. Ben argues 'lost decade' narrative ignores enterprise tripling and cloud seed — Satya fixed storytelling not fundamentals.",
    background="Ben and David continue from Windows 95 celebration into MSN vs open web, Mosaic/Netscape rise, Spyglass-licensed IE, and DOJ trials (FTC 1990, consent 1994, IE tying 1998, Jackson breakup order 2000). Ballmer CEO 2000–2014 spans Xbox, search/mobile misses, Nokia ~$7B write-down, stack-ranking culture, and Azure incubation.\n\nTwenty-plus research interviews inform analysis: Gates deposition videos shaped public opinion; Apple 1997 $150M investment bought IE default on Mac displacing Netscape.",
    important_facts=[
        "Netscape Aug 9, 1995 IPO ~$3B cap; grew 1M to 15M users in one year; Marc quote wanted Windows as ' poorly debugged device drivers.'",
        "Dec 7, 1995 Bill announces IE free bundled in Windows 95 — Netscape stock ~-33% same day, never recovered; IE market share eventually >90%.",
        "Nov 1999 Jackson finding of fact: Windows monopoly via network effects; June 7, 2000 breakup order (OS vs apps companies) — MSFT cap ~$600B to ~$270B by late 2000; settlement 2001 after 9/11 push.",
        "Apple Aug 1997: Microsoft $150M investment (~8% of ~$2B Apple), IE default on Mac, Office commitment — Steve Jobs saved Apple; Google founded 1998.",
        "Ballmer CEO 2000–2014: revenue/profits ~3x; stock flat due to multiple compression from ~80x earnings entry; Azure skunkworks ~2006; Satya CEO Feb 4, 2014; MSFT ~$3.5T cap by 2024.",
    ],
    mental_model={
        "name": "Embrace, Extend, Bundle",
        "components": "Microsoft's internet strategy: detect exponential platform (Sinofsky snowstorm, Allard memo), ship browser tied to Windows OEM channel, price free to cut off Netscape air supply. Legal gray zone — features vs tying. Same pattern failed in mobile/search where distribution wasn't owned. Enterprise EA and Azure later reused bundling at zero marginal cost. Narrative matters: Ballmer tripled business without stock credit until Satya's 'mobile-first, cloud-first' repetition.",
        "application": "Platform owners win when distribution channel competes with you — lesson for iOS/App Store today. Investors evaluating MSFT legacy: separate consumer Ls from enterprise/cloud Ws; Azure born outside Server & Tools shows incumbent disruption requires structural separation.",
    },
    competitive_advantage="1995–2000 Microsoft owned PC OEM channel (>90% share) — insurmountable for Netscape selling browser alone. IE integration + AOL deals (1996) closed distribution loops. Enterprise switching costs compounded post-browser into Active Directory/Exchange era Ballmer built.\n\nWeaknesses: missed mobile (iPhone 2007), search (Google), social; Vista/Longhorn execution failure; DOJ hangover and stack-ranking internal warfare. Public hated Microsoft while CIOs kept buying.\n\nVersus Google/Apple post-2007, Microsoft lost consumer developer mindshare but preserved enterprise lock-in funding Azure. Antitrust remedy never split company — operational 'split' was Ballmer enterprise vs Bill consumer until Satya unified story.",
    key_insights=[
        {"view": "Netscape lost when distribution competed.", "question": "Why did free IE win?", "answer": "Windows >90% share; IE bundled Dec 1995 free; Netscape sold servers — browser was loss leader for platform dream. When OEM channel turned on Netscape (AOL 1996 IE deal, Apple 1997 default), air supply cut. Lesson: don't build on another platform's distributor if they can clone you."},
        {"view": "Breakup order was real then forgotten.", "question": "Was Microsoft split?", "answer": "Judge Jackson June 2000 ordered OS/apps separation — Ballmer and Gates assigned different companies in ruling; cap halved. Judge Jackson removed for secret press meetings; 2001 settlement avoided split. 15 months world believed breakup imminent."},
        {"view": "Ballmer era tripled business, not failed.", "question": "Why flat stock?", "answer": "Inherited ~80x P/E at bubble peak; profits grew ~3x 2000–2014 but multiple compressed. Consumer narrative (Zune, Bing, Phone) drowned Azure/enterprise truth. Ben: evaluating Ballmer like buying at all-time-high multiple — unfair grade."},
        {"view": "Azure required outside incubation.", "question": "Why not Server & Tools?", "answer": "Ray Ozzie ~2006 team separate from Windows Server cash cow — same pattern Ballmer wished for mobile. Satya (then head of STB) opposed Nokia ~$7.5B; board lacked support; Satya CEO Feb 2014 as clean break."},
        {"view": "Gates deposition was PR disaster.", "question": "Why did tapes matter?", "answer": "Bill argued over 'definition of definition' — intended for transcript only but video leaked; Boies played clips shaping judge/press perception. Antitrust fight hardened Microsoft aggression while consumer taste shifted to Google/Apple aesthetics."},
    ],
    top_investment_implications=[
        {"ticker": "MSFT", "direction": "Long", "confidence": "High", "thesis": "Volume II shows antitrust survived, Azure seeded, enterprise moat intact — today's ~$3.5T cap pays Ballmer-era cloud/EA foundation; Satya narrative unlock not fundamental rebuild."},
        {"ticker": "GOOGL", "direction": "Watch", "confidence": "Medium", "thesis": "Netscape/browser war winner of platform layer post-PC; MSFT failed to contain search/mobile — Google captured post-IE platform economics MSFT feared from Netscape."},
    ],
    golden_quotes=[
        "\"Netscape will reduce Windows to a set of poorly debugged device drivers\" — Marc Andreessen 1995 press cycle.",
        "\"Exponential phenomena cannot be ignored\" — Bill Gates company value after 1994 internet offsite.",
        "\"Microsoft was ordered… to split up\" — Ben on June 2000 Jackson remedy lost to history.",
    ],
    chronology={
        "subject": "Microsoft · Volume II (1995–2014)",
        "events": [
            {"date": "Jan 1994", "event": "Jay Allard Internet memo; Mosaic exponential growth noted"},
            {"date": "Feb 1994", "event": "Sinofsky snowstorm at Cornell — kids on Internet"},
            {"date": "Aug 1995", "event": "Windows 95 launch; Netscape IPO ~$3B"},
            {"date": "Dec 1995", "event": "IE free+bundled; Netscape stock crashes ~33%"},
            {"date": "Aug 1997", "event": "Apple MSFT deal — $150M, IE default on Mac"},
            {"date": "May 1998", "event": "DOJ broad antitrust suit filed"},
            {"date": "Nov 1999", "event": "Jackson monopoly finding of fact"},
            {"date": "Jun 2000", "event": "Breakup order; MSFT cap ~$600B→~$270B"},
            {"date": "Jan 2000", "event": "Ballmer CEO; Gates chief architect"},
            {"date": "2006", "event": "Azure incubation under Ray Ozzie"},
            {"date": "Feb 2014", "event": "Satya Nadella CEO; Ballmer retires"},
            {"date": "2024", "event": "Microsoft ~$3.5T market cap; most valuable company"},
        ],
    },
    review_notes="Manual GPT Acquired batch v2 — template v5.1-acquired",
)

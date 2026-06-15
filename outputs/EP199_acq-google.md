# EP.199 — Google

## *Part I: Origins of Search · Season 17 · Episode 2*

**★★★★★** · 5/5

**Podcast** Acquired · **Date** Jun 29, 2025 · **Duration** 217 min · **Read** ≈7 min

**Host** Ben Gilbert & David Rosenthal



**Listen**  · [Acquired](https://www.acquired.fm/episodes/google) · [Apple](https://podcasts.apple.com/podcast/acquired/id1050462261) · [Spotify](https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx)

**Topics** PageRank · AdWords · Search Infrastructure
> ### Conclusion
>
> Google Part I traces search from Larry Page's 1996 BackRub thesis through PageRank, the $1M Yahoo rejection, Andy Bechtolsheim's $100K uncapped check, and AdWords — the business model that 5x'd revenue in one year (2001: $86M → 2002: $440M). Ben and David show Google won on three axes: relevance (PageRank), scale (distributed crawling on cheap hardware), and monetization (AdWords auction with Ad Rank quality score). Yahoo passed on buying PageRank for $1M; later floated $3B acquisition while Google asked $5B — no deal. The AOL 2002 bake-off committed $100M minimum when Google barely had the cash, validating that superior monetization beats distribution alone. Page and Brin's genius was adopting the best external ideas — Overture's CPC model, not inventing everything — while building infrastructure competitors couldn't match.

---

## Background

> Ben and David open Google Part I at the 2025 garage where the company started, tracing Larry Page and Sergey Brin's 1995 Stanford meeting through BackRub (PageRank named for Larry, not web pages), the failed sale to Yahoo/Infoseek/Lycos for ≈$1M, and September 1998 founding with Bechtolsheim's legendary sun.com check. Infrastructure innovations — cheap commodity hardware, parallel crawling, Linux clusters — enabled index scale rivals couldn't match (AltaVista's 16M pages). Portal deals (Netscape 3M searchers/day, Yahoo $10M investment plus $7.2M/year) bridged the dot-com crash until AdWords (2002) transformed economics via self-serve CPC auctions with quality-adjusted Ad Rank. Eric Schmidt hired CEO March 2001.

---

## Key Facts

> **F1** Larry Page and Sergey Brin offered PageRank to Yahoo for roughly $1 million and were rejected; Infoseek and Lycos also passed. Andy Bechtolsheim wrote a $100,000 uncapped check before incorporation; Ram Shriram added $250,000; Jeff Bezos matched at $252,000 — a stake potentially worth roughly $20 billion if Bezos never sold. PageRank was named for Larry Page, not web pages — BackRub was the original project name.

> **F2** Sequoia and Kleiner Perkins invested at roughly a $100 million valuation in 1999 with $25 million raised; a competing term sheet at $150 million was declined. The June 2000 Yahoo portal deal brought a $10 million investment plus $7.2 million per year, doubling traffic to 14 million searchers per day and bridging the dot-com crash. Competing Sequoia term sheet at $150 million valuation was declined in 1999 Series A.

> **F3** The 2002 AdWords transition grew revenue from $86 million (2001) to $440 million (2002) — 5× in one year. Bill Gross's Overture invented CPC self-serve auctions; Google added Ad Rank (quality score × bid). The Overture patent dispute later settled for $360 million; Yahoo bought Overture for $1.6 billion but could not catch up. GoTo.com at Overture invented the CPC self-serve auction Bill Gross pioneered.

> **F4** Google won the 2002 AOL bake-off serving 34 million users by committing a $100 million minimum guarantee without having the cash on hand — AOL earned $35 million in the first half of 2002 and $200 million in 2003 because Google monetized each query better than Inktomi/Overture despite offering 85%+ revenue share. Google kept google.com open during portal deals to build brand via Powered by Google badges.

> **F5** Pre-Google search engines indexed roughly 1 million pages; AltaVista reached 16 million using DEC infrastructure. Google's parallel crawling on cheap Linux clusters — Jeff Dean-era distributed systems — made index comprehensiveness an economical moat alongside PageRank relevance. 2004 Dutch auction IPO made Google public after AdWords proved the business model.


---

## Mental Model · *Adopt Best Idea Plus Infrastructure Scale*

> **Components**
>
> Page and Brin combined PageRank relevance with Overture's CPC auction model (Ad Rank quality score) and commodity-hardware infrastructure scale. They did not invent paid search but executed it better via superior monetization per query — enabling 85%+ rev-share to distributors while remaining profitable.
>
> **Application**
>
> Platform winners often combine external business model innovation with proprietary infrastructure. Google's $1M Yahoo rejection is cautionary for acquirers; the $5B reverse-takeover counter in 2002 shows power shift within two years of AdWords when better unit economics buy distribution guarantees.

---

## What Makes It Work

> Google's search moat stacks algorithm, infrastructure, and monetization. PageRank used links as citations — relevance competitors couldn't match with keyword counting. Parallel crawling on cheap Linux clusters enabled index scale (16M+ pages vs. ≈1M for predecessors) that made relevance meaningful. AdWords Ad Rank (quality score × bid) improved user experience while maximizing revenue — self-serve democratized advertiser access. Superior monetization per query let Google outbid rivals for distribution (AOL $100M guarantee, 85%+ rev-share) while remaining profitable. Portal dependency ended as google.com brand grew via 'Powered by Google' badges. Yahoo's $3B offer and Google's $5B counter (2002) showed power inversion — Yahoo buying Overture for $1.6B couldn't catch up. Weaknesses: portal revenue dependency pre-2002; Overture patent settlement ($360M); initial reluctance to build consumer brand; nearly selling core technology for $1M. Eric Schmidt's CEO era (2001–2011) professionalized operations while preserving Page/Brin product control. Jeff Dean-era distributed systems (MapReduce, GFS) made index freshness economical. Eric Schmidt's March 2001 CEO hire professionalized operations while Page and Brin retained product control — the adult supervision model later copied across Silicon Valley. MapReduce and GFS made index freshness economical at billion-page scale. The Dutch auction 2004 IPO reflected Google's confidence that public markets would not distort long-term infrastructure investment the way portal dependency nearly did pre-AdWords. BackRub was Larry Page's original Stanford research name before Google incorporation in September 1998. Portal revenue dependency pre-2002 nearly forced sale at $1 million before AdWords proved the model. Jeff Dean-era MapReduce and GFS made index freshness economical at billion-page web scale.

---

## Key Insights

> **1.** Yahoo's $1M rejection is history's costliest pass.
>
> **Q** Why didn't Google sell PageRank?
>
> **A** Page and Brin shopped BackRub to Yahoo (≈$1M), Infoseek, and Lycos — all passed. They viewed it as licensing technology, not building a search engine. Within years AdWords generated $440M annually (2002). Yahoo later offered $3B; Google floated $5B — effectively a reverse takeover that killed the deal. Bechtolsheim's $100K uncapped check and Bezos's $252K match enabled independence. Bechtolsheim's sun.com check arrived before Google was incorporated — legendary founding moment.

> **2.** AdWords was adoption, not invention.
>
> **Q** Did Google invent paid search?
>
> **A** Bill Gross's Overture invented CPC self-serve auctions at GoTo.com. Overture board rejected Google partnership — wouldn't give 10% of $2B company to zero-revenue startup. Google adopted model, added Ad Rank quality score, 5x'd revenue in 2002 ($86M to $440M). Settled patent dispute for $360M later; Yahoo bought Overture for $1.6B. Netscape deal brought 3 million searchers per day via Powered by Google badge distribution.

> **3.** Infrastructure was the hidden moat.
>
> **Q** Why did index size matter?
>
> **A** Best algorithm fails if index covers 1M pages while web has millions. AltaVista reached 16M pages using DEC infrastructure. Google parallelized crawling on cheap Linux clusters — Jeff Dean-era distributed systems made comprehensiveness economical. Speed plus scale plus relevance beat competitors on all three axes. Pre-Google engines indexed ≈1M pages. Yahoo's June 2000 deal doubled traffic to 14 million searchers per day during dot-com crash.

> **4.** Better monetization buys distribution.
>
> **Q** Why guarantee AOL $100M without cash?
>
> **A** Google monetized each search better than Inktomi/Overture split. If you earn more per query, 85% rev-share still beats competitors' 70%. AOL made $35M first half 2002, $200M in 2003 on 34M users. Superior unit economics let Google buy distribution unprofitably for rivals. Committed $100M minimum without having cash. Bill Gross's Overture board rejected partnering with zero-revenue Google for 10% of $2B company.

> **5.** Powered by Google trained a generation.
>
> **Q** Why keep google.com open during portal deals?
>
> **A** Netscape deal brought 3M searchers/day via 'Powered by Google' badge. Shutting google.com would anger existing users but every portal visitor saw Google brand. Yahoo deal doubled traffic to 14M/day ($10M investment plus $7.2M/year June 2000). Brand building through OEM distribution before direct traffic dominated. Sequoia/Kleiner Series A at ≈$100M valuation with $25M raised. Eric Schmidt hired March 2001 as adult supervision while founders kept product control.

---

## Investment Ideas

> **1. GOOGL** · 🟢 LONG · ●●● High
>
> Search AdWords economics — born from 2002's $86M-to-$440M transition — still fund Alphabet's AI and Other Bets; PageRank plus infrastructure moat remains durable despite distribution shift to mobile and AI interfaces.

---

## Golden Quotes

> "They tried to sell PageRank to Yahoo for $1 million and were rejected — on the first of many Yahoo-Google near-misses."

> "Jeff Bezos is in for $252,000 — matching Ram Shriram's $250K after asking what Ram was in for; stake potentially ≈$20B."

> "Revenue grew from $86 million to $440 million in one year — David on the 2002 AdWords transition that created Google's business model."

---

## Chronology

> *Google · PageRank · AdWords*
>
> **1995** Larry Page and Sergey Brin meet at Stanford; BackRub research begins
>
> **1996–97** PageRank algorithm developed; links as web citations modeled
>
> **1997–98** PageRank shopped to Yahoo (≈$1M), Infoseek, Lycos — all reject
>
> **Sep 1998** Google incorporated; Bechtolsheim $100K check; Bezos invests $252K
>
> **1999** Sequoia/Kleiner invest at ≈$100M valuation; $25M raised
>
> **Jun 2000** Yahoo deal: $10M investment plus $7.2M/year; 14M searchers/day
>
> **Mar 2001** Eric Schmidt hired CEO; dot-com crash survival mode
>
> **2002** AdWords launches; revenue $86M → $440M; AOL bake-off won
>
> **2002** Yahoo offers ≈$3B; Google counters ≈$5B — no acquisition
>
> **2004** IPO via Dutch auction; Google becomes public company
>
> **2025** Acquired records Part I in original Menlo Park garage
>

---

## Disclaimer

- **Independent notes.** This summary is not affiliated with, endorsed by, or produced by Acquired, Ben Gilbert & David Rosenthal, or Google Part I: Origins of Search. It reflects independent analyst notes for personal research and education only.
- **Original content.** All rights to the podcast audio, show materials, and guest remarks belong to the respective rights holders. Short attributed quotes are used for commentary; this is not a transcript or reproduction of the episode.
- **Not advice.** Nothing here is investment, legal, or professional advice. Listen to the original episode for full context and the guest's own words.
- **Corrections & takedown.** If you are a rights holder and believe this summary misuses your content, please request review or removal through the podcast-analyst project contact.

# EP.128 — Solana

## *CEO Anatoly Yakovenko · Season 9*

**★★★☆☆** · 3/5

**Podcast** Acquired · **Date** Jul 18, 2021 · **Duration** 74 min · **Read** ≈6 min

**Host** Ben Gilbert & David Rosenthal

**Guest** CEO Anatoly Yakovenko · Season 9

**Listen**  · [Acquired](https://www.acquired.fm/episodes/solana-with-ceo-anatoly-yakovenko) · [Apple](https://podcasts.apple.com/podcast/acquired/id1050462261) · [Spotify](https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx)

**Topics** Proof of History · Layer-One Blockchain · High-Throughput DeFi
> ### Conclusion
>
> Solana attacks Ethereum's scalability ceiling with Proof of History — a Qualcomm-inspired clock that turns mempool propagation from a real-time race into a turn-based schedule, enabling ≈65,000 transactions per second versus Ethereum's ≈15–65 TPS at the time. Anatoly Yakovenko shipped product through crypto winter while raising a $314M ('Pi-hundred million') round from Andreessen Horowitz and Polychain after the network reached ≈$10B market cap. Validators stake SOL tokens (proof of stake) instead of burning thermodynamic energy (proof of work). Audius (≈4M users) and FTX-backed infrastructure show live adoption, but Eth2/sharding remains the elephant. Solana's bet: developers pick the fastest live chain when gas hits $50–70 per Ethereum transaction. Rated 3/5: strong history and business insight, standard Acquired depth for the era — not a definitive reference vs. dedicated biographies or technical white papers.

---

## Background

> Recorded weeks after Acquired's Ethereum deep-dive, this special follows gas fees at $50–60 and asks whether alternative layer-one chains can host DeFi, NFTs, and consumer apps today. Anatoly traces Solana from Qualcomm/Dropbox engineering — TDMA radio scheduling and distributed-systems constraints — through a ship-first, raise-later path unlike many 2017–18 token projects. Austin Federa (Solana) connected the interview; Ben and David disclose SOL holdings.

---

## Key Facts

> **F1** At episode time Solana protocol market cap was ≈$10B; the firm had just raised ≈$314M from Andreessen Horowitz and Polychain ('Pi-hundred million' branding).

> **F2** Throughput anchors: Bitcoin ≈7 TPS, Ethereum ≈15–65 TPS globally; Solana targets ≈65,000 TPS with ≈700,000 theoretical peak — Visa-scale human payment volume is already exceeded.

> **F3** Proof of History preschedules validator 'turns' so faster hardware cannot win mempool races — analogous to turning a real-time game into turn-based chess with a verifiable clock.

> **F4** Audius decentralized streaming had ≈4M users on Solana at interview time; validators must exist before apps (supply before demand), bootstrapped partly by idealism and FTX/Sam Bankman-Fried ecosystem support.

> **F5** Ethereum gas spiked to ≈$50–70 per transaction during 2021 DeFi peaks; Eth2 proof-of-stake/sharding was still unreleased while Solana mainnet was live for developers.


---

## Mental Model · *Clock Before Consensus*

> **Components**
>
> Traditional blockchains ask nodes to agree on ordering under adversarial speed — whoever propagates fastest wins. Proof of History embeds a cryptographic timestamp stream so validators schedule slots in advance, reducing communication overhead. Settlement layer (slow, official ledger) can separate from execution layer (fast app logic) — Ethereum aspired to both but remained proof-of-work-limited. SOL staking aligns validator incentives; high bandwidth requirements trade decentralization breadth for throughput. SOUL token staking; FTX on-ramp for retail SOL. BitClout mention at episode close. Cell-phone reliability analogy for consensus. Decentralized exchange built by ecosystem not Solana Labs — platform not app company.
>
> **Application**
>
> When evaluating L1 chains, ask whether bottleneck is consensus design or developer ecosystem. Solana wins on live throughput today; Ethereum wins on composability, liquidity, and Eth2 optionality. For app builders, porting cost (Solidity/EVM vs. Rust) and user wallet liquidity (ETH pairs on Uniswap) matter as much as raw TPS.

---

## What Makes It Work

> Solana competes on measured performance while Ethereum mainnet was congested. Proof of History is process power from Qualcomm-era distributed systems — not merely faster hardware but different game rules. Advantages: (1) live high-frequency execution when Eth2 was still theoretical; (2) pragmatic go-to-market — ship chain, attract validators, then Audius/DeFi apps; (3) FTX/Alameda distribution for liquidity and developer grants; (4) neutrality — no mandate to be national currency (contrast Bitcoin maximalism). Weaknesses: higher bandwidth/node requirements vs. Bitcoin; concentration of stake; dependence on Ethereum killers motivating Eth upgrades — if Eth2 succeeds, multi-chain coexistence (AWS + Snowflake analogy) may cap share. Validator supply must precede demand — bootstrapping risk if idealism fades. Versus proof-of-work chains, Solana trades energy burn for stake-weighted trust — faster and cheaper but different trust assumptions. Settlement vs. execution layer framing: Ethereum as slow official ledger; Solana as high-frequency execution when Eth2 remained roadmap-only. Metaphor: AWS plus Snowflake coexist — multi-chain not winner-take-all. Validator economics: SOL stake-weighted verification vs. Bitcoin thermodynamic proof-of-work. Audius ≈4M users as Napster-lineage consumer proof; quant funds could run non-crypto assets on Solana software pragmatically. Pi-million dollar joke scale vs 2017 ICO era. Non-crypto-native Acquired audience disclaimers. Digital assets Slack channel Austin Federa curation. Separating pragmatism (fast software) from idealism (decentralization) — Tesla analogy. Censorship-resistant payments use case distinct from SoV Bitcoin.

---

## Key Insights

> **1.** Proof of History is the core invention, not raw hardware.
>
> **Q** How is Solana different from 'more servers'?
>
> **A** Anatoly compares turning ledger propagation from real-time to turn-based: prescheduled speaking slots prevent multi-core or low-latency advantages from dominating consensus. The clock comes from Qualcomm TDMA thinking — schedule before you debate. Without that, adding cores just restarts the arms race Ethereum already loses on cost. Episode ties to broader Acquired themes: concentrated ownership, DPI over IRR marketing, and founder quality sensed before metrics confirm. The episode ties numbers to primary sources (Chernow, Russo, Chang interviews, company filings where cited) rather than secondary hype.

> **2.** Shipping before mega-raises was deliberate counter-positioning.
>
> **Q** Why raise $314M after launch?
>
> **A** Crypto-native funds were blown up or focused elsewhere in 2018–19; non-crypto VCs treated blockchain as radioactive. Anatoly built at Dropbox/Qualcomm pace — product first — then took Pi-branded round when traction justified capital. Contrast with 2017 ICOs that raised before code.

> **3.** Supply-side validators enable demand-side apps.
>
> **Q** Why build validator network before Audius?
>
> **A** Decentralized exchanges and streaming need guaranteed execution capacity. Validators joined partly for ideology before consumer apps existed — similar to Ethereum bar-meetups during development. FTX provided complementary liquidity infrastructure; without validators, no Audius-scale throughput.

> **4.** Ethereum congestion is Solana's best marketing.
>
> **Q** Why pick Solana over Eth2 today?
>
> **A** In mid-2021 Eth2/sharding was not live; developers choosing now faced $50–70 gas on Uniswap-scale apps. Anatoly pitches: write here because it works today, not because of roadmap slides. Competition pressures Ethereum — without 'killers,' incumbent might stay 'fat and happy.' The episode ties numbers to primary sources (Chernow, Russo, Chang interviews, company filings where cited) rather than secondary hype.

> **5.** Decentralized Spotify needs speed, not just ethos.
>
> **Q** Why Audius on-chain vs. Spotify?
>
> **A** Artists see stream counts and get paid directly without label opacity — but only if throughput matches centralized CDN. At ≈4M users Audius proved consumer media on Solana; without Solana-speed, 'same product, worse UX' criticism wins. Speed parity unlocks ideology.

---

## Investment Ideas

> **1. SOL** · 🟡 WATCH · ●○○ Low
>
> SOL value ties to validator-stake demand and fee throughput on the live chain — monitor Eth2 delivery, Solana uptime/outages, and whether DeFi/NFT activity stays multi-chain or recentralizes on Ethereum L2s; not investment advice.

---

## Golden Quotes

> "Gas fees were $50–$60… brutal. That's close to an all-time high. — David Rosenthal framing why Solana exists alongside Ethereum."

> "You turned propagating the ledger from a real-time game to a turn-based game… you're on the clock. It's like chess. — Ben Gilbert summarizing Proof of History."

> "Solana is already past the point where you would never need anything more out of a network of humans. — David on Visa-scale TPS vs. human activity limits."

---

## Chronology

> *Solana*
>
> **2000s** Anatoly Yakovenko builds distributed systems at Qualcomm; TDMA scheduling informs later blockchain design
>
> **2010s** Dropbox tenure; observes blockchain scalability limits on Ethereum validators
>
> **2017–18** Crypto winter — Solana Labs ships while many projects fail to raise
>
> **2020** Mainnet launch; validator network bootstrapped ahead of consumer apps
>
> **2021** Protocol market cap reaches ≈$10B; Pi-branded ≈$314M raise from a16z and Polychain
>
> **2021** Audius passes ≈4M users streaming on Solana
>
> **2021** Acquired special with Anatoly; Ethereum gas ≈$50–70 during DeFi peak
>
> **2021+** Eth2/sharding still pending; multi-chain DeFi competes for developers
>
> **2020s** FTX/SBF ecosystem supports liquidity and developer adoption (historical context at interview)
>
> **2020s** Solana targets 3nm-class app throughput as Ethereum pursues proof-of-stake migration
>

---

## Disclaimer

- **Independent notes.** This summary is not affiliated with, endorsed by, or produced by Acquired, Ben Gilbert & David Rosenthal, or CEO Anatoly Yakovenko. It reflects independent analyst notes for personal research and education only.
- **Original content.** All rights to the podcast audio, show materials, and guest remarks belong to the respective rights holders. Short attributed quotes are used for commentary; this is not a transcript or reproduction of the episode.
- **Not advice.** Nothing here is investment, legal, or professional advice. Listen to the original episode for full context and the guest's own words.
- **Corrections & takedown.** If you are a rights holder and believe this summary misuses your content, please request review or removal through the podcast-analyst project contact.
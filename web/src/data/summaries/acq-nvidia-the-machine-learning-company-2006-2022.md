# EP.149 — Nvidia

## *Part II: The Machine Learning Company (2006-2022) · Season 10 · Episode 6*

**★★★★☆** · 4/5

**Podcast** Acquired · **Date** Apr 20, 2022 · **Duration** 132 min · **Read** ≈6 min

**Host** Ben Gilbert & David Rosenthal



**Listen**  · [Acquired](https://www.acquired.fm/episodes/nvidia-the-machine-learning-company-2006-2022) · [Apple](https://podcasts.apple.com/podcast/acquired/id1050462261) · [Spotify](https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx)

**Topics** CUDA · Deep Learning · AI Infrastructure
> ### Conclusion
>
> Part II opens with Jensen's Omniverse vision — simulating physical worlds on one GPU — then rewinds to 2006: Jensen bets company on CUDA while gaming still works, stock drops ≈80% in financial crisis, Tegra/Zune HD and Icera mobile misadventures sidetrack but don't save the firm. CUDA (development began 2006) is free, closed-source, hardware-locked — Apple/Intel alliance analogy — with ≈1,100 employees titled CUDA today per LinkedIn search. AlexNet (2012 ImageNet) implemented in CUDA on Nvidia GPUs is the "big bang" for AI; Fei-Fei Li's ImageNet and Toronto team beat error rate by >10 points (≈15% vs ≈25%+ prior). Data-center revenue, RTX ray tracing, crypto segmentation, automotive (≈$1B revenue cited), Omniverse, and hyperscaler custom-silicon bear cases follow. Nvidia runs ≈37% operating margins on ≈$1B annual CapEx vs Apple's ≈$10B and TSMC's ≈$30B — fabless software economics. Power stew: scale economies on CUDA R&D, switching costs, cornered resource (CUDA only runs on Nvidia). A+ shareholder case requires believing physical-world AI (AV,

---

## Background

> Season 10 Episode 6 continues Nvidia after 2006 AMD-ATI deal and Intel Larrabee threat. Jensen expands mission beyond gaming while Wall Street loved Xbox-era growth to ≈$5–6B market cap then punished CUDA spend — ≈80% drawdown in 2008, another ≈50% on 2011 earnings miss. CUDA built a full stack (API, libraries, frameworks) over six-plus years before usefulness — compared to Microsoft/Apple dev environments in scope. 2012 AlexNet (Krizhevsky, Sutskever, Hinton) on CUDA GPUs wins ImageNet by a margin hosts compare to breaking the four-minute mile. Deep learning talent migrates to Google/Facebook; Nvidia becomes picks-and-shovels. Side paths: Tegra in Zune HD, Tesla Model S infotainment, Nintendo Switch; Icera acquisition → Graphcore founders as bear case (≈$700M VC raised). Analysis with Hamilton Helmer preview: Nvidia as platform with scale, switching, cornered resource. Lapsus$ hack demanded open-source drivers — evidence of lock-in value. Grading ties rich valuation to autonomous/physical AI optionality beyond digital ads/feeds ML.

---

## Key Facts

> **F1** CUDA development began 2006; hosts cite 6+ years before platform was broadly usable — ≈1,100 Nvidia employees with CUDA in title on LinkedIn at recording (Ben's search).

> **F2** Nvidia stock dropped ≈80% during financial crisis while Jensen continued CUDA investment; 2011 earnings miss caused another ≈50% drawdown — "is NVIDIA run over?" headlines.

> **F3** AlexNet (2012 ImageNet): ≈15% error rate vs prior leaders ≈25%+ — >10 percentage-point gap; implemented in CUDA on Nvidia GPUs — hosts call AI "big bang" moment.

> **F4** Nvidia has never charged for CUDA (through episode date) — proprietary, runs only on Nvidia hardware; OpenCL runs on Nvidia chips but not vice versa.

> **F5** CapEx comparison cited: Nvidia ≈$1B/year vs Apple ≈$10B, Microsoft/Google ≈$25B, TSMC ≈$30B; Nvidia ≈37% operating margins — above Apple, below Facebook/Google digital margins.


---

## Mental Model · *Free Software, Expensive Silicon*

> **Components**
>
> Jensen's CUDA bet mirrors Apple: give developers world-class platform free, monetize via high-margin hardware. "If you don't build it, they can't come" — market for general-purpose GPU compute (scientific/Cray replacement) looked tiny in 2006; scale required to amortize pyramid-scale engineering. AlexNet proved "embarrassingly parallel" workloads — independent computations suited to GPU architecture vs serial CPU. Mobile detours (Tegra, Icera → Graphcore) show diversification risk when core bet is unresolved. Crypto mining forced product segmentation (crippled consumer cards, dedicated miners) — Nvidia arbitraged others' arbitrage. Bear case: Google TPU, Cerebras (≈$2M chip vs ≈$20–30K Nvidia), Apple M-series GPUs, Tesla FSD silicon — but recreating 15 years CUDA + libraries is enormous bite. Omniverse = enterprise simulation metaverse (not consumer Metaverse).
>
> **Application**
>
> Platform hardware winners often subsidize software ecosystems until developer habit locks in — evaluate whether competitor can replicate stack, not just chip specs. For AI infra investors, separate gaming/crypto cyclicality from data-center CUDA habit. Enterprises without hyperscaler teams should buy integrated systems (DGX preview for Part III) vs piecemeal. Watch customer concentration and open-source/driver hack demands as stress tests of moat.

---

## What Makes It Work

> Post-2012 Nvidia stacks multiple Helmer powers on CUDA + gaming leadership. Scale economies: ≈1,100 CUDA staff amortized over millions of developers and data-center GPUs — competitors need equal R&D without equal breadth of customers. Switching costs: CUDA code does not run on AMD/TPU without rewrite — deeper than driver switching; ML frameworks and talent assume Nvidia first. Cornered resource: CUDA proprietary to Nvidia silicon — legal/technical barrier, not just TOS. Process power (legacy): six-month ship cycles from Part I eroded but fab flexibility remains (Samsung Ampere rumor, Intel fab talks). Branding: "serious ML runs on Nvidia" post-AlexNet; gaming RTX ray tracing keeps developer co-optimization pressure. Weaknesses: historical 80%+ drawdowns; Tegra/mobile failure; Android value chain profitless per hosts; hyperscaler custom ASICs (Google largest bear); Lapsus$ leak; rich public valuation requiring physical AI TAM (AV, Omniverse) to justify growth — digital ML alone may be insufficient for A+ stock outcome. Versus AMD: Radeon gaming-focused; took eye off CUDA opportunity. Graphcore/Icera founders exemplify failed insider competition.

---

## Key Insights

> **1.** CUDA was an iPhone-sized bet at billion-dollar scale.
>
> **Q** Why compare CUDA to Apple's platform shift?
>
> **A** At several-billion-dollar market cap, Jensen committed to a multi-year developer environment (drivers, APIs, libraries) larger than prior CG shaders — with no clear near-term revenue. Six-plus years to usefulness; ≈1,100 CUDA-titled staff today. Free software + proprietary hardware = Apple business model; Clay Christensen "open wins" skepticism was widespread until scale proved integrated stack.

> **2.** AlexNet did not validate Jensen's timing — it created the market.
>
> **Q** Did Jensen plan AlexNet?
>
> **A** Hosts and Ben Thompson interview agree: Jensen did not foresee AlexNet. Fei-Fei Li's ImageNet (2012 competition) and Toronto team's convolutional net won by >10 points error-rate gap running CUDA on GeForce cards. Scientific researchers previously shoehorned chemistry into graphics shaders — suboptimal until deep learning exploded parallel GPU demand.

> **3.** Mobile and Tegra were expensive distractions.
>
> **Q** What was Tegra's legacy?
>
> **A** Tegra shipped in Microsoft Zune HD (tell-all failure signal), Tesla Model S touchscreen, Nintendo Switch — repurposed silicon after smartphone SoC failure vs Qualcomm. Icera baseband buy (2011) shut down; founders created Graphcore (≈$700M VC) as Nvidia killer narrative. AMD spun mobile GPU to Qualcomm as Adreno (Radeon anagram).

> **4.** Nvidia extracts margin via segmentation and systems.
>
> **Q** How did crypto affect the business?
>
> **A** Miners arbitraged consumer GPUs — Nvidia crippled mining on gaming cards and sold dedicated miners; "your arbitrage is my opportunity." Terms-of-service and product segmentation improved predictability. Data-center terms similarly gate workload types — evil genius margin expansion while gamers get supply.

> **5.** Power is the CUDA platform stew.
>
> **Q** Which Helmer powers apply in 2022?
>
> **A** Scale economies on CUDA R&D, switching costs (boot CUDA = boot Nvidia), cornered resource (CUDA-hardware binding). Process power less than Part I. Hyperscaler ASICs (Google TPU, Cerebras at ≈$2M vs ≈$20–30K GPU) attack slice of stack but full recreation hard. A+ investment case needs physical-world AI (AV Hyperion, Omniverse) plus digital ML — not pandemic pull-forward alone.

---

## Investment Ideas

> **1. NVDA** · 🟡 WATCH · ●●○ Medium
>
> CUDA switching costs + ≈37% op margins on ≈$1B CapEx are exceptional — but valuation embeds physical AI (auto, Omniverse); monitor hyperscaler insourcing, crypto/gaming cycles, and Lapsus$-style IP pressure on proprietary stack.

> **2. GOOGL** · 🟡 WATCH · ●○○ Low
>
> Google cited as largest CUDA bear via TPU/custom training silicon — yet Google Cloud still Nvidia customer; TPU vertical scope limits external platform threat vs Nvidia horizontal CUDA habit.

---

## Golden Quotes

> ""If you don't build it, they can't come." — Jensen Huang on CUDA (paraphrased by hosts; distinct from "if you build it they will come")."

> ""CUDA is like one of the greatest business stories of the last 10 years, 20 years." — David Rosenthal; Ben calls it among boldest bets Acquired has covered."

> ""It is entirely free… But anyone can download it… You do any of this work, you cannot deploy it on anything but NVIDIA chips." — David on CUDA economics."

---

## Chronology

> *Nvidia (CUDA & ML era)*
>
> **2006** CUDA development begins — general-purpose GPU compute bet alongside gaming
>
> **2006** AMD acquires ATI — becomes primary GPU competitor
>
> **2008** Financial crisis — Nvidia stock ≈80% drawdown; Jensen continues CUDA spend
>
> **2009–12** Tegra in Zune HD, Tesla Model S screen, early automotive; mobile largely fails
>
> **2011** Nvidia buys Icera baseband; earnings miss → ≈50% stock drawdown
>
> **2011** Fei-Fei Li builds ImageNet; deep learning research accelerates
>
> **2012** AlexNet wins ImageNet by >10pt error gap on CUDA + Nvidia GPUs
>
> **2013** Bryan Catanzaro/Andrew Ng paper scales unsupervised learning on GPUs
>
> **2017+** RTX ray tracing; DLSS co-development with game studios
>
> **2011–22** Icera shutdown; Graphcore founded by Icera alumni (≈$700M VC raised)
>
> **2020s** Crypto mining drives segmentation — gaming cards limited, dedicated miners sold
>
> **2022** Omniverse simulation platform; automotive ≈$1B revenue cited; Jensen pitches $100T TAM × 1%
>
> **2022** Lapsus$ hack steals Nvidia source code — demands open drivers; Jensen acknowledges publicly
>

---

## Disclaimer

- **Independent notes.** This summary is not affiliated with, endorsed by, or produced by Acquired, Ben Gilbert & David Rosenthal, or Nvidia Part II: The Machine Learning Company (2006-2022). It reflects independent analyst notes for personal research and education only.
- **Original content.** All rights to the podcast audio, show materials, and guest remarks belong to the respective rights holders. Short attributed quotes are used for commentary; this is not a transcript or reproduction of the episode.
- **Not advice.** Nothing here is investment, legal, or professional advice. Listen to the original episode for full context and the guest's own words.
- **Corrections & takedown.** If you are a rights holder and believe this summary misuses your content, please request review or removal through the podcast-analyst project contact.
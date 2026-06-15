# EP.147 — Nvidia

## *Part I: The GPU Company (1993-2006) · Season 10 · Episode 5*

**★★★★☆** · 4/5

**Podcast** Acquired · **Date** Mar 27, 2022 · **Duration** 120 min · **Read** ≈6 min

**Host** Ben Gilbert & David Rosenthal



**Listen**  · [Acquired](https://www.acquired.fm/episodes/nvidia-the-gpu-company-1993-2006) · [Apple](https://podcasts.apple.com/podcast/acquired/id1050462261) · [Spotify](https://open.spotify.com/show/2HI3KdjtJnr3E8B4W8Y0Yx)

**Topics** GPU Computing · Semiconductor Strategy · Programmable Shaders
> ### Conclusion
>
> Nvidia Part I traces Jensen Huang from 1963 Taiwan through two near-death crises: 90 funded GPU clones in 1993, then Microsoft's Direct3D triangle standard vs Nvidia's quadrilateral bet that nearly bankrupted the company in 1997. The RIVA 128 escape — $1M emulator bet, tape-out without silicon prototypes, ≈100,000 units — and TSMC partnership (Jensen's letter to Morris Chang) established a six-month ship cadence Microsoft could not replicate. Programmable shaders (CG with Microsoft, GeForce 256, Xbox GPU) created developer-facing differentiation Intel integrated graphics could not absorb. By 2006 Nvidia had ≈83% standalone GPU share but little Hamilton Helmer "power" — commodity cycles, Xbox margin extraction, and AMD-ATI acquisition looming. Sequoia's $2M at $6M post in 1993 became among history's greatest venture outcomes via Jensen's reinvention discipline, not the original graphics-card thesis.

---

## Background

> Ben and David open Season 10 Episode 5 noting Nvidia as the eighth-largest company globally by market cap — impossible from a 1993 pitch to 90 competitors making PC gaming cards. Jensen Huang (born 1963, Taiwan) emigrated, skipped grades, studied electrical engineering at Oregon State and Stanford (eight-year master's), worked AMD then LSI Logic. Wilf Corrigan (Fairchild/LSI Logic CEO) referred Jensen to Don Valentine; Jensen botched the pitch but Sequoia and Sutter Hill invested $2M at $6M post anyway. Early wins (Sega deal, quadrilateral architecture) collided with Microsoft DirectX triangles and nine months of runway. Jensen bet on chip emulation at one frame per 30 seconds, skipped prototype silicon, and shipped the RIVA 128 — convincing developers to use eight of ≈24 Direct3D blend modes. TSMC became primary foundry after Jensen's cold letter to Morris Chang. IPO January 1999 at ≈$600M cap (100× seed). GeForce 256 marketed the invented term "GPU"; CG programmable shaders with Microsoft and Xbox partnership followed. Part II covers CUDA and machine learning; hosts tease Keyhole investment foreshadowing simulation/Omniverse.

---

## Key Facts

> **F1** Sequoia and Sutter Hill invested $2M total at ≈$6M post-money valuation in 1993; ≈89 competing GPU startups funded within months — Nvidia IPO'd January 1999 at ≈$600M market cap (≈100× seed valuation).

> **F2** 1997 crisis: ≈9 months runway; Nvidia spent ≈$1M on emulation hardware (~one-third of cash) to tape out RIVA 128 without prototype silicon — ordered ≈100,000 units from non-TSMC foundry.

> **F3** RIVA 128 supported roughly two-thirds of Direct3D blend modes (≈8 of ≈24–25); Nvidia campaigned developers to target those modes — 1997 shipment while competitors used two-year fab iteration cycles.

> **F4** TR-63 transistor radio sold 1.5M units at $25 (Sony episode cross-reference avoided) — here: fiscal 1999 revenue ≈$158M pre-IPO; Nvidia reached ≈$1B revenue by company year nine — fastest semiconductor to $1B cited, added to S&P 500.

> **F5** At episode close (2006): ≈83% standalone desktop/laptop GPU market share per hosts; AMD acquired ATI in 2006; Nvidia had product-market fit in gaming but hosts conclude minimal sustainable power vs Microsoft/Intel platform economics.


---

## Mental Model · *Reinvent Before Moore's Law Kills You*

> **Components**
>
> Jensen recognized graphics cards faced commodity cycles — parallel workloads off CPU, but no differentiation until programmable shaders and developer tools (CG, later CUDA). Two company-defining bets: (1) emulation-accelerated tape-out when bankrupt — speed as strategy; (2) vertical integration of drivers (Nvidia-written vs OEM-written) and developer SDKs — Apple-esque control. Microsoft profited from DirectX/Xbox without fab risk; Nvidia fought for survival twice (90 competitors, Intel integration threat). TSMC partnership converted foundry rejection into long-term scale — Jensen phone call from Morris Chang after physical letter. Simulation theme begins with 2006 Keyhole investment → Google Earth. Venture lesson: Sequoia was "wrong" on thesis, right on Jensen — proliferation then consolidation (Buffett 70 auto companies → three).
>
> **Application**
>
> In commoditizing hardware, ship cadence and developer lock-in matter more than first-mover funding headlines. Ask whether platform owners (Microsoft, Intel) capture value without entering the brutal cycle. When evaluating deep-tech founders, reference checks from portfolio CEOs (Wilf→Don) can outweigh pitch quality. Reinvention every 6–10 years is structural, not optional, in Moore's-law businesses.

---

## What Makes It Work

> Through 2006 Nvidia's advantage was execution speed and gamer brand, not durable Helmer power. Process power (temporary): six-month architecture cadence vs ~two-year industry norm — RIVA 128 emulation breakthrough. Collapsed as competitors learned and TSMC served all comers. Attempted switching costs: CG programmable shaders and NVIDIA-written drivers improved experience vs ATI — but Microsoft kept APIs cross-vendor; CUDA not yet deployed. Scale economies weak pre-CUDA — Xbox deal extracted margin (Microsoft "pound of flesh"); gaming TAM large (≈$100B cited today) but cyclical. Counter-positioning absent — Nvidia competed head-on in peripherals; Intel integrated graphics threatened low-end. Strengths vs 89 startups: Jensen survival will, TSMC access, developer evangelism (Crysis/Far Cry trope — games sell hardware). Xbox/Geforce era made GPU a standalone category Intel could not fully absorb. Weaknesses at 2006 cliff: revenue flattening post-Xbox; AMD+ATI; Intel Larrabee announced; no ML platform yet — hosts grade period A (created industry) not A+ (Microsoft captured platform economics without fab pain). Keyhole bet signals simulation ambition beyond games.

---

## Key Insights

> **1.** Don Valentine funded the founder, not the slide deck.
>
> **Q** How did Sequoia invest after Jensen's failed pitch?
>
> **A** Jensen partially wrote a business plan (three chapters of a how-to book), then "barfed" in the Sequoia meeting. Don stopped him leaving: Wilf Corrigan vouched — "if you lose my money, I'll kill you." $2M at $6M post with ≈89 clones following. Mark Stevens and Sequoia held personally for decades — among best venture returns ever despite wrong initial market thesis.

> **2.** Triangles beat quadrilaterals because standards beat first movers.
>
> **Q** Why did Microsoft's Direct3D nearly kill Nvidia?
>
> **A** Nvidia/Sega bet quadrilateral polygon primitives; DirectX used triangles (minimal 2D shape). Microsoft baked APIs into Windows — developers wanted Direct3D, not middleware from "no-name" vendors. Nvidia was first funded and first wrong on standard — competitors joined Microsoft ecosystem while Nvidia had ≈9 months cash.

> **3.** Emulation let Nvidia trade time for survival.
>
> **Q** What was insane about the RIVA 128 launch?
>
> **A** With ≈9 months runway, Nvidia spent ≈$1M (~one-third of cash) on chip emulation running ≈1 frame/30 seconds — debugged in software, taped out without prototype silicon, ordered ≈100,000 units. Only customer of startup emulator vendor (later failed). Supported ≈8/24–25 blend modes — salesforce asked developers to limit feature usage.

> **4.** Programmable shaders were the first real differentiation play.
>
> **Q** Why invent the term GPU?
>
> **A** GeForce 256 + CG (C extended for graphics) let developers program lighting/shaders on GPU — middle finger to Intel integrated graphics strategy. Required massive R&D while nearly broke again. Xbox partnership validated shaders but Microsoft extracted margins — strategic win, economic mixed bag.

> **5.** 2006 Nvidia had fit but not moat.
>
> **Q** What power did Nvidia have before CUDA?
>
> **A** Hosts conclude minimal sustainable power — attempted switching costs via CG not CUDA-level; process power eroding; Microsoft/Intel captured platform rents. Bull case from 2006: scientific computing and parallel workloads (spoiler: CUDA/AlexNet). Grade A for creating/shepherding GPU industry; not A+ because Microsoft benefited without Nvidia's existential fights.

---

## Investment Ideas

> **1. NVDA** · 🟡 WATCH · ●●○ Medium
>
> Part I frames origin of reinvention culture and TSMC dependency — modern NVDA power (CUDA, data center) begins Part II; historical lesson: hardware share without platform lock-in is cyclical until software moat arrives.

> **2. MSFT** · 🟡 WATCH · ●●○ Medium
>
> DirectX/Xbox let Microsoft harvest GPU industry innovation without fab or six-month ship cycles — platform owners often capture more rent than component winners in early standards wars.

---

## Golden Quotes

> "If you lose my money, I'll kill you. — Don Valentine to Jensen Huang after the botched Sequoia pitch, per Acquired."

> "When technology moves this fast, if you're not reinventing yourself, you're just slowly dying… at the rate of Moore's law. — Jensen Huang (Stanford lecture), cited on AMD pivot vs Nvidia."

> "My will to survive exceeds almost everybody else's will to kill me. — Jensen Huang, opening CliffsNotes of Part I."

---

## Chronology

> *Nvidia (GPU era)*
>
> **Feb 1963** Jen-Hsun (Jensen) Huang born in southern Taiwan
>
> **1993** Nvidia founded; $2M raised at $6M post from Sequoia/Sutter Hill; ≈89 GPU competitors funded
>
> **1993** Sega partnership for Saturn/Dreamcast path — quadrilateral architecture chosen
>
> **1995–96** Microsoft Direct3D/DirectX standardizes triangles — Nvidia strategic crisis
>
> **1997** RIVA 128 shipped via emulation tape-out — ≈100,000 units; ≈9 months runway at crisis peak
>
> **1997–98** Jensen's letter reaches Morris Chang; TSMC becomes primary Nvidia foundry
>
> **Jan 1999** Nvidia IPO ≈$600M market cap after RIVA 128 success
>
> **1999** GeForce 256 launched — "GPU" term marketed; fiscal revenue ≈$158M
>
> **1999–2001** CG programmable shaders developed with Microsoft; GeForce 3 PC version
>
> **2001–05** Xbox GPU deal — strategic validation, margin pressure from Microsoft
>
> **2006** AMD acquires ATI; Intel announces Larrabee GPU project; Nvidia invests in Keyhole (→ Google Earth)
>
> **2006** Hosts assess ≈83% standalone GPU share but weak Helmer power pre-CUDA
>

---

## Disclaimer

- **Independent notes.** This summary is not affiliated with, endorsed by, or produced by Acquired, Ben Gilbert & David Rosenthal, or Nvidia Part I: The GPU Company (1993-2006). It reflects independent analyst notes for personal research and education only.
- **Original content.** All rights to the podcast audio, show materials, and guest remarks belong to the respective rights holders. Short attributed quotes are used for commentary; this is not a transcript or reproduction of the episode.
- **Not advice.** Nothing here is investment, legal, or professional advice. Listen to the original episode for full context and the guest's own words.
- **Corrections & takedown.** If you are a rights holder and believe this summary misuses your content, please request review or removal through the podcast-analyst project contact.
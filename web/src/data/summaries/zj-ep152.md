# EP.152 — Sun Yutao (孙宇涛)

## *Reading the Kimi K3 Tech Report: Attention Aesthetics, Multi-Teacher Distill, Open MoE*

**★★★☆☆** · 3/5

**Podcast** Zhang Xiaojun Podcast · **Date** Aug 26, 2026 · **Duration** 124 min · **Read** ≈4 min

**Host** Zhang Xiaojun

**Guest** Sun Yutao (孙宇涛) · Tsinghua CS PhD candidate · incoming scholar, Shanghai Innovation Institute

**Listen** [YouTube](https://www.youtube.com/watch?v=axFwKz1X0is) · [Apple](https://podcasts.apple.com/cn/podcast/id1634356920)

**Topics** Moonshot · DeepSeek · NVDA
> ### Conclusion
>
> Zhang Xiaojun's paper-club tape: Tsinghua PhD Sun Yutao (architecture/pretrain since 2023) walks Kimi K3 after they waited for the right guest. K3 is an effectively scaled 2.8T fully open MoE — about 100B active, 1M context — larger than other Chinese open models at ship. Fake scale is standing up 2.8T and training 100B tokens. K2 reused a DeepSeek-V3-class stack; K3 is the architecture episode: hybrid attention, gated attention on MLA, latent MoE dispatch, on-policy distillation instead of merging RL rewards. His hot take: after Theseus-ship replacements, frontier models are refinements, not human-scale inventions.

---

## Background

> Learning episode, not a founder interview. Zhang delayed after the K3 drop to find someone whose PhD is architecture. Sun talks fast and chains ten-plus papers (YOCO, gated DeltaNet, DenseNet-era connections, Su Jianlin on optimizers). YouTube captions were off; this is a whisper-small transcript — names like Transformer/Theseus/DeepSeek are interpreted from ASR.

---

## Key Facts

> **F1** Scoreboard: Zhang's cold open — K3 is an effectively scaled 2.8T total-parameter, fully open MoE. Sun's three claimed scalings: size first (2.8T is only real if trained for real; a 2.8T unit run on 100B tokens is fake scale), activation around 100B (bigger than other domestic open models at the K3 date), and context to about 1M tokens. First-principles line on the tape: bigger models set a higher intelligence ceiling if you do not botch the rest; benchmarks can be gamed, parameter count is still the honest lever. Kimi reached that scale early.

> **F2** Architecture vs K2: K2's push was scaling and non-architecture work, so it kept a DeepSeek-V3-class (whisper: Deep Sake Waysray) skeleton. K3 is different — hybrid attention (Sun's YOCO-class story: linear attention up front, full attention later, skip full attention in prefill, keep one KV cache), gated attention folded into MLA (K2 already used MLA; DeepSeek V4 dropped it because they had something else). Sun: MLA is an MQA equivalent, a better implementation, not a new primitive — matching quality costs extra compute, and a better GQA can eat the gain. Latent MoE shrinks the dispatched hidden state 2–4x to cut all-to-all. Dropless expert pick unbalances GPUs; a 128-expert / EP8 static map is 16 experts per card; redundant experts can prove a small extra pool balances token counts.

> **F3** Train stack and philosophy: Muon/MIL vs architecture — Su Jianlin's line (whisper: 苏建磊) is that any optimizer will blow up; if you want control, change the architecture (QK logits, bounds), do not clip forever. Theseus's ship: 2017 Transformer was attention plus residual; by 2026 so many planks are swapped you can ask if it is still a Transformer. Sun's hot take: no more human-scale inventions, only refinements. Post-train: on-policy distillation turns specialist RL / reward models into teacher models and distills — easier than merging unique rewards (math, preference, extra skills) into one RL pot. Zhang also flags DenseNet / hyperconnection-era residual plumbing as the unglamorous fourth knob after attention, MoE, and the optimizer.


---

## Mental Model · *Effective 2.8T × Architecture Episode × Distill the Teachers*

> **Components**
>
> Scale is real only if tokens and activation match the parameter sticker. K3's sticker is 2.8T / ≈100B active / 1M context and fully open. K2 was a DeepSeek-shaped scaler; K3 is where Moonshot spends architecture: hybrid attention, gated MLA, latent dispatch, redundant-expert load balance. MLA is a better MQA, not a forever primitive — V4 already left. OPD is the multi-teacher move: do not merge rewards, distill specialists. Theseus: keep swapping planks and call it incremental. Fix instability in the architecture, not only in Muon clips.
>
> **Application**
>
> Private:Moonshot is the named 2.8T open MoE and the K2-to-K3 architecture turn. Private:DeepSeek is the V3 skeleton K2 copied and the V4 lab that dropped MLA. NVDA is the GPU that waits when expert load is uneven — infra, not a new chip thesis. Do not underwrite a 2.8T press release trained on 100B tokens. Fade 'MLA is the consensus forever.' Treat OPD as the post-train org chart, not a magic loss.

---


## Key Insights

> **1.** 2.8T is a claim about training, not a file size.
>
> **Q** What is fake scale?
>
> **A** Stand up 2.8T, run 100B tokens, ship. K3's tape is effective scale plus ≈100B active and 1M context, open.

> **2.** K3 is the architecture episode.
>
> **Q** What changed after K2?
>
> **A** K2 reused a DeepSeek-V3 stack. K3 adds hybrid attention, gated MLA, latent MoE. MLA is better MQA; V4 already left.

> **3.** Distill teachers, do not merge rewards.
>
> **Q** Why on-policy distillation?
>
> **A** Each RL skill has its own reward. OPD turns specialists into teachers. Easier than one pot of math plus preference plus extras.

---

## Investment Ideas

> **1. Moonshot** · 🟢 LONG · ●●○ Medium
>
> Named 2.8T / ≈100B-active open MoE with a real architecture delta vs K2; scale is only as good as the tokens — medium

> **2. DeepSeek** · 🟢 LONG · ●○○ Low
>
> The V3-class stack K2 copied, and the V4 lab that already walked off MLA — low

---

## Golden Quotes

> "K3是有效扩展到2.8T总参数并全量开源的MOE模型"

> "我的暴论就是大模型"

> "on-policy distillation"

---

## Chronology

> *Kimi K3 · open MoE · architecture*
>
> **2017** Transformer as attention + residual — Theseus ship launches
>
> **2023** Sun starts architecture PhD (pre/around ChatGPT)
>
> **K2** Moonshot scales on a DeepSeek-V3-class skeleton
>
> **K3 drop** 2.8T open MoE; Zhang starts hunting a reader
>
> **V4** DeepSeek leaves MLA for something else
>
> **2026-08-26** ZJ 152 with Sun Yutao
>

---

## Disclaimer

- **Independent notes.** This summary is not affiliated with, endorsed by, or produced by Zhang Xiaojun Podcast, Zhang Xiaojun, or Sun Yutao (孙宇涛). It reflects independent analyst notes for personal research and education only.
- **Original content.** All rights to the podcast audio, show materials, and guest remarks belong to the respective rights holders. Short attributed quotes are used for commentary; this is not a transcript or reproduction of the episode.
- **Not advice.** Nothing here is investment, legal, or professional advice. Listen to the [original episode](https://www.youtube.com/watch?v=axFwKz1X0is) for full context and the guest's own words.
- **Corrections & takedown.** If you are a rights holder and believe this summary misuses your content, please request review or removal through the podcast-analyst project contact.
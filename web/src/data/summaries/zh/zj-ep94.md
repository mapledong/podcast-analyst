# EP.94 — 广密

## *逐篇讲解DeepSeek、Kimi、MiniMax注意力机制新论文——“硬件上的暴力美学”*

**★★★☆☆** · 3/5

**Podcast** 张小珺商业访谈录 · **Date** Mar 2, 2025 · **Duration** 90 min · **Read** ≈1 min

**Host** 张小珺

**Guest** 广密 · AI研究员、全球大模型季报主播

**Listen** [YouTube](https://www.youtube.com/watch?v=42CveqxzU5M) · [Apple](https://podcasts.apple.com/cn/podcast/id1634356920)

**Topics** NVDA · DEEPSEEK · KIMI · MINIMAX
> ### Conclusion
>
> 广密逐篇讲解 DeepSeek、Kimi、MiniMax 注意力创新，将中国实验室框为硬件上的暴力美学——MLA、稀疏注意力与 MoE 路由在英伟达（NVDA）集群上榨更多 token/瓦。效率增益压缩推理成本曲线但抬高训练规模 GPU 需求。投资者应观望 NVDA 的中国集群建设与实验室效率赛，开源模型压 hyperscaler 毛利。

---

## Background

> 张小珺 2025 年 3 月 2 日与广密（AI 研究员、大模型季报主播）逐句精读 DeepSeek、月之暗面 Kimi、MiniMax 新注意力论文。主题「硬件上的暴力美学」——算法与 H100/H800 内存带宽及 MFU 协同设计。广密解释多头潜注意力、闪电注意力变体及中国实验室为何发表西方藏在 infra 里的工程突破。

---

## Key Facts

> **F1** 注意力工程浪潮：DeepSeek V3/R1 MLA 降 KV cache 内存——每 GPU 更多上下文；Kimi 与 MiniMax 推稀疏与线性注意力混合。即使每 token 推理降，训练规模仍利 NVDA——算力杰文斯悖论。

> **F2** 开源权重压力：中国实验室发论文与权重——商品化 GOOGL/META 基础模型租金同时刺激硬件需求。广密称最美算法最干净——投资者跟 MFU 与 $/token 非参数量吹嘘。

> **F3** 可投资 NVDA：中国实验室 capex 周期绑注意力突破——新架构交付则集群升级。观望 NVDA 数据中心收入来自中国 hyperscaler 与创业训练；风险是出口管制 cap H800 供给。


---

## Mental Model · *注意力 MFU × 开源商品化 × 杰文斯算力*

> **Components**
>
> 效率降 $/token 但抬总服务 token。中国实验室为英伟达内存拓扑协同设计。开源权重压缩模型租金、扩大硬件盛宴。
>
> **Application**
>
> 英伟达（NVDA）：观望 DeepSeek/Kimi 论文后中国训练集群需求——效率增益增 aggregate compute。若出口政策永久 cap 中国 MFU 增长则低配。

---


## Key Insights

> **1.** 暴力美学即硬件协同设计。
>
> **Q** 广密对中国论文论点是什么？
>
> **A** DeepSeek MLA 等优化真实集群拓扑——内存带宽与 MFU 非仅学术新奇。投资者应将论文读作 GPU 代际 capex 信号。

> **2.** 干净算法在经济上胜。
>
> **Q** 为何赞「最优美最干净」？
>
> **A** 更简单注意力变体部署快、易 debug——每 flop 工程阻力低。发干净架构加开源的实验室迫西方 incumbent 匹配效率或烧毛利。

> **3.** 效率可增 GPU 需求。
>
> **Q** MLA 是否伤 NVDA？
>
> **A** 广密暗示杰文斯效应——更廉推理催生更多 Agent 与更长上下文，训练赛继续。NVDA 赢在 aggregate token 乘训练前沿，非仅每 token 租金。

---

## Investment Ideas

> **1. NVDA** · 🟡 WATCH · ●●○ Medium
>
> 英伟达（NVDA）：广密 DeepSeek/Kimi/MiniMax 注意力论文——观望中国集群需求随效率赛扩大总算力

---

## Golden Quotes

> "应该都是有的他们的主要贡献应该是更多的集中在这种如何让它变得更高效的上面"

> "对因为这个东西我因为我比较我我主要就是在做一些线性注意力的一个东西"

> "所以我们要保证就是我们这些有一些很多这种运算能够写成矩阵成法"

---

## Chronology

> *广密 · 注意力论文*
>
> **2024** DeepSeek V2/V3 MLA 注意力突破
>
> **2025-01** Kimi K1.5 与推理模型注意力变体
>
> **2025-02** MiniMax 等稀疏注意力论文
>
> **2025-03-02** 广密论文讲解录制
>
> **2025** 中国实验室新架构驱动集群升级
>
> **2026+** 推理成本曲线与 Agent token 需求
>

---

## Disclaimer

- **Independent notes.** This summary is not affiliated with, endorsed by, or produced by 张小珺商业访谈录, 张小珺, or 广密. It reflects independent analyst notes for personal research and education only.
- **Original content.** All rights to the podcast audio, show materials, and guest remarks belong to the respective rights holders. Short attributed quotes are used for commentary; this is not a transcript or reproduction of the episode.
- **Not advice.** Nothing here is investment, legal, or professional advice. Listen to the [original episode](https://www.youtube.com/watch?v=42CveqxzU5M) for full context and the guest's own words.
- **Corrections & takedown.** If you are a rights holder and believe this summary misuses your content, please request review or removal through the podcast-analyst project contact.

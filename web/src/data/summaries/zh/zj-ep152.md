# EP.152 — 孙宇涛

## *152. 领读Kimi K3技术报告：注意力美学、多教师蒸馏、开源MoE*

**★★★☆☆** · 3/5

**播客** 张小珺商业访谈录 · **日期** 2026年8月26日 · **时长** 124 分钟 · **阅读** ≈4 分钟

**主持人** 张小珺

**嘉宾** 孙宇涛 · 清华大学计算机系博士候选人 · 上海创智学院预聘学者

**收听** [YouTube](https://www.youtube.com/watch?v=axFwKz1X0is) · [小宇宙](https://www.xiaoyuzhoufm.com/episode/6a8eadd61352af56ff3c6017) · [Apple 播客](https://podcasts.apple.com/cn/podcast/id1634356920)

**主题** Moonshot · DeepSeek · NVDA
> ### 结论
>
> 张小珺这期是论文课：清华博士孙宇涛（2023年起做架构/预训练）在他们等对嘉宾之后领读Kimi K3。K3是有效扩展到2.8T、全量开源的MoE——激活约100B，上下文约1M——发布时比国内其他开源更大。假扩展是立起2.8T只跑100B token。K2沿用DeepSeek V3一类骨架；K3才是架构集：混合注意力、MLA上加gated、latent MoE通信、用on-policy distillation而不是把RL奖励糊在一锅。他的暴论：忒修斯之船换完板，前沿只剩改良，没有太人本的创新。

---

## 背景

> 学习播客，不是创始人访谈。K3发布后张小珺等适合讲架构的人。孙宇涛语速快，串联十多篇（YOCO、gated DeltaNet、DenseNet时代的连接、苏剑林谈优化器）。YouTube字幕关了，这是whisper-small；Transformer/忒修斯/DeepSeek等是按转写校正的。

---

## 关键事实

> **F1** 记分牌：开场——K3是有效扩展到2.8T总参数并全量开源的MoE。孙宇涛说的三个scaling：先讲尺寸（2.8T只有真训练才算；立起2.8T跑100B token是假扩展），激活大约100B（K3发布时比国内其他开源大一截），上下文做到约1M token。带子上的第一性：模型更大才有更高智能上限，别的别搞砸；benchmark可以刷，参数量仍是老实杠杆。Kimi相当早地摸到这个量级。

> **F2** 架构对K2：K2发力在scaling和非架构，所以沿用DeepSeek V3一类（转写Deep Sake Waysray）骨架。K3不一样——混合注意力（孙的YOCO故事：前期线性注意力、后期全注意力，prefill跳过全注意力、只留一份KV），gated注意力折进MLA（K2已用MLA；DeepSeek V4不用了，因为有别的）。孙：MLA是MQA的等价形式，更好的实现，不是新原语——要对齐效果会加计算，更好的GQA能吃掉这块收益。Latent MoE把dispatch的隐状态缩小2–4倍，砍all-to-all。Dropless选专家会让GPU负载不齐；128专家/EP8静态是每卡16个；冗余专家可以从数学上用一小撮额外专家把token数对齐。

> **F3** 训练栈和哲学：Muon/MIL对架构——苏剑林（转写苏建磊）的意思是任何优化器都会炸；要管得住就改架构（QK logits、上界），不要永远clip。忒修斯之船：2017年Transformer是attention加残差；到2026年换了那么多板，还能不能叫Transformer。孙的暴论：没有太人本的创新，后面都是改良。后训练：on-policy distillation把专项RL/奖励模型变成教师再蒸馏——比把数学、preference、额外技能的独特奖励糊进一锅RL容易。张小珺还把DenseNet/hyperconnection这类残差管道当成注意力、MoE、优化器之后不风光的第四个旋钮。


---

## 思维模型 · *有效的2.8T × 架构集 × 蒸馏教师*

> **构成**
>
> 扩展只有token和激活对得上参数贴纸才算。K3的贴纸是2.8T / 约100B激活 / 1M上下文，并且全开源。K2是DeepSeek形的scaler；K3是月之暗面花在架构上的那一集：混合注意力、gated MLA、latent通信、冗余专家均衡。MLA是更好的MQA，不是永远共识——V4已经走了。OPD是多教师：别合并奖励，蒸馏专项。忒修斯：继续换板，叫它增量。不稳先改架构，不只clip Muon。
>
> **应用**
>
> Private:Moonshot是点名的2.8T开源MoE，也是K2到K3的架构转弯。Private:DeepSeek是K2抄的V3骨架，也是已经离开MLA的V4实验室。NVDA是专家负载不齐时在等的那张GPU——基建，不是新芯片论点。不要给只跑了100B token的2.8T通稿估值。淡「MLA永远是共识」。把OPD当后训练编制，不当神奇loss。

---


## 核心洞察

> **1.** 2.8T是训练主张，不是文件大小。
>
> **问** 什么是假扩展？
>
> **答** 立起2.8T，跑100B token，发出来。K3这期是有效扩展，加上约100B激活和1M上下文，开源。

> **2.** K3才是架构集。
>
> **问** K2之后变了什么？
>
> **答** K2沿用DeepSeek V3骨架。K3加混合注意力、gated MLA、latent MoE。MLA是更好的MQA；V4已经离开。

> **3.** 蒸馏教师，别合并奖励。
>
> **问** 为什么是on-policy distillation？
>
> **答** 每个RL技能有自己的奖励。OPD把专项变成教师。比数学+preference+额外技能一锅炖容易。

---

## 投资启示

> **1. Moonshot** · 🟢 LONG · ●●○ Medium
>
> 点名的2.8T/约100B激活开源MoE，相对K2有真架构差；扩展只取决于token — medium

> **2. DeepSeek** · 🟢 LONG · ●○○ Low
>
> K2沿用的V3一类骨架，以及已经离开MLA的V4实验室 — low

---

## 金句

> 「K3是有效扩展到2.8T总参数并全量开源的MOE模型」

> 「我的暴论就是大模型」

> 「on-policy distillation」

---

## 时间线

> *Kimi K3 · 开源MoE · 架构*
>
> **2017** Transformer＝attention+残差——忒修斯之船上水
>
> **2023** 孙宇涛开始架构博士（ChatGPT前后）
>
> **K2** 月之暗面在DeepSeek V3一类骨架上做scaling
>
> **K3发布** 2.8T开源MoE；张小珺开始找领读者
>
> **V4** DeepSeek不用MLA，换了别的
>
> **2026-08-26** 张小珺152 孙宇涛
>

---

## 免责声明

- **独立笔记。** 本摘要与 张小珺商业访谈录、张小珺 或 孙宇涛 无隶属或合作关系，仅供个人研究与学习。
- **原创内容。** 播客音频及嘉宾言论版权归原权利人所有；此处引用短句仅为评论目的，并非逐字稿。
- **非投资建议。** 本文不构成任何投资、法律或专业建议。 请收听[原节目](https://www.youtube.com/watch?v=axFwKz1X0is)获取完整语境。
- **纠错与下架。** 若您是权利人并认为本摘要不当使用您的内容，请通过 podcast-analyst 项目联系申请复核或下架。
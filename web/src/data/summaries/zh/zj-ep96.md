# EP.96 — 郎咸朋

## *和郎咸朋聊，自动驾驶10年演进史、关键技术细节和特斯拉*

**★★★☆☆** · 3/5

**Podcast** 张小珺商业访谈录 · **Date** Mar 16, 2025 · **Duration** 120 min · **Read** ≈1 min

**Host** 张小珺

**Guest** 郎咸朋 · 理想汽车智能驾驶负责人

**Listen** [YouTube](https://www.youtube.com/watch?v=qtugoE1xQZk) · [Apple](https://podcasts.apple.com/cn/podcast/id1634356920)

**Topics** TSLA · 自动驾驶 · 端到端 · 纯视觉
> ### Conclusion
>
> 郎咸朋十年回顾称特斯拉最早最准喊出纯视觉、弃高精地图——行业在激光雷达加轨道隐喻上浪费数年。端到端与生成式融合取代后处理拼接；算力不足时特斯拉自研芯片。投资者应观望特斯拉（TSLA）FSD 里程与芯片节奏作为中国团队追赶的基准，非 legacy 激光雷达地图栈。

---

## Background

> 理想汽车副总裁郎咸朋（2024 年 12 月录制）梳理中国自动驾驶从 2014–15 年百度激光雷达加高精地图「虚拟轨道」经 BEV（2018）至今日端到端浪潮。高精地图在日均变动的 970 万公里普通道路上无法扩展；特斯拉纯视觉立场曾遭嘲笑现被验证。郎咸朋引特斯拉端到端哲学——在统一画布融合相机特征再反投物体保一致性，对比逐相机检测拼接。30 TOPS 英伟达芯片跑不动视频网络后自研 FSD 芯片，现数百 TOPS。谈话是技术科普：规则→感知栈→BEV→端到端→世界模型。

---

## Key Facts

> **F1** 2014 轨道隐喻已死：早期 AV 想象虚拟轨道加 360° 激光雷达如地铁——仅高速公路 30 万公里可行，非中国 970 万公里普通道路与日更施工。高精地图刷新经济学扼杀该路径；特斯拉 2018 纯视觉宣言正确且超前，多数 incumbent 无法 pivot 沉没激光雷达投入。

> **F2** 特斯拉端到端教训：后融合拼接幻觉时改生成式——在拼接鸟瞰画布提取再反投一致物体到各相机。郎咸朋赞特斯拉以端到端方法解决，非像今日 LLM 幻觉打地鼠式修补。算法加自研硅协同：英伟达代际不足跑视频网时 2016 年启动芯片项目。

> **F3** 基准框架：特斯拉（TSLA）观望——FSD 里程、Dojo/世界模型迭代与 TOPS 路线图定中国团队对标节奏。理想端端透明（attention 与轨迹 UI）竞争可解释性；胜利模式是特斯拉规模车队数据加本土合规。


---

## Mental Model · *纯视觉 × 端到端融合 × 硅协同*

> **Components**
>
> 高精地图无法扩展至动态路网。统一 BEV 融合胜逐相机拼接——对象是 consistency 非补丁。GPU 不够则垂直整合硅——自动驾驶算力绑定。
>
> **Application**
>
> 特斯拉（TSLA）：观望 FSD 收入确认与每干预里程趋势——设定全球 AD 期权估值天花板。中国 OEM AD 赌注为衍生；仍卖激光雷达地图拐杖作主栈的供应商低配。

---


## Key Insights

> **1.** 特斯拉最先看见纯视觉。
>
> **Q** 郎咸朋为何抬高特斯拉 2018 判断？
>
> **A** 行业大脑 wired 于激光雷达轨道——特斯拉在看似荒谬时喊不要高精地图、不要激光雷达、纯视觉。郎咸朋将同行分为不信者、信但转不了身者、故意者。最先正确且超前胜在死架构上 incremental 修补。

> **2.** 端到端胜后融合补丁。
>
> **Q** 特斯拉 BEV 洞察是什么？
>
> **A** 在一张画布拼接相机特征、整体检测、反投——物体保持一致，对比合并逐相机局部框。郎咸朋类比偏好生成式修复胜 LLM 幻觉打地鼠。架构选择重于 transformer 细节。

> **3.** 硅跟随算法饥渴。
>
> **Q** 特斯拉为何造 FSD 芯片？
>
> **A** 视频网络超 30 TOPS 英伟达部件——特斯拉垂直整合至 72+ TOPS 代际。郎咸朋十年叙事将算力波（2013 DL 复兴）与传感器定律绑：相机与算法进步时激光雷达拐杖 ROI 失守。

---

## Investment Ideas

> **1. TSLA** · 🟡 WATCH · ●●○ Medium
>
> 特斯拉（TSLA）：郎咸朋十年自动驾驶史——纯视觉与端到端融合基准；观望 FSD 里程与自研硅节奏

---

## Golden Quotes

> "而不是说我来我来去用一些地位的层次来安抚你什么的"

> "就是你导航是我们开车一个非常重要的这样一个方式"

> "我们也不是说把所有的客户题到最后让你全背一遍"

---

## Chronology

> *郎咸朋 · 自动驾驶十年*
>
> **2014–2015** 百度自动驾驶团队；激光雷达+高精地图轨道范式
>
> **2018** BEV 时代；特斯拉宣布纯视觉
>
> **2016–2019** 特斯拉 FSD 芯片项目；72 TOPS 代际
>
> **2023–2024** 中国端到端采纳浪潮
>
> **2024-12** 郎咸朋录制张小珺自动驾驶史节目
>

---

## Disclaimer

- **Independent notes.** This summary is not affiliated with, endorsed by, or produced by 张小珺商业访谈录, 张小珺, or 郎咸朋. It reflects independent analyst notes for personal research and education only.
- **Original content.** All rights to the podcast audio, show materials, and guest remarks belong to the respective rights holders. Short attributed quotes are used for commentary; this is not a transcript or reproduction of the episode.
- **Not advice.** Nothing here is investment, legal, or professional advice. Listen to the [original episode](https://www.youtube.com/watch?v=qtugoE1xQZk) for full context and the guest's own words.
- **Corrections & takedown.** If you are a rights holder and believe this summary misuses your content, please request review or removal through the podcast-analyst project contact.

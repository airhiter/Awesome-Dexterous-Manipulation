<div align="center">

# Awesome Dexterous Manipulation Papers

**灵巧手操作 · 前沿论文 · 科研阅读指南**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/Papers-49-2867B2?style=flat-square)
![Core Reading](https://img.shields.io/badge/Core%20Reading-20-7C3AED?style=flat-square)
![Updated](https://img.shields.io/badge/Updated-2026--11--26-16805D?style=flat-square)
[![GitHub Stars](https://img.shields.io/github/stars/airhiter/Awesome-Dexterous-Manipulation?style=flat-square)](https://github.com/airhiter/Awesome-Dexterous-Manipulation/stargazers)

[English](README.md) | [简体中文](README.zh-CN.md)

[领域综述](#category-7) · [核心精读](#core-reading) · [相关资源](#resources) · [贡献指南](#contributing)

</div>

## 关于本项目

**Awesome Dexterous Manipulation Papers** 聚焦灵巧手操作的前沿算法研究，汇集 CoRL、RSS、ICRA、IROS 等会议论文及产业界技术报告，涵盖数据采集、触觉感知、强化学习、VLA、世界模型与灵巧抓取。

<p align="center">
  <a href="https://arxiv.org/abs/2504.03515"><img src="https://raw.githubusercontent.com/chang-xinhai/Awesome-Dexterous-Manipulation/main/assets/dexterous-manipulation-examples.png" alt="Real-world dexterous robotic manipulation examples" width="900"></a>
  <br>
  <sub>真实世界中的灵巧操作示例。来源：Fig. 1, <a href="https://arxiv.org/abs/2504.03515">Dexterous Manipulation through Imitation Learning: A Survey</a> (An et al., 2025). 图像链接来自 <a href="https://github.com/chang-xinhai/Awesome-Dexterous-Manipulation">chang-xinhai/Awesome-Dexterous-Manipulation</a>.</sub>
</p>

**检索截止:** 2026-11-26 · **49 篇文献 · 7 个方向 · 20 篇核心精读**

## 目录

- [领域综述 (5)](#category-7)
- [数据采集、模仿学习与跨本体迁移 (13)](#category-1)
- [触觉感知、触觉基础模型与多模态融合 (10)](#category-2)
- [强化学习、Sim-to-Real 与策略后训练 (7)](#category-3)
- [VLA 与通用灵巧操作基础模型 (5)](#category-4)
- [世界模型、动力学建模与接触控制 (8)](#category-5)
- [灵巧抓取与基础数据集 (1)](#category-6)
- [核心精读清单（20篇）](#core-reading)
- [相关资源](#resources)
- [贡献指南](#contributing)

**阅读优先级:** S＝重点精读；A＝完整通读；B＝补充阅读。

<a id="category-7"></a>

## 01. 领域综述 (5)

如何快速建立领域知识体系？

| 编号 | 论文 | 发表情况 | 核心内容 | 原文 | 优先级 |
| --- | --- | --- | --- | --- | --- |
| 46 | The Developments and Challenges Toward Dexterous and Embodied Robotic Manipulation: A Survey | IEEE RAM 2026 | 具身灵巧操作、数据采集、学习框架与关键挑战 | [原文入口](https://doi.org/10.1109/MRA.2025.3642671) | **S** |
| 47 | Dexterous Manipulation Through Imitation Learning: A Survey | IEEE T-ASE 2026 | 模仿学习、示范数据、遥操作与灵巧操作 | [原文入口](https://doi.org/10.1109/TASE.2025.3646183) | **S** |
| 45 | Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey of Hardware, Data, Cross-Embodiment Transfer, Learning, and Evaluation | arXiv 2026.11 | 基础模型时代灵巧机械手的全栈综述 | [原文入口](https://arxiv.org/abs/2611.06724) | **S** |
| 48 | Towards Robotic Dexterous Hand Intelligence: A Survey | arXiv 2026.05 | 硬件、控制、学习方法、数据集与评估 | [原文入口](https://arxiv.org/abs/2605.13925) | **A** |
| 49 | Survey of Learning-Based Approaches for Robotic In-Hand Manipulation | Frontiers in Robotics and AI 2024 | 手内操作的模型学习、强化学习与模仿学习 | [原文入口](https://doi.org/10.3389/frobt.2024.1455431) | **A** |

**推荐阅读顺序：** 先阅读 IEEE RAM 和 IEEE T-ASE 两篇正式发表的综述，建立整体技术框架；再阅读 2026 年全栈综述，补充最新进展。

<a id="category-1"></a>

## 02. 数据采集、模仿学习与跨本体迁移 (13)

如何获得大规模、高质量的操作数据并实现人机迁移？

| 编号 | 论文 | 发表情况 | 核心内容 | 原文 | 优先级 |
| --- | --- | --- | --- | --- | --- |
| 01 | AnyTeleop | RSS 2023 | 通用视觉遥操作与动作重定向 | [原文入口](https://roboticsproceedings.org/rss19/p015.html) | **A** |
| 02 | DexCap | RSS 2024 | 便携式动作捕捉与模仿学习 | [原文入口](https://dex-cap.github.io/) | **S** |
| 03 | Tilde | RSS 2024 | 低成本灵巧手遥操作 | [原文入口](https://roboticsproceedings.org/rss20/p128.html) | **B** |
| 04 | DexWild | RSS 2025 | 自然场景中的人类操作数据采集 | [原文入口](https://roboticsproceedings.org/rss21/p075.html) | **A** |
| 05 | Dex1B | RSS 2025 | 十亿级仿真示范数据与策略学习 | [原文入口](https://roboticsproceedings.org/rss21/p106.html) | **S** |
| 06 | DexUMI | CoRL 2025 | 使用人手作为通用数据采集接口 | [原文入口](https://proceedings.mlr.press/v305/xu25b.html) | **S** |
| 07 | DEXOP | arXiv 2025 | 外骨骼与多模态示范数据采集 | [原文入口](https://arxiv.org/abs/2509.04441) | **A** |
| 08 | EgoDex | ICLR 2026 | Apple 第一视角人类灵巧操作数据集 | [原文入口](https://machinelearning.apple.com/research/egodex-learning-dexterous-manipulation) | **A** |
| 09 | Dexterity from Smart Lenses | ICRA 2026 | 智能眼镜采集人类操作示范 | [原文入口](https://ieeexplore.ieee.org/abstract/document/11697220) | **A** |
| 10 | UniDex | CVPR 2026 | 人类视频与通用灵巧操作策略 | [原文入口](https://unidex-ai.github.io/) | **S** |
| 11 | DexImit | RSS 2026 | 从单目人类视频学习双手操作 | [原文入口](https://roboticsproceedings.org/rss22/p003.html) | **S** |
| 12 | ReDex | IROS 2026 | 基于手物关系几何先验的跨本体迁移 | [原文入口](https://psycho811.github.io/ReDex/) | **S** |
| 13 | RealDexUMI | arXiv 2026 | 可穿戴灵巧手数据采集系统 | [原文入口](https://research.beingbeyond.com/realdexumi) | **A** |

<a id="category-2"></a>

## 03. 触觉感知、触觉基础模型与多模态融合 (10)

如何感知接触、摩擦、滑移和作用力？

| 编号 | 论文 | 发表情况 | 核心内容 | 原文 | 优先级 |
| --- | --- | --- | --- | --- | --- |
| 14 | Rotating without Seeing | RSS 2023 | 无视觉条件下的触觉手内旋转 | [原文入口](https://roboticsproceedings.org/rss19/p036.html) | **S** |
| 15 | KineDex | CoRL 2025 | 动觉示教与触觉力控策略 | [原文入口](https://proceedings.mlr.press/v305/zhang25l.html) | **A** |
| 16 | Text2Touch | CoRL 2025 | 利用 LLM 构建触觉 RL 奖励 | [原文入口](https://proceedings.mlr.press/v305/field25a.html) | **B** |
| 17 | ViTacFormer | RSS 2026 | 视觉与触觉跨模态表征学习 | [原文入口](https://roboticsproceedings.org/rss22/p129.html) | **S** |
| 18 | T-Rex | CoRL 2026 | 高频触觉反馈与变频率 MoT 架构 | [原文入口](https://arxiv.org/abs/2606.17055) | **S** |
| 19 | TTP | arXiv 2026.07 | 人类触觉数据预训练与迁移 | [原文入口](https://arxiv.org/abs/2607.01067) | **S** |
| 20 | TouchWorld | arXiv 2026.07 | 预测式与反应式触觉基础模型 | [原文入口](https://arxiv.org/abs/2607.07287) | **S** |
| 21 | Dex-X | arXiv 2026.09 | 人类视频与仿真交互相结合的视触觉学习 | [原文入口](https://arxiv.org/abs/2609.07747) | **A** |
| 22 | Spark-0 | arXiv 2026.10 | 大规模空间对齐触觉预训练 | [原文入口](https://arxiv.org/abs/2610.22342) | **S** |
| 23 | LingBot-Touch | arXiv 2026.11 | 异构触觉传感器统一表征 | [原文入口](https://arxiv.org/abs/2611.12806) | **S** |

<a id="category-3"></a>

## 04. 强化学习、Sim-to-Real 与策略后训练 (7)

如何通过交互和策略迭代提升灵巧操作能力？

| 编号 | 论文 | 发表情况 | 核心内容 | 原文 | 优先级 |
| --- | --- | --- | --- | --- | --- |
| 24 | In-Hand Object Rotation via Rapid Motor Adaptation | CoRL 2022 | 隐式物理参数估计与快速在线适应 | [原文入口](https://proceedings.mlr.press/v205/qi23a.html) | **S** |
| 25 | DexPoint | CoRL 2022 | 点云表征、接触奖励与 Sim-to-Real | [原文入口](https://proceedings.mlr.press/v205/qin23a.html) | **A** |
| 26 | Dexplore | CoRL 2025 | 基于人类动作先验的策略探索 | [原文入口](https://proceedings.mlr.press/v305/xu25d.html) | **A** |
| 27 | DexCtrl | ICRA 2026 | 自适应控制器与仿真到真机迁移 | [原文入口](https://arxiv.org/abs/2505.00991) | **A** |
| 28 | SimToolReal | RSS 2026 | 物体中心表征与零样本灵巧工具操作 | [原文入口](https://roboticsproceedings.org/rss22/p151.html) | **A** |
| 29 | Hand-in-the-Loop | arXiv 2026.05 | 人在环干预与灵巧手 VLA 策略纠正 | [原文入口](https://arxiv.org/abs/2605.15157) | **S** |
| 30 | ADEPT | CoRL 2026 | 强化学习预训练与后训练、视触觉策略 | [原文入口](https://arxiv.org/abs/2608.19182) | **S** |

<a id="category-4"></a>

## 05. VLA 与通用灵巧操作基础模型 (5)

如何通过统一模型实现跨任务、跨本体泛化？

| 编号 | 论文 | 发表情况 | 核心内容 | 原文 | 优先级 |
| --- | --- | --- | --- | --- | --- |
| 31 | GR-Dexter | Technical report 2025.12 | 字节 Seed：双臂灵巧手硬件、数据、VLA 一体化 | [原文入口](https://arxiv.org/abs/2512.24210) | **S** |
| 32 | XRZero-G0 | arXiv 2026.04 | 自变量机器人：数据规模、质量、配比与跨本体迁移 | [原文入口](https://arxiv.org/abs/2604.13001) | **S** |
| 33 | LingBot-VLA 2.0 | arXiv 2026.07 | 蚂蚁灵波：预测式表征与统一动作空间 | [原文入口](https://arxiv.org/abs/2607.06403) | **A** |
| 34 | Motus2 | arXiv 2026.08 | 生数科技等：自进化通用世界模型与灵巧操作 | [原文入口](https://arxiv.org/abs/2608.30237) | **S** |
| 35 | GR00T 2 | Technical report 2026.11 | NVIDIA：通用灵巧操作、跨本体泛化与后训练 | [原文入口](https://research.nvidia.com/labs/gear/gr00t-2/assets/gr00t2_whitepaper.pdf) | **S** |

<a id="category-5"></a>

## 06. 世界模型、动力学建模与接触控制 (8)

如何预测动作的物理后果并指导控制？

| 编号 | 论文 | 发表情况 | 核心内容 | 原文 | 优先级 |
| --- | --- | --- | --- | --- | --- |
| 36 | Contact-Implicit MPC for Dexterous In-hand Manipulation | IROS 2024 | 接触隐式动力学与长时域 MPC | [原文入口](https://ieeexplore.ieee.org/abstract/document/10801751) | **A** |
| 37 | Scaling Cross-Embodiment World Models for Dexterous Manipulation | IROS 2026 | 跨本体统一动力学建模 | [原文入口](https://arxiv.org/abs/2511.01177) | **S** |
| 38 | World Models for Learning Dexterous Hand-Object Interactions from Human Videos (DexWM) | ECCV 2026 | 基于人类视频学习手物交互动力学 | [原文入口](https://arxiv.org/abs/2512.13644) | **S** |
| 39 | Dexterous World Models (DWM) | CVPR 2026 | 动作条件下的视频扩散世界模型 | [原文入口](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html) | **A** |
| 40 | DexTouch-WM | arXiv 2026.09 | 动作条件下的触觉世界模型 | [原文入口](https://arxiv.org/abs/2609.20649) | **S** |
| 41 | PointWAM | arXiv 2026.10 | 三维点轨迹世界动作模型 | [原文入口](https://arxiv.org/abs/2610.02840) | **S** |
| 42 | ACTS | arXiv 2026.10 | 从人类物理交互学习视触觉世界模型 | [原文入口](https://arxiv.org/abs/2610.24285) | **A** |
| 43 | DexFLEX | CoRL 2026 | 接触感知基础控制器 | [原文入口](https://arxiv.org/abs/2610.14372) | **S** |

<a id="category-6"></a>

## 07. 灵巧抓取与基础数据集 (1)

如何生成稳定且物理可行的抓取姿态？

| 编号 | 论文 | 发表情况 | 核心内容 | 原文 | 优先级 |
| --- | --- | --- | --- | --- | --- |
| 44 | DexGraspNet | ICRA 2023 | 大规模灵巧抓取数据集与物理约束优化 | [原文入口](https://pku-epic.github.io/DexGraspNet/) | **B** |

<a id="core-reading"></a>

## 核心精读清单（20篇）

先读综述，再按顺序阅读代表性工作。此处仅引用上方编号，不计入新增文献。可勾选记录精读进度。

- [ ] #45 — [Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey of Hardware, Data, Cross-Embodiment Transfer, Learning, and Evaluation](https://arxiv.org/abs/2611.06724) — arXiv 2026.11
- [ ] #02 — [DexCap](https://dex-cap.github.io/) — RSS 2024
- [ ] #06 — [DexUMI](https://proceedings.mlr.press/v305/xu25b.html) — CoRL 2025
- [ ] #05 — [Dex1B](https://roboticsproceedings.org/rss21/p106.html) — RSS 2025
- [ ] #12 — [ReDex](https://psycho811.github.io/ReDex/) — IROS 2026
- [ ] #14 — [Rotating without Seeing](https://roboticsproceedings.org/rss19/p036.html) — RSS 2023
- [ ] #17 — [ViTacFormer](https://roboticsproceedings.org/rss22/p129.html) — RSS 2026
- [ ] #18 — [T-Rex](https://arxiv.org/abs/2606.17055) — CoRL 2026
- [ ] #20 — [TouchWorld](https://arxiv.org/abs/2607.07287) — arXiv 2026.07
- [ ] #22 — [Spark-0](https://arxiv.org/abs/2610.22342) — arXiv 2026.10
- [ ] #23 — [LingBot-Touch](https://arxiv.org/abs/2611.12806) — arXiv 2026.11
- [ ] #24 — [In-Hand Object Rotation via Rapid Motor Adaptation](https://proceedings.mlr.press/v205/qi23a.html) — CoRL 2022
- [ ] #30 — [ADEPT](https://arxiv.org/abs/2608.19182) — CoRL 2026
- [ ] #29 — [Hand-in-the-Loop](https://arxiv.org/abs/2605.15157) — arXiv 2026.05
- [ ] #31 — [GR-Dexter](https://arxiv.org/abs/2512.24210) — Technical report 2025.12
- [ ] #35 — [GR00T 2](https://research.nvidia.com/labs/gear/gr00t-2/assets/gr00t2_whitepaper.pdf) — Technical report 2026.11
- [ ] #34 — [Motus2](https://arxiv.org/abs/2608.30237) — arXiv 2026.08
- [ ] #37 — [Scaling Cross-Embodiment World Models for Dexterous Manipulation](https://arxiv.org/abs/2511.01177) — IROS 2026
- [ ] #40 — [DexTouch-WM](https://arxiv.org/abs/2609.20649) — arXiv 2026.09
- [ ] #43 — [DexFLEX](https://arxiv.org/abs/2610.14372) — CoRL 2026

### 单篇论文阅读模板

```text
研究问题 / 研究动机 / 核心创新
输入 / 输出 / 模型架构
训练数据 / 优化目标 / 训练流程
真机评估 / 泛化能力 / 消融实验
局限 / 可复现性 / 潜在研究机会
```

<a id="resources"></a>

## 相关资源

- [Awesome Dexterous Manipulation](https://github.com/chang-xinhai/Awesome-Dexterous-Manipulation)
- [Awesome Robot Data Engine](https://github.com/chang-xinhai/Awesome-Robot-Data-Engine)
- [Awesome UMI](https://github.com/chang-xinhai/Awesome-UMI)
- [Awesome World Action Models](https://github.com/rcl-robotics/Awesome-World-Action-Models)
- [CoRL / PMLR](https://proceedings.mlr.press/)
- [RSS Proceedings](https://roboticsproceedings.org/)
- [ICRA / IROS / IEEE Xplore](https://ieeexplore.ieee.org/)
- [Awesome list guidelines](https://github.com/sindresorhus/awesome/blob/main/awesome.md)

<a id="contributing"></a>

## 贡献指南

欢迎通过 Issue 或 Pull Request 补充新论文、纠正链接及会议归属。具体收录和去重规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。
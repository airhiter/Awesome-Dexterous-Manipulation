# Awesome Dexterous Manipulation Papers

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Papers](https://img.shields.io/badge/Papers-45-blue) ![Updated](https://img.shields.io/badge/Updated-2026--11--26-informational)

[English](README.md) | [简体中文](README.zh-CN.md)

A curated reading list of dexterous robotic manipulation papers, including robotics conferences, related venues, industry technical reports and arXiv preprints.

**Literature cutoff:** 2026-11-26 · **45 entries**

## Contents

- [Surveys (1)](#category-7)
- [Data Acquisition, Imitation Learning and Cross-Embodiment Transfer (13)](#category-1)
- [Tactile Sensing and Multimodal Learning (10)](#category-2)
- [Reinforcement Learning, Sim-to-Real and Post-training (7)](#category-3)
- [VLA and Generalist Foundation Models (5)](#category-4)
- [World Models, Dynamics and Contact Control (8)](#category-5)
- [Dexterous Grasping and Datasets (1)](#category-6)
- [Core Reading List (20)](#core-reading)
- [Resources](#resources)
- [Contributing](#contributing)

**Reading priority:** S = deep reading; A = full reading; B = supplementary.

<a id="category-7"></a>

## 01. Surveys (1)

Where should a newcomer start?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 45 | Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey of Hardware, Data, Cross-Embodiment Transfer, Learning, and Evaluation | arXiv 2026.11 | Full-stack overview of dexterous robotic hands | [Source](https://arxiv.org/abs/2611.06724) | **S** |

<a id="category-1"></a>

## 02. Data Acquisition, Imitation Learning and Cross-Embodiment Transfer (13)

How can we obtain high-quality and scalable demonstrations?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 01 | AnyTeleop | RSS 2023 | General vision-based teleoperation and motion retargeting | [Source](https://roboticsproceedings.org/rss19/p015.html) | **A** |
| 02 | DexCap | RSS 2024 | Portable motion capture and imitation learning | [Source](https://dex-cap.github.io/) | **S** |
| 03 | Tilde | RSS 2024 | Low-cost dexterous teleoperation | [Source](https://roboticsproceedings.org/rss20/p128.html) | **B** |
| 04 | DexWild | RSS 2025 | Human demonstration collection in natural environments | [Source](https://roboticsproceedings.org/rss21/p075.html) | **A** |
| 05 | Dex1B | RSS 2025 | Large-scale synthetic demonstrations and policy learning | [Source](https://roboticsproceedings.org/rss21/p106.html) | **S** |
| 06 | DexUMI | CoRL 2025 | Human hands as a universal data collection interface | [Source](https://proceedings.mlr.press/v305/xu25b.html) | **S** |
| 07 | DEXOP | arXiv 2025 | Exoskeleton-based multimodal demonstration collection | [Source](https://arxiv.org/abs/2509.04441) | **A** |
| 08 | EgoDex | ICLR 2026 | Apple egocentric human manipulation dataset | [Source](https://machinelearning.apple.com/research/egodex-learning-dexterous-manipulation) | **A** |
| 09 | Dexterity from Smart Lenses | ICRA 2026 | Human demonstration collection using smart glasses | [Source](https://ieeexplore.ieee.org/abstract/document/11697220) | **A** |
| 10 | UniDex | CVPR 2026 | Human video and general-purpose dexterous policies | [Source](https://unidex-ai.github.io/) | **S** |
| 11 | DexImit | RSS 2026 | Bimanual manipulation from monocular human videos | [Source](https://roboticsproceedings.org/rss22/p003.html) | **S** |
| 12 | ReDex | IROS 2026 | Cross-embodiment transfer using relational geometric priors | [Source](https://psycho811.github.io/ReDex/) | **S** |
| 13 | RealDexUMI | arXiv 2026 | Wearable dexterous manipulation data collection | [Source](https://research.beingbeyond.com/realdexumi) | **A** |

<a id="category-2"></a>

## 03. Tactile Sensing and Multimodal Learning (10)

How can robots sense contact, friction, slip and force?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 14 | Rotating without Seeing | RSS 2023 | Vision-free tactile in-hand rotation | [Source](https://roboticsproceedings.org/rss19/p036.html) | **S** |
| 15 | KineDex | CoRL 2025 | Kinesthetic teaching and tactile force-aware policies | [Source](https://proceedings.mlr.press/v305/zhang25l.html) | **A** |
| 16 | Text2Touch | CoRL 2025 | LLM-assisted tactile RL reward design | [Source](https://proceedings.mlr.press/v305/field25a.html) | **B** |
| 17 | ViTacFormer | RSS 2026 | Cross-modal visual-tactile representations | [Source](https://roboticsproceedings.org/rss22/p129.html) | **S** |
| 18 | T-Rex | CoRL 2026 | High-frequency tactile feedback and variable-frequency MoT | [Source](https://arxiv.org/abs/2606.17055) | **S** |
| 19 | TTP | arXiv 2026.07 | Human tactile pretraining and transfer | [Source](https://arxiv.org/abs/2607.01067) | **S** |
| 20 | TouchWorld | arXiv 2026.07 | Predictive and reactive tactile foundation model | [Source](https://arxiv.org/abs/2607.07287) | **S** |
| 21 | Dex-X | arXiv 2026.09 | Visual-tactile learning from human video and simulation | [Source](https://arxiv.org/abs/2609.07747) | **A** |
| 22 | Spark-0 | arXiv 2026.10 | Large-scale spatially aligned tactile pretraining | [Source](https://arxiv.org/abs/2610.22342) | **S** |
| 23 | LingBot-Touch | arXiv 2026.11 | Unified representation of heterogeneous tactile sensors | [Source](https://arxiv.org/abs/2611.12806) | **S** |

<a id="category-3"></a>

## 04. Reinforcement Learning, Sim-to-Real and Post-training (7)

How can interaction and policy improvement enhance dexterity?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 24 | In-Hand Object Rotation via Rapid Motor Adaptation | CoRL 2022 | Implicit physics estimation and rapid online adaptation | [Source](https://proceedings.mlr.press/v205/qi23a.html) | **S** |
| 25 | DexPoint | CoRL 2022 | Point-cloud representation, contact rewards and sim-to-real | [Source](https://proceedings.mlr.press/v205/qin23a.html) | **A** |
| 26 | Dexplore | CoRL 2025 | Policy exploration guided by human motion priors | [Source](https://proceedings.mlr.press/v305/xu25d.html) | **A** |
| 27 | DexCtrl | ICRA 2026 | Adaptive control and sim-to-real transfer | [Source](https://arxiv.org/abs/2505.00991) | **A** |
| 28 | SimToolReal | RSS 2026 | Object-centric representation and zero-shot tool use | [Source](https://roboticsproceedings.org/rss22/p151.html) | **A** |
| 29 | Hand-in-the-Loop | arXiv 2026.05 | Human-in-the-loop correction of dexterous VLA policies | [Source](https://arxiv.org/abs/2605.15157) | **S** |
| 30 | ADEPT | CoRL 2026 | RL pretraining and post-training with visual-tactile policies | [Source](https://arxiv.org/abs/2608.19182) | **S** |

<a id="category-4"></a>

## 05. VLA and Generalist Foundation Models (5)

How can a shared model generalize across tasks and embodiments?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 31 | GR-Dexter | Technical report 2025.12 | ByteDance Seed: integrated bimanual hardware, data and VLA | [Source](https://arxiv.org/abs/2512.24210) | **S** |
| 32 | XRZero-G0 | arXiv 2026.04 | Data scale, quality, mixture and cross-embodiment transfer | [Source](https://arxiv.org/abs/2604.13001) | **S** |
| 33 | LingBot-VLA 2.0 | arXiv 2026.07 | Robbyant: predictive representation and unified action space | [Source](https://arxiv.org/abs/2607.06403) | **A** |
| 34 | Motus2 | arXiv 2026.08 | Self-evolving generalist world model and dexterous manipulation | [Source](https://arxiv.org/abs/2608.30237) | **S** |
| 35 | GR00T 2 | Technical report 2026.11 | NVIDIA: generalist dexterity, transfer and post-training | [Source](https://research.nvidia.com/labs/gear/gr00t-2/assets/gr00t2_whitepaper.pdf) | **S** |

<a id="category-5"></a>

## 06. World Models, Dynamics and Contact Control (8)

How can models predict physical consequences and guide control?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 36 | Contact-Implicit MPC for Dexterous In-hand Manipulation | IROS 2024 | Contact-implicit dynamics and long-horizon MPC | [Source](https://ieeexplore.ieee.org/abstract/document/10801751) | **A** |
| 37 | Scaling Cross-Embodiment World Models for Dexterous Manipulation | IROS 2026 | Unified cross-embodiment dynamics | [Source](https://arxiv.org/abs/2511.01177) | **S** |
| 38 | World Models for Learning Dexterous Hand-Object Interactions from Human Videos (DexWM) | ECCV 2026 | Hand-object dynamics learned from human videos | [Source](https://arxiv.org/abs/2512.13644) | **S** |
| 39 | Dexterous World Models (DWM) | CVPR 2026 | Action-conditioned video diffusion world model | [Source](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html) | **A** |
| 40 | DexTouch-WM | arXiv 2026.09 | Action-conditioned tactile world model | [Source](https://arxiv.org/abs/2609.20649) | **S** |
| 41 | PointWAM | arXiv 2026.10 | 3D point-trajectory world-action model | [Source](https://arxiv.org/abs/2610.02840) | **S** |
| 42 | ACTS | arXiv 2026.10 | Visual-tactile world models from human physical interaction | [Source](https://arxiv.org/abs/2610.24285) | **A** |
| 43 | DexFLEX | CoRL 2026 | Contact-aware foundation controller | [Source](https://arxiv.org/abs/2610.14372) | **S** |

<a id="category-6"></a>

## 07. Dexterous Grasping and Datasets (1)

How can we generate stable and physically feasible grasps?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 44 | DexGraspNet | ICRA 2023 | Large-scale grasp dataset and physics-constrained optimization | [Source](https://pku-epic.github.io/DexGraspNet/) | **B** |

<a id="core-reading"></a>

## Core Reading List (20)

Read the survey first, then follow the selected papers. References point to the numbered entries above; the checkboxes are a reading plan, not additional bibliography entries.

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

### Paper review template

```text
Problem / Motivation / Key idea
Inputs / Outputs / Architecture
Training data / Objective / Training pipeline
Real-world evaluation / Generalization / Ablations
Limitations / Reproducibility / Research opportunities
```

<a id="resources"></a>

## Resources

- [Awesome Dexterous Manipulation](https://github.com/chang-xinhai/Awesome-Dexterous-Manipulation)
- [Awesome Robot Data Engine](https://github.com/chang-xinhai/Awesome-Robot-Data-Engine)
- [Awesome UMI](https://github.com/chang-xinhai/Awesome-UMI)
- [Awesome World Action Models](https://github.com/rcl-robotics/Awesome-World-Action-Models)
- [CoRL / PMLR](https://proceedings.mlr.press/)
- [RSS Proceedings](https://roboticsproceedings.org/)
- [ICRA / IROS / IEEE Xplore](https://ieeexplore.ieee.org/)
- [Awesome list guidelines](https://github.com/sindresorhus/awesome/blob/main/awesome.md)

<a id="contributing"></a>

## Contributing

Corrections and new papers are welcome via issues or pull requests. See [CONTRIBUTING.md](CONTRIBUTING.md) for the inclusion and deduplication rules.
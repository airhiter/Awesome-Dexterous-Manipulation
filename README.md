<div align="center">

# Awesome Dexterous Manipulation Papers

**Dexterous manipulation · Research papers · Reading roadmap**

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/Papers-49-2867B2?style=flat-square)
![Core Reading](https://img.shields.io/badge/Core%20Reading-20-7C3AED?style=flat-square)
![Updated](https://img.shields.io/badge/Updated-2026--11--26-16805D?style=flat-square)
[![GitHub Stars](https://img.shields.io/github/stars/airhiter/Awesome-Dexterous-Manipulation?style=flat-square)](https://github.com/airhiter/Awesome-Dexterous-Manipulation/stargazers)

[English](README.md) | [简体中文](README.zh-CN.md)

[Survey](#category-7) · [Core Reading](#core-reading) · [Resources](#resources) · [Contributing](#contributing)

</div>

## About

**Awesome Dexterous Manipulation Papers** brings together research on learning and control for dexterous robotic hands, including CoRL, RSS, ICRA, IROS and industry technical reports. Topics span data acquisition, tactile sensing, reinforcement learning, VLA, world models and dexterous grasping.

<p align="center">
  <a href="https://arxiv.org/abs/2504.03515"><img src="https://raw.githubusercontent.com/chang-xinhai/Awesome-Dexterous-Manipulation/main/assets/dexterous-manipulation-examples.png" alt="Real-world dexterous robotic manipulation examples" width="900"></a>
  <br>
  <sub>Real-world examples of dexterous manipulation. Source: Fig. 1, <a href="https://arxiv.org/abs/2504.03515">Dexterous Manipulation through Imitation Learning: A Survey</a> (An et al., 2025). Image hosted by <a href="https://github.com/chang-xinhai/Awesome-Dexterous-Manipulation">chang-xinhai/Awesome-Dexterous-Manipulation</a>.</sub>
</p>

**Literature cutoff:** 2026-11-26 · **49 papers · 7 categories · 20 core readings**

## Contents

- [Surveys (5)](#category-7)
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

## 01. Surveys (5)

Where should a newcomer start?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 01 | The Developments and Challenges Toward Dexterous and Embodied Robotic Manipulation: A Survey | IEEE RAM 2026 | Overview of embodied dexterity, data collection, learning frameworks and open challenges | [Source](https://doi.org/10.1109/MRA.2025.3642671) | **S** |
| 02 | Dexterous Manipulation Through Imitation Learning: A Survey | IEEE T-ASE 2026 | Imitation learning, demonstrations, teleoperation and dexterous manipulation | [Source](https://doi.org/10.1109/TASE.2025.3646183) | **S** |
| 03 | Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey of Hardware, Data, Cross-Embodiment Transfer, Learning, and Evaluation | arXiv 2026.11 | Full-stack overview of dexterous robotic hands | [Source](https://arxiv.org/abs/2611.06724) | **S** |
| 04 | Towards Robotic Dexterous Hand Intelligence: A Survey | arXiv 2026.05 | Hardware, control, learning, datasets and evaluation | [Source](https://arxiv.org/abs/2605.13925) | **A** |
| 05 | Survey of Learning-Based Approaches for Robotic In-Hand Manipulation | Frontiers in Robotics and AI 2024 | Model-based learning, reinforcement learning and imitation learning for in-hand manipulation | [Source](https://doi.org/10.3389/frobt.2024.1455431) | **A** |

**Suggested reading order:** Start with the IEEE RAM and IEEE T-ASE surveys to establish the field's foundations, then read the November 2026 full-stack survey for recent developments.

<a id="category-1"></a>

## 02. Data Acquisition, Imitation Learning and Cross-Embodiment Transfer (13)

How can we obtain high-quality and scalable demonstrations?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 06 | AnyTeleop | RSS 2023 | General vision-based teleoperation and motion retargeting | [Source](https://roboticsproceedings.org/rss19/p015.html) | **A** |
| 07 | DexCap | RSS 2024 | Portable motion capture and imitation learning | [Source](https://dex-cap.github.io/) | **S** |
| 08 | Tilde | RSS 2024 | Low-cost dexterous teleoperation | [Source](https://roboticsproceedings.org/rss20/p128.html) | **B** |
| 09 | DexWild | RSS 2025 | Human demonstration collection in natural environments | [Source](https://roboticsproceedings.org/rss21/p075.html) | **A** |
| 10 | Dex1B | RSS 2025 | Large-scale synthetic demonstrations and policy learning | [Source](https://roboticsproceedings.org/rss21/p106.html) | **S** |
| 11 | DexUMI | CoRL 2025 | Human hands as a universal data collection interface | [Source](https://proceedings.mlr.press/v305/xu25b.html) | **S** |
| 12 | DEXOP | arXiv 2025 | Exoskeleton-based multimodal demonstration collection | [Source](https://arxiv.org/abs/2509.04441) | **A** |
| 13 | EgoDex | ICLR 2026 | Apple egocentric human manipulation dataset | [Source](https://machinelearning.apple.com/research/egodex-learning-dexterous-manipulation) | **A** |
| 14 | Dexterity from Smart Lenses | ICRA 2026 | Human demonstration collection using smart glasses | [Source](https://ieeexplore.ieee.org/abstract/document/11697220) | **A** |
| 15 | UniDex | CVPR 2026 | Human video and general-purpose dexterous policies | [Source](https://unidex-ai.github.io/) | **S** |
| 16 | DexImit | RSS 2026 | Bimanual manipulation from monocular human videos | [Source](https://roboticsproceedings.org/rss22/p003.html) | **S** |
| 17 | ReDex | IROS 2026 | Cross-embodiment transfer using relational geometric priors | [Source](https://psycho811.github.io/ReDex/) | **S** |
| 18 | RealDexUMI | arXiv 2026 | Wearable dexterous manipulation data collection | [Source](https://research.beingbeyond.com/realdexumi) | **A** |

<a id="category-2"></a>

## 03. Tactile Sensing and Multimodal Learning (10)

How can robots sense contact, friction, slip and force?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 19 | Rotating without Seeing | RSS 2023 | Vision-free tactile in-hand rotation | [Source](https://roboticsproceedings.org/rss19/p036.html) | **S** |
| 20 | KineDex | CoRL 2025 | Kinesthetic teaching and tactile force-aware policies | [Source](https://proceedings.mlr.press/v305/zhang25l.html) | **A** |
| 21 | Text2Touch | CoRL 2025 | LLM-assisted tactile RL reward design | [Source](https://proceedings.mlr.press/v305/field25a.html) | **B** |
| 22 | ViTacFormer | RSS 2026 | Cross-modal visual-tactile representations | [Source](https://roboticsproceedings.org/rss22/p129.html) | **S** |
| 23 | T-Rex | CoRL 2026 | High-frequency tactile feedback and variable-frequency MoT | [Source](https://arxiv.org/abs/2606.17055) | **S** |
| 24 | TTP | arXiv 2026.07 | Human tactile pretraining and transfer | [Source](https://arxiv.org/abs/2607.01067) | **S** |
| 25 | TouchWorld | arXiv 2026.07 | Predictive and reactive tactile foundation model | [Source](https://arxiv.org/abs/2607.07287) | **S** |
| 26 | Dex-X | arXiv 2026.09 | Visual-tactile learning from human video and simulation | [Source](https://arxiv.org/abs/2609.07747) | **A** |
| 27 | Spark-0 | arXiv 2026.10 | Large-scale spatially aligned tactile pretraining | [Source](https://arxiv.org/abs/2610.22342) | **S** |
| 28 | LingBot-Touch | arXiv 2026.11 | Unified representation of heterogeneous tactile sensors | [Source](https://arxiv.org/abs/2611.12806) | **S** |

<a id="category-3"></a>

## 04. Reinforcement Learning, Sim-to-Real and Post-training (7)

How can interaction and policy improvement enhance dexterity?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 29 | In-Hand Object Rotation via Rapid Motor Adaptation | CoRL 2022 | Implicit physics estimation and rapid online adaptation | [Source](https://proceedings.mlr.press/v205/qi23a.html) | **S** |
| 30 | DexPoint | CoRL 2022 | Point-cloud representation, contact rewards and sim-to-real | [Source](https://proceedings.mlr.press/v205/qin23a.html) | **A** |
| 31 | Dexplore | CoRL 2025 | Policy exploration guided by human motion priors | [Source](https://proceedings.mlr.press/v305/xu25d.html) | **A** |
| 32 | DexCtrl | ICRA 2026 | Adaptive control and sim-to-real transfer | [Source](https://arxiv.org/abs/2505.00991) | **A** |
| 33 | SimToolReal | RSS 2026 | Object-centric representation and zero-shot tool use | [Source](https://roboticsproceedings.org/rss22/p151.html) | **A** |
| 34 | Hand-in-the-Loop | arXiv 2026.05 | Human-in-the-loop correction of dexterous VLA policies | [Source](https://arxiv.org/abs/2605.15157) | **S** |
| 35 | ADEPT | CoRL 2026 | RL pretraining and post-training with visual-tactile policies | [Source](https://arxiv.org/abs/2608.19182) | **S** |

<a id="category-4"></a>

## 05. VLA and Generalist Foundation Models (5)

How can a shared model generalize across tasks and embodiments?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 36 | GR-Dexter | Technical report 2025.12 | ByteDance Seed: integrated bimanual hardware, data and VLA | [Source](https://arxiv.org/abs/2512.24210) | **S** |
| 37 | XRZero-G0 | arXiv 2026.04 | Data scale, quality, mixture and cross-embodiment transfer | [Source](https://arxiv.org/abs/2604.13001) | **S** |
| 38 | LingBot-VLA 2.0 | arXiv 2026.07 | Robbyant: predictive representation and unified action space | [Source](https://arxiv.org/abs/2607.06403) | **A** |
| 39 | Motus2 | arXiv 2026.08 | Self-evolving generalist world model and dexterous manipulation | [Source](https://arxiv.org/abs/2608.30237) | **S** |
| 40 | GR00T 2 | Technical report 2026.11 | NVIDIA: generalist dexterity, transfer and post-training | [Source](https://research.nvidia.com/labs/gear/gr00t-2/assets/gr00t2_whitepaper.pdf) | **S** |

<a id="category-5"></a>

## 06. World Models, Dynamics and Contact Control (8)

How can models predict physical consequences and guide control?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 41 | Contact-Implicit MPC for Dexterous In-hand Manipulation | IROS 2024 | Contact-implicit dynamics and long-horizon MPC | [Source](https://ieeexplore.ieee.org/abstract/document/10801751) | **A** |
| 42 | Scaling Cross-Embodiment World Models for Dexterous Manipulation | IROS 2026 | Unified cross-embodiment dynamics | [Source](https://arxiv.org/abs/2511.01177) | **S** |
| 43 | World Models for Learning Dexterous Hand-Object Interactions from Human Videos (DexWM) | ECCV 2026 | Hand-object dynamics learned from human videos | [Source](https://arxiv.org/abs/2512.13644) | **S** |
| 44 | Dexterous World Models (DWM) | CVPR 2026 | Action-conditioned video diffusion world model | [Source](https://openaccess.thecvf.com/content/CVPR2026/html/Kim_Dexterous_World_Models_CVPR_2026_paper.html) | **A** |
| 45 | DexTouch-WM | arXiv 2026.09 | Action-conditioned tactile world model | [Source](https://arxiv.org/abs/2609.20649) | **S** |
| 46 | PointWAM | arXiv 2026.10 | 3D point-trajectory world-action model | [Source](https://arxiv.org/abs/2610.02840) | **S** |
| 47 | ACTS | arXiv 2026.10 | Visual-tactile world models from human physical interaction | [Source](https://arxiv.org/abs/2610.24285) | **A** |
| 48 | DexFLEX | CoRL 2026 | Contact-aware foundation controller | [Source](https://arxiv.org/abs/2610.14372) | **S** |

<a id="category-6"></a>

## 07. Dexterous Grasping and Datasets (1)

How can we generate stable and physically feasible grasps?

| ID | Paper | Venue / Status | Focus | Source | Priority |
| --- | --- | --- | --- | --- | --- |
| 49 | DexGraspNet | ICRA 2023 | Large-scale grasp dataset and physics-constrained optimization | [Source](https://pku-epic.github.io/DexGraspNet/) | **B** |

<a id="core-reading"></a>

## Core Reading List (20)

Read the survey first, then follow the selected papers. References point to the numbered entries above; the checkboxes are a reading plan, not additional bibliography entries.

- [ ] #03 — [Dexterous Robotic Hands in the Foundation-Model Era: A Full-Stack Survey of Hardware, Data, Cross-Embodiment Transfer, Learning, and Evaluation](https://arxiv.org/abs/2611.06724) — arXiv 2026.11
- [ ] #07 — [DexCap](https://dex-cap.github.io/) — RSS 2024
- [ ] #11 — [DexUMI](https://proceedings.mlr.press/v305/xu25b.html) — CoRL 2025
- [ ] #10 — [Dex1B](https://roboticsproceedings.org/rss21/p106.html) — RSS 2025
- [ ] #17 — [ReDex](https://psycho811.github.io/ReDex/) — IROS 2026
- [ ] #19 — [Rotating without Seeing](https://roboticsproceedings.org/rss19/p036.html) — RSS 2023
- [ ] #22 — [ViTacFormer](https://roboticsproceedings.org/rss22/p129.html) — RSS 2026
- [ ] #23 — [T-Rex](https://arxiv.org/abs/2606.17055) — CoRL 2026
- [ ] #25 — [TouchWorld](https://arxiv.org/abs/2607.07287) — arXiv 2026.07
- [ ] #27 — [Spark-0](https://arxiv.org/abs/2610.22342) — arXiv 2026.10
- [ ] #28 — [LingBot-Touch](https://arxiv.org/abs/2611.12806) — arXiv 2026.11
- [ ] #29 — [In-Hand Object Rotation via Rapid Motor Adaptation](https://proceedings.mlr.press/v205/qi23a.html) — CoRL 2022
- [ ] #35 — [ADEPT](https://arxiv.org/abs/2608.19182) — CoRL 2026
- [ ] #34 — [Hand-in-the-Loop](https://arxiv.org/abs/2605.15157) — arXiv 2026.05
- [ ] #36 — [GR-Dexter](https://arxiv.org/abs/2512.24210) — Technical report 2025.12
- [ ] #40 — [GR00T 2](https://research.nvidia.com/labs/gear/gr00t-2/assets/gr00t2_whitepaper.pdf) — Technical report 2026.11
- [ ] #39 — [Motus2](https://arxiv.org/abs/2608.30237) — arXiv 2026.08
- [ ] #42 — [Scaling Cross-Embodiment World Models for Dexterous Manipulation](https://arxiv.org/abs/2511.01177) — IROS 2026
- [ ] #45 — [DexTouch-WM](https://arxiv.org/abs/2609.20649) — arXiv 2026.09
- [ ] #48 — [DexFLEX](https://arxiv.org/abs/2610.14372) — CoRL 2026

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
# Routing reference

Use sibling skills in the installed destination. The catalog below is a mapping, not proof that a skill has executed.

| Trigger | Skill | Prerequisite / parallel boundary |
|---|---|---|
| 地震动分析 | [ground-motion-analysis](../../ground-motion-analysis/SKILL.md) | Inspect inputs before analysis; see its workflow |
| GMM 残差分析 | [gmm-residual-analysis](../../gmm-residual-analysis/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 混合效应 REML | [mixed-effects-reml](../../mixed-effects-reml/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 震源—路径—场地分解 | [event-path-site-decomposition](../../event-path-site-decomposition/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 随机振动模拟 | [random-vibration-simulation](../../random-vibration-simulation/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 情景地震 | [scenario-earthquake](../../scenario-earthquake/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 地震快速研判 | [earthquake-rapid-analysis](../../earthquake-rapid-analysis/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 证据链 | [evidence-chain](../../evidence-chain/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 图件审计 | [figure-audit](../../figure-audit/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 论文主线 | [paper-storyline](../../paper-storyline/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 审稿视角审计 | [reviewer-audit](../../reviewer-audit/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 可复现性审计 | [reproducibility-audit](../../reproducibility-audit/SKILL.md) | Inspect inputs before analysis; see its workflow |
| 期刊技能桥接 | [journal-bridge](../../journal-bridge/SKILL.md) | Inspect inputs before analysis; see its workflow |

## Dependency examples

- Waveforms → ground-motion-analysis → gmm-residual-analysis → mixed-effects-reml → event-path-site-decomposition.
- Verified result tables → evidence-chain → paper-storyline; reviewer-audit can assess an existing manuscript alongside figure-audit and reproducibility-audit.
- random-vibration-simulation and scenario-earthquake share parameter validation; neither substitutes for observed validation.
- earthquake-rapid-analysis can call scenario-earthquake for explicitly provisional modeled estimates.
- journal-bridge applies journal constraints after research claims and evidence have been checked.

For concurrent branches, record inputs, output directory, required skill, acceptance condition and artifact IDs. Write no shared mutable tables from multiple workers. Review and reconcile results before dependent writing.

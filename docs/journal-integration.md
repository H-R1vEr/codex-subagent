# Optional Journal Skills integration

ResearchFlow owns the domain/evidence workflows. Journal packages supply additional editorial constraints. No third-party skill text is copied, downloaded by default, or relicensed here.

## Verified upstream

The upstream [brycewang-stanford/Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills) was checked on 2026-09-30 at commit `932eb23331721b16e967c59f093781be1928b498`. Its [root license at that revision](https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/932eb23331721b16e967c59f093781be1928b498/LICENSE) is MIT, copyright 2026 Bryce Wang. MIT permits reuse subject to notice preservation, but this repository still uses external installation to avoid vendoring and permit independent upstream updates. Review the specific package's license and instructions before use; this snapshot is not a guarantee about future revisions or all linked material.

## Reproducible optional setup

```bash
git clone https://github.com/brycewang-stanford/Awesome-Journal-Skills.git /path/to/journal-skills
git -C /path/to/journal-skills checkout 932eb23331721b16e967c59f093781be1928b498
```

Use real local paths; on Windows choose a Windows path instead of `/path/to`. At the pinned revision, `Cell-Skills/skills/` contains `cell-workflow` and eleven other skills; `Science-Skills/skills/` contains `sci-workflow` and eleven others. Both package LICENSE files were checked and state MIT, copyright 2026 Bryce Wang.

There is **no standalone `Nature-Skills` directory at this revision**. Nature-family entries exist in broader subject suites, for example `English-NaturalScience-Journal-Skills/skills/nature-astronomy/`. Do not present those as a complete Nature main-journal workflow suite. For Nature, independently select/review an available Nature skill source or use current publisher instructions through the bridge; its absence does not block the original research workflows.

Inspect the chosen package's LICENSE and SKILL.md files. Copy only the chosen complete skill directories from its `skills/` into your configured `.agents/skills` destination, without colliding with existing names. Preserve required copyright/license notices alongside any copied material. Alternatively ask the available `$skill-installer` to install a reviewed specific repository path/ref; confirm that the tool supports pinning before using it. Do not copy the outer journal suite as though it were a single skill.

After installation, use `$journal-bridge` with the target journal/article type. It discovers actual installed names rather than assuming an upstream router name. Record the upstream revision, selected skills and license checks in your research manifest. If unavailable, the bridge proceeds with research checks and labels journal-specific requirements unchecked.

## Author instructions are a separate source

- [Cell author information](https://www.cell.com/cell/authors)
- [Nature submission guidance](https://www.nature.com/nature/for-authors)
- [Science author information](https://www.science.org/content/page/instructions-preparing-initial-manuscript)

These are publisher entry points, not a verified list of current word limits. Verify the relevant article-type rules at use time and cite retrieval dates. Never infer endorsement, suitability or acceptance from a package name.

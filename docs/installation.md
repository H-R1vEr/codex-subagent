# Installation and removal

The installer copies complete original skill folders from `skills/`. It is local-only and downloads no dependencies or third-party packages. Python 3.10+ is required; `requirements-dev.txt` is only needed for lint/docs development.

## Windows

```powershell
.\scripts\install.ps1 -Scope user -Skill gmm-residual-analysis,mixed-effects-reml -DryRun
.\scripts\install.ps1 -Scope user -Skill gmm-residual-analysis,mixed-effects-reml
```

If local execution policy blocks a trusted, reviewed script, follow your organization's policy. You can use the equivalent `python scripts/install.py --scope user` without changing execution policy. `-Python` accepts the actual Python executable when the default launcher is unavailable.

## macOS and Linux

```bash
bash scripts/install.sh --scope user --skill gmm-residual-analysis --skill mixed-effects-reml
# Override interpreter when needed:
PYTHON=/path/to/python3 bash scripts/install.sh --scope user
```

Project installs require an explicit existing project root. Custom destinations are supported via `--destination PATH` or `-Destination PATH`. For explicit legacy installation choose your host's configured `.codex/skills` path; current default discovery is `.agents/skills`. Do not install duplicate skill names in multiple scopes.

## Collisions, updates and removal

Existing skill directories cause the entire installation preflight to fail before copying anything. Back up the relevant directories before manually replacing them with a reviewed version. There is deliberately no force-delete or silent upgrade option. Installation prints an exact plan and returns nonzero on failure. Dry-run creates nothing. To remove, inspect the exact installed directories from the plan and manually remove only those folders; unrelated skills must remain.

## Confirm discovery

Ask Codex to use `$evidence-chain` on a small supplied claim table and confirm that it reads the installed `SKILL.md`. Installation smoke tests confirm copied files, not actual model selection. Restart Codex if discovery has not refreshed. See [official guidance](https://developers.openai.com/codex/skills/).

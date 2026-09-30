# Validation scope

`python scripts/validate.py` checks all original skills: parseable YAML frontmatter; matching names; useful descriptions; body; supported resource folders; UI metadata; catalog consistency; local Markdown/image and HTML asset links and Markdown anchors; required repository files; and unfinished scaffold markers. External URL reachability is intentionally not a release gate because transient networks and publisher access vary.

`python -m unittest discover -s tests -v` exercises installation into temporary user-selected paths, whole-run collision refusal, dry-run purity, selective installation, malformed names/traversal rejection, symlink boundaries, and corrupt frontmatter/broken-link detection. It also runs the synthetic residual fixture.

`python scripts/build_docs.py` renders Markdown into a complete static `site/`, rewriting local links and preserving assets. The HTML homepage is also independently viewable offline. GitHub Actions runs validation and tests on three operating systems; Pages build runs on Ubuntu and deploys only after validation/tests succeed.

## Behavioral checks for users

Each skill includes an acceptance scenario. Run those with an installed skill and actual Codex to check selection and judgment. In particular: unit mismatch; duplicate joins; REML fixed-effect comparisons; unidentifiable path/site effects; missing journal skills; and source-versus-model confusion. Model behavior is nondeterministic and needs review.

V1 local delivery reports tests actually run separately from checks that only exist in CI. Structural passing does not validate earthquake simulation, GMM implementations, REML inference or manuscript claims. The synthetic demo tests arithmetic and evidence labeling only.

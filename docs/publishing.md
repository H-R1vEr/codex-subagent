# Publish to GitHub and Pages

The local repository is ready to review. Publishing needs your account and repository destination; no account name is hard-coded. Review the license/contributor ownership, skill instructions and test results before uploading. Do not include `work/` from the parent workspace or unpublished research data.

1. Create an empty public GitHub repository named `ResearchFlow-Skills` under your chosen account.
2. From this repository root, initialize Git if needed, commit the reviewed files, add the actual remote and push `main`. This package does not automatically push.
3. Confirm the validation workflow succeeds. Under **Settings → Pages → Build and deployment**, select **GitHub Actions**.
4. Run **Deploy docs to Pages** manually or push a reviewed change to `main`. The Pages environment may require approval depending on your settings.
5. Use the URL returned by deployment; update GitHub's About/website field. No fabricated live URL or badge is included before publication.

The Pages workflow renders a site with functioning documentation and skill-page links. Relative paths support a project subpath. No third-party skills, analytics or external JavaScript are deployed. For local preview run `python scripts/build_docs.py`, then `python -m http.server 8000 --directory site` and open `http://localhost:8000`.

Recommend a first `v1.0.0` release after remote CI and actual Codex discovery checks. The repository version describes package contents; scientific acceptance remains task-specific.

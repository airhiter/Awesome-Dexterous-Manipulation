# AGENTS.md

## Mission
Maintain a focused, bilingual Awesome list of dexterous robot manipulation research. Prioritize relevant recent work from CoRL, RSS, ICRA, IROS and other strong venues, as well as substantial public technical reports and preprints.

## Canonical content
- `README.md` is the English canonical list; `README.zh-CN.md` is its Chinese counterpart.
- Keep these seven flat categories in their current order:
  1. Surveys
  2. Data Acquisition, Imitation Learning and Cross-Embodiment Transfer
  3. Tactile Sensing and Multimodal Learning
  4. Reinforcement Learning, Sim-to-Real and Post-training
  5. VLA and Generalist Foundation Models
  6. World Models, Dynamics and Contact Control
  7. Dexterous Grasping and Datasets
- Assign each paper exactly one main category based on its principal contribution. Do not create new subcategories or change the taxonomy without the maintainer's request.
- Keep paper IDs consecutive in display order, preserve existing paper information unless correcting verified errors, and update the references in the core reading list when IDs change.

## Adding papers
1. Search this repository first, then search GitHub and relevant official proceedings, arXiv, OpenReview, DOI records or author project pages.
2. Deduplicate by title, acronym, DOI and arXiv ID. A preprint and its published version are one entry.
3. Confirm the paper's identity, exact title and publication status from authoritative sources. If only a preprint is verifiable, label it arXiv; never infer acceptance from an unofficial list.
4. Add a concise technical focus, canonical source link and S/A/B reading priority. Do not invent authors, metrics, acceptance status or code availability.
5. Update both READMEs with identical IDs, paper names, venue/status, canonical links and priorities; translate technical descriptions.
6. Update section counts, total badges, contents, cutoff date and News when appropriate. Do not expand the core reading list unless justified or requested.

## Quality checks
Run from the repository root:

```sh
python scripts/maintain_papers.py check
python scripts/maintain_papers.py export
```

The check verifies structural consistency, not scientific correctness. Optionally run `python scripts/maintain_papers.py links` to report reachable source URLs. Manually investigate failures and check paper metadata before changing entries. Respect publisher access controls and rate limits.

## Assets and repository hygiene
- Store original diagrams and authorized static assets under `assets/`; document source, author and permission in `assets/README.md`.
- Keep third-party figures attributed and do not copy images or papers into the repository without appropriate rights.
- Keep downloaded PDFs, exported files, credentials and local caches out of Git.
- Do not change LICENSE, citation authorship, or external service configuration without maintainer approval.
- Use small, descriptive commits; avoid unrelated formatting changes. Preserve bilingual navigation, acknowledgements, citation, license, contributors and star history.

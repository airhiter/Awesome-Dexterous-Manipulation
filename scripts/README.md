# Maintenance scripts

Requires Python 3.8+; no third-party dependencies.

Run from the repository root:

| Command | Purpose |
| --- | --- |
| `python scripts/maintain_papers.py check` | Validate consecutive IDs, category counts, duplicates, bilingual consistency and core references |
| `python scripts/maintain_papers.py export` | Export a UTF-8 CSV manifest to `exports/papers.csv` |
| `python scripts/maintain_papers.py links` | Check source URL reachability and write `exports/link_report.csv` |

Use `--output PATH` to select a CSV output path, or `--root PATH` to check another local checkout.

The export contains the source links and the metadata currently recorded in the README. It is a manifest for paper retrieval and bibliography tools, not a complete verified citation database. The link check does not bypass paywalls, download papers or confirm the scientific content of a source. HTTP 403, 429 and timeouts can be caused by access restrictions or rate limits.

本目录用于检查中英文文献库、连续编号、重复条目和精读清单，导出论文下载清单及链接检测报告。输出保存在已被 Git 忽略的 `exports/` 目录中。

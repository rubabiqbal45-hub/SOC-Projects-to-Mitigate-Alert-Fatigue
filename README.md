# SOC Alert Triage: Research Projects

Two Python projects that aim to reduce analyst alert fatigue in a Security Operations Center (SOC).

| Project | What it does | Tools |
| :--- | :--- | :--- |
| **1. ML Alert Triage and False-Positive Reduction Framework** | Parses structured logs, engineers features and scores alerts so analysts review the riskiest first. Includes risk-controlled suppression of low-risk alerts. | Python, feature engineering, gradient-boosted and baseline models |
| **2. SOC Alert Triage RAG Pipeline** | Enriches each alert with asset context from an internal database and writes a plain-language triage summary. | Python, `unittest` |

> **Note:** Project 1 was evaluated on a synthetic alert stream. The results show the pipeline and evaluation method work. They do not prove real-world performance.

---

## Project 1: Key results

Test window of a synthetic stream: 48,000 alerts over 81 days, 10 rules, 60 hosts, with a time-based train, calibration and test split.

| Result | Value |
| :--- | :--- |
| Alerts suppressed (primary mode) | 52.17% |
| Attacks still caught (recall) | 99.35% |
| Final model ROC-AUC (clean / under adversarial imitation) | 0.986 / 0.978 |
| Mean time in queue (simulated) | 366.1 min down to 4.8 min |
| SLA breach rate (simulated) | 96.3% down to 9.2% |
| Analysts needed to meet the SLA (simulated) | 19 down to 9 |

Limits: the data is synthetic, benign activity is cleaner than a real enterprise, and the queue parameters are assumed, not measured. A live SOC pilot would be needed before any operational claim.

---

## Project 2: Asset-aware triage

Alerts are routed by the criticality of the asset involved:

- **Critical assets:** elevated priority action.
- **Medium assets (normal workstations):** baseline Tier 1 monitoring.
- **Unknown assets (unregistered addresses):** low-risk tracking.

---

## Running the tests

From the repository root:

```bash
python -m unittest tests/test_data_loader.py
```

The tests check that:

- `test_critical_asset_matching`: critical endpoints trigger elevated priority.
- `test_medium_asset_matching`: normal workstations route to baseline Tier 1 monitoring.
- `test_unknown_asset_fallback`: unregistered addresses fall back to low-risk tracking.

Requires Python 3 (add the exact version you ran).

# Context-Aware Security Operations Triage Architecture

This repository hosts a dual-track cybersecurity research framework designed to optimize incident response workflows and mitigate analyst alert fatigue within modern Security Operations Centers (SOCs).

---

## 🗺️ Project Workspace Directory Layout

The codebase and research dossiers are partitioned into two distinct implementation tracks inside the `src/` directory. Click the links below to jump directly into each project's dedicated subfolder handbook:

| 📂 Research Implementation Track | 🔬 Core Research Focus | 🛠️ Primary Toolkit |
| :--- | :--- | :--- |
| **[Project 1: SOC Alert Fatigue Mitigation Project of NMF]** | Conceptual design methodology, telemetry stream parsing models, and neural matrix logical thresholds. | Python, Structured Data Matrices, Anomaly Profiling |
| **[Project 2: SOC Alert Triage RAG Pipeline Engine]** | Active runtime script automation pipeline, asset contextual database blending, and natural language triage reports. | Python 3.15, Native In-Context Prompts, `unittest` |

---

## 🧪 Automated Testing & Validation Framework

To ensure absolute logical precision across both tracking paths, the context-enrichment logic processes are fully monitored by a native unit testing suite.

To run the verification matrix from your root terminal, execute:
```bash
python -m unittest tests/test_data_loader.py
```

### Expected Validation Diagnostics:
*   `test_critical_asset_matching`: Verifies critical endpoints automatically trigger elevated priority action alerts.
*   `test_medium_asset_matching`: Confirms normal workspace nodes route safely to baseline Tier-1 monitoring templates.
*   `test_unknown_asset_fallback`: Validates unregistered network addresses gracefully drop to low-risk tracking scripts.

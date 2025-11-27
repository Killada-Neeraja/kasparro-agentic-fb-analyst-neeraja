# Kasparro — Agentic Facebook Performance Analyst

This repository implements a simple, modular **agentic system** that analyzes Facebook Ads performance for an undergarments brand. It produces insights, recommended creative strategies, and a validation report — fulfilling the assignment requirements for an agent-based pipeline.

---

## Quick Start
```bash
python -V  # should be >= 3.10
python -m venv .venv && source .venv/bin/activate  # win: .venv\Scripts\activate
pip install -r requirements.txt
python src/run.py "Analyze ROAS drop in last 7 days"


## Data
Dataset used: synthetic_fb_ads_undergarments.csv
Stored under data/
Contains campaign details including:
impressions, clicks, spend, revenue, ROAS, CTR, platform, creative_type, audience_type, country
Insights are generated directly from this dataset.

## Config
python: "3.10"
random_seed: 42
confidence_min: 0.6
use_sample_data: false
sample_fraction: 0.3

## Repo Map
├── config/
├── data/
│   ├── synthetic_fb_ads_undergarments.csv
├── logs/
├── reports/
│   ├── report.md
│   ├── insights.json
│   ├── creatives.json
│   ├── evaluation.json
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── analyst.py
│   │   ├── evaluator.py
│   ├── run.py
├── tests/
│   ├── test_evaluator.py

## Run
python src/run.py "Analyze ROAS drop"

## Outputs
The agent pipeline generates three files:
reports/insights.json
reports/creatives.json
reports/report.md

## Observability
A structured JSON trace is created at:
logs/pipeline_trace.json
Trace includes:
user query
loaded config
evaluation verdict
Framework easily extends to Langfuse / agent-level monitoring when needed.

## Release
Assignment submission build: v1.0
Repo link:
🔗 https://github.com/Killada-Neeraja/kasparro-agentic-fb-analyst-neeraja

## Self-Review
- Clear roadmap execution: Planner → Analyst → Evaluator
JSON outputs enable downstream integration
Threshold-based evaluation demonstrates practical QA thinking
Structure follows Kasparro-provided template
Future improvements:
Add LLM-driven creative generation
More evaluation rules
Langfuse observability
Unit tests for all agents (Planner & Analyst)

# Kasparro — Agentic Facebook Performance Analyst

A modular agentic system that analyzes Facebook Ads performance for an undergarments brand.  
It produces insights, creative recommendations, and a validation report — as required in the assignment.

---

## Quick Start

```bash
python -V  # should be >= 3.10
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/run.py "Analyze ROAS drop in last 7 days"
```



## Data
Dataset used: synthetic_fb_ads_undergarments.csv
Stored under data/
Contains campaign details including:
impressions, clicks, spend, revenue, ROAS, CTR, platform, creative_type, audience_type, country
Insights are generated directly from this dataset.

## Config
File: config/config.yaml
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
├── prompts/
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
Outputs saved to reports/.

## Outputs
reports/insights.json
reports/creatives.json
reports/report.md
reports/evaluation.json

## Observability
Execution trace stored at:
logs/pipeline_trace.json
Trace includes:
input query
config used
insights + evaluation decision

## Release
Assignment submission build: v1.0
Repo link:
🔗 https://github.com/Killada-Neeraja/kasparro-agentic-fb-analyst-neeraja

## Self-Review
-gents: Planner → Analyst → Evaluator
Validation structure: Basic threshold checks + confidence scoring
JSON-based outputs enable automation/integration
Structure closely follows assignment specification
Future recommended improvements:
Proper Creative Generation Agent with LLM prompts
Enhanced evaluator logic
Langfuse or similar tracing support
Additional agent unit tests
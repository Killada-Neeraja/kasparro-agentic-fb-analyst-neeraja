# Kasparro — Agentic Facebook Performance Analyst

## Quick Start
```bash
python -V  # ensure Python >= 3.10
pip install pandas
python src/run.py

## Data

## Config
python: "3.10"
random_seed: 42
confidence_min: 0.6
use_sample_data: true



## Repo Map
src/
 ├─ run.py                  → Runs the full pipeline
 └─ agents/
     ├─ planner.py         → Defines the task plan/steps
     ├─ analyst.py         → Loads CSV, generates insights & creatives
     ├─ evaluator.py       → Validates outputs & saves evaluation results

data/
 └─ synthetic_fb_ads_undergarments.csv  → Input dataset
reports/
 ├─ insights.json          → Best campaign/platform/country/creative type
 ├─ creatives.json         → Recommended messaging for ads
 └─ report.md              → Final human-readable summary
logs/                      → Placeholder for future logging
tests/                     → Placeholder for future tests
prompts/                   → Placeholder for LLM prompts

## Run
python src/run.py

## Outputs
The agent pipeline generates three files:
reports/insights.json
reports/creatives.json
reports/report.md

## Observability
This project does not currently include Langfuse or external monitoring.
However, the repository structure includes folders (`logs/`, `reports/`) to support
future observability improvements such as JSON logs or performance trace exports.


## Release
Version: v1.0 — Final Assignment Submission
Core features implemented
Automatic pipeline generation complete

## Self-Review

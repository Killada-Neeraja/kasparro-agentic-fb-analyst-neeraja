#!/usr/bin/env bash

# Create and activate virtual environment
python -m venv .venv

# Linux/Mac activate
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Windows activate fallback
if [ -f ".venv/Scripts/activate" ]; then
    .venv/Scripts/activate
fi

# Install requirements
pip install -r requirements.txt

# Run pipeline with example task
python src/run.py "Analyze ROAS drop in last 7 days"

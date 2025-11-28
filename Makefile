.PHONY: install run test

install:
	python -m venv .venv
	. .venv/Scripts/activate && pip install -r requirements.txt

run:
	. .venv/Scripts/activate && python src/run.py "Analyze ROAS drop in last 7 days"

test:
	. .venv/Scripts/activate && pytest
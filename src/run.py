import sys
import json
from pathlib import Path
import yaml

from agents.planner import PlannerAgent
from agents.data_agent import DataAgent
from agents.insight_agent import InsightAgent
from agents.evaluator import EvaluatorAgent
from agents.creative_generator import CreativeGenerator
from llm_client import LLMClient


BASE_DIR = Path(__file__).resolve().parent.parent


def load_config():
    config_path = BASE_DIR / "config" / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def main(query: str):
    config = load_config()

    llm = LLMClient()

    planner = PlannerAgent(llm_client=llm, prompts_dir=BASE_DIR / "prompts", config=config)
    data_agent = DataAgent(config=config)
    insight_agent = InsightAgent(llm_client=llm, prompts_dir=BASE_DIR / "prompts", config=config)
    evaluator = EvaluatorAgent(config=config)
    creative_agent = CreativeGenerator(llm_client=llm, prompts_dir=BASE_DIR / "prompts", config=config)

    # 1️⃣ Plan
    plan = planner.create_plan(query)

    # 2️⃣ Load + summarize
    df = data_agent.load_data()
    data_summary = data_agent.summarize(df)

    # 3️⃣ Generate insights
    insights = insight_agent.generate_insights(data_summary, plan)

    # 4️⃣ Evaluate
    evaluation = evaluator.evaluate(insights)

    # 5️⃣ Select underperformers for creative ideas
    threshold = config.get("roas_bad_threshold", 1.0)
    underperforming = [row for row in data_summary if row.get("ROAS", 999) < threshold]
    creatives = creative_agent.generate_creatives(underperforming, insights)

    # Save outputs
    reports = BASE_DIR / "reports"
    save_json(reports / "insights.json", insights)
    save_json(reports / "evaluation.json", evaluation)
    save_json(reports / "creatives.json", creatives)

    print("\n=== PIPELINE COMPLETE ===")
    print(f"Insights saved to: {reports / 'insights.json'}")
    print(f"Evaluation saved to: {reports / 'evaluation.json'}")
    print(f"Creatives saved to: {reports / 'creatives.json'}")


if __name__ == "__main__":
    user_query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Analyze ROAS drop in last 7 days"
    main(user_query)

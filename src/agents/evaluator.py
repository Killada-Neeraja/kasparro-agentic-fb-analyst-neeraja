from pathlib import Path
import json


class EvaluatorAgent:
    """
    Very simple evaluator that checks:
    - whether all key insights are present
    - whether at least one creative exists
    - whether there is at least one UGC creative
    Writes evaluation.json into reports/.
    """

    def __init__(self, reports_dir: str = "reports"):
        self.reports_dir = Path(reports_dir)
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def evaluate(self, insights: dict, creatives: list) -> dict:
        result = {}

        required_keys = [
            "best_campaign_by_roas",
            "best_platform_by_revenue",
            "best_country_by_cvr",
            "best_creative_type",
            "best_audience_type",
        ]
        missing = [k for k in required_keys if k not in insights]
        result["missing_insight_keys"] = missing

        result["num_creatives"] = len(creatives)
        result["has_ugc_creative"] = any(
            c.get("creative_type", "").lower() == "ugc"
            for c in creatives
        )

        if not missing and result["num_creatives"] > 0:
            result["status"] = "pass"
        else:
            result["status"] = "needs_improvement"

        out_path = self.reports_dir / "evaluation.json"
        with out_path.open("w") as f:
            json.dump(result, f, indent=4)

        return result

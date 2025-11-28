import math
from typing import Dict, Any, List


class EvaluatorAgent:
    """
    Evaluates the quality of insights produced by the InsightAgent.

    Inputs:
      insights_payload: dict with key "insights" -> list of insight dicts
    """

    def __init__(self, config: Dict[str, Any]):
        self.confidence_min = float(config.get("confidence_min", 0.6))
        self.min_insights = int(config.get("min_insights", 3))

    def evaluate(self, insights_payload: Dict[str, Any]) -> Dict[str, Any]:
        insights: List[Dict[str, Any]] = insights_payload.get("insights", []) or []

        issues = []

        # 1) Basic existence check
        if len(insights) == 0:
            issues.append("no_insights_generated")

        if len(insights) < self.min_insights:
            issues.append(f"too_few_insights(<{self.min_insights})")

        # 2) Schema & value checks
        for idx, ins in enumerate(insights):
            prefix = f"insight_{idx}"

            # required keys
            for key in ["id", "title", "description", "impact", "confidence"]:
                if key not in ins:
                    issues.append(f"{prefix}_missing_{key}")

            # impact domain
            impact = ins.get("impact")
            if impact not in ("high", "medium", "low"):
                issues.append(f"{prefix}_invalid_impact:{impact}")

            # confidence range
            try:
                conf = float(ins.get("confidence", 0.0))
                if math.isnan(conf) or conf < 0 or conf > 1:
                    issues.append(f"{prefix}_invalid_confidence:{conf}")
                elif conf < self.confidence_min:
                    issues.append(f"{prefix}_low_confidence:{conf}")
            except (TypeError, ValueError):
                issues.append(f"{prefix}_non_numeric_confidence")

        # 3) Final verdict
        status = "pass" if len(issues) == 0 else "fail"

        return {
            "status": status,
            "issues": issues,
            "insight_count": len(insights),
            "confidence_min": self.confidence_min,
        }

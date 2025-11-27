from typing import List, Dict


class CreativeGeneratorAgent:
    """
    Generates creative improvement suggestions, especially for underperforming (low CTR / low ROAS) segments.
    """

    def __init__(self):
        pass

    def generate(self, insights: Dict, roas_hypothesis: Dict) -> List[Dict]:
        creatives: List[Dict] = []

        best_creative_type = insights.get("best_creative_type", "UGC")
        best_country = insights.get("best_country_by_cvr", "UK")
        best_audience = insights.get("best_audience_type", "Retargeting")
        hypo_text = roas_hypothesis.get("hypothesis", "")
        confidence = roas_hypothesis.get("confidence", 0.0)

        creatives.append(
            {
                "platform": "Facebook",
                "audience_type": best_audience,
                "creative_type": best_creative_type,
                "hypothesis_context": hypo_text,
                "hypothesis_confidence": confidence,
                "recommendation": (
                    "Lean into the highest performing creative type and audience. "
                    "Adapt messaging to address ROAS decline causes (e.g., ad fatigue, rising CPC)."
                ),
                "example_copy": (
                    "UK men are sticking with comfort — refresh your UGC creatives with shorter hooks, "
                    "clearer value props, and stronger CTAs to fight rising CPC."
                ),
            }
        )

        creatives.append(
            {
                "platform": "Instagram",
                "audience_type": "Broad",
                "creative_type": "Video",
                "hypothesis_context": hypo_text,
                "hypothesis_confidence": confidence * 0.8,
                "recommendation": (
                    "Test broader reach creatives on Instagram with fast-moving visuals and brand recall focus."
                ),
                "example_copy": (
                    "Not just another undergarment brand. Show the switch moment: "
                    "before vs after wearing our premium modal collection."
                ),
            }
        )

        return creatives

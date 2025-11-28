import json
from typing import Any


class LLMClient:
    """
    Minimal stub LLM client for local runs.
    It returns simple but valid JSON for insights and creative ideas.
    """

    def generate(self, prompt: str) -> str:
        # If the prompt looks like it's for the Creative Agent, return "ideas"
        if "Creative Generator Agent" in prompt or '"ideas"' in prompt:
            return json.dumps(
                {
                    "ideas": [
                        {
                            "campaign_name": "Sample Campaign",
                            "ad_name": "Sample Ad",
                            "headline": "Feel confident all day long",
                            "primary_text": "Soft, breathable undergarments designed for all-day comfort.",
                            "cta": "Shop Now",
                            "angle": "comfort-first message",
                            "based_on_insight_ids": ["I1"],
                        }
                    ]
                }
            )

        # Default: return structured insights
        return json.dumps(
            {
                "insights": [
                    {
                        "id": "I1",
                            "title": "Core campaigns drive most revenue",
                            "description": "A small number of campaigns appear to drive the majority of revenue; these should be protected and scaled carefully.",
                            "impact": "high",
                            "confidence": 0.9,
                            "evidence": ["Core Campaign"],
                    },
                    {
                        "id": "I2",
                        "title": "Some campaigns have low ROAS",
                        "description": "Certain campaigns show lower ROAS and may need budget cuts or creative refresh.",
                        "impact": "high",
                        "confidence": 0.8,
                        "evidence": ["Example Low ROAS Campaign"],
                    },
                    {
                        "id": "I3",
                        "title": "Room to improve CTR on remarketing",
                        "description": "Remarketing or lower-funnel campaigns might benefit from stronger hooks or clearer offers.",
                        "impact": "medium",
                        "confidence": 0.75,
                        "evidence": ["Example Remarketing Campaign"],
                    },
                ]
            }
        )

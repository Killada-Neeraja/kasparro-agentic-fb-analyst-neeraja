import json

class InsightAgent:
    def __init__(self, llm_client, prompts_dir, config):
        self.llm_client = llm_client
        self.prompts_dir = prompts_dir
        self.config = config

    def generate_insights(self, data_summary, plan):
        prompt = self._load_prompt("insight_agent_prompt.md")

        formatted_input = json.dumps({
            "plan": plan,
            "data_summary": data_summary
        })

        full_prompt = f"{prompt}\n\nDATA:\n{formatted_input}"

        response = self.llm_client.generate(full_prompt)

        try:
            result = json.loads(response)
        except json.JSONDecodeError:
            result = {
                "insights": [],
                "error": "Invalid JSON from LLM"
            }

        return result

    def _load_prompt(self, filename):
        with open(f"{self.prompts_dir}/{filename}", "r", encoding="utf-8") as f:
            return f.read()

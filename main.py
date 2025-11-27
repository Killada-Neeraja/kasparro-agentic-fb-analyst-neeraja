import json
from agents.planner import PlannerAgent
from agents.analyst import AnalystAgent

class RunnerAgent:
    def __init__(self):
        self.planner = PlannerAgent()
        self.analyst = AnalystAgent()

    def run(self):
        plan = self.planner.plan()
        print("Plan:", plan)

        for step in plan['steps']:
            print(f"Executing: {step}")
            result = self.analyst.analyze(plan)
            print("Step Result:", result)

        with open('logs/run_log.json', 'w') as f:
            json.dump({"status": "Run Completed", "plan": plan}, f, indent=4)

        print("Pipeline completed! Logs saved to logs/run_log.json")

if __name__ == "__main__":
    runner = RunnerAgent()
    runner.run()

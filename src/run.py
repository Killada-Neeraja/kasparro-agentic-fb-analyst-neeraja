from agents.analyst import AnalystAgent


def main():
    analyst = AnalystAgent()
    result = analyst.run()
    print("Insights:")
    print(result["insights"])
    print("\nCreatives:")
    print(result["creatives"])


if __name__ == "__main__":
    main()

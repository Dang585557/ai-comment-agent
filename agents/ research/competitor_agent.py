from datetime import datetime


class CompetitorAgent:

    def analyze(self, keyword: str):

        competitors = [
            {
                "name": "Competitor A",
                "followers": 120000,
                "engagement": "8.5%"
            },
            {
                "name": "Competitor B",
                "followers": 95000,
                "engagement": "7.2%"
            },
            {
                "name": "Competitor C",
                "followers": 76000,
                "engagement": "6.8%"
            }
        ]

        return {
            "keyword": keyword,
            "competitors": competitors,
            "analyzed_at": datetime.now().isoformat()
        }

    def summary(self, report: dict):

        return {
            "keyword": report["keyword"],
            "total_competitors": len(report["competitors"]),
            "generated_at": datetime.now().isoformat()
        }


if __name__ == "__main__":

    agent = CompetitorAgent()

    result = agent.analyze("AI Technology")

    print(result)

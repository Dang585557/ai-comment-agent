from datetime import datetime

class TrendAgent:

    def search(self, keyword: str):

        return {
            "keyword": keyword,
            "trends": [
                f"{keyword}",
                f"{keyword} 2026",
                f"Best {keyword}",
                f"{keyword} Tips",
                f"{keyword} Review",
                "Trending",
                "Viral"
            ],
            "generated_at": datetime.now().isoformat()
        }

    def score(self, trends: list):

        result = []

        score = 100

        for trend in trends:

            result.append({
                "keyword": trend,
                "score": score
            })

            score -= 5

        return result

    def report(self, keyword: str):

        trends = self.search(keyword)

        return {
            "keyword": keyword,
            "results": self.score(
                trends["trends"]
            ),
            "created_at": datetime.now().isoformat()
        }


if __name__ == "__main__":

    agent = TrendAgent()

    print(
        agent.report(
            "Artificial Intelligence"
        )
    )

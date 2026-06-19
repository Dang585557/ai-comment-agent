from datetime import datetime


class AnalyticsAgent:

    def evaluate(self, content: dict):

        score = 85

        return {
            "score": score,
            "estimated_views": 10000,
            "estimated_likes": 1200,
            "estimated_comments": 150,
            "estimated_shares": 80,
            "engagement_rate": "14.3%",
            "recommendation": self.recommend(score),
            "analyzed_at": datetime.now().isoformat()
        }

    def recommend(self, score: int):

        if score >= 90:
            return "Ready to publish"

        if score >= 75:
            return "Improve title and hashtags"

        return "Rewrite script"

    def summary(self, analysis: dict):

        return (
            f"Score: {analysis['score']} | "
            f"Views: {analysis['estimated_views']} | "
            f"Likes: {analysis['estimated_likes']}"
        )


if __name__ == "__main__":

    agent = AnalyticsAgent()

    result = agent.evaluate(
        {
            "title": "AI Technology"
        }
    )

    print(result)

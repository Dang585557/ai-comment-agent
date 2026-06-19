from datetime import datetime
import json


class ReportAgent:

    def generate(self, topic: str, analysis: dict):

        return {
            "topic": topic,
            "status": "COMPLETED",
            "analysis": analysis,
            "generated_at": datetime.now().isoformat()
        }

    def save(self, report: dict, filename: str):

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                report,
                f,
                indent=4,
                ensure_ascii=False
            )

        return filename

    def summary(self, report: dict):

        analysis = report["analysis"]

        return (
            f"Topic: {report['topic']}\n"
            f"Score: {analysis['score']}\n"
            f"Estimated Views: {analysis['estimated_views']}\n"
            f"Estimated Likes: {analysis['estimated_likes']}\n"
            f"Recommendation: {analysis['recommendation']}"
        )


if __name__ == "__main__":

    agent = ReportAgent()

    report = agent.generate(
        "AI Technology",
        {
            "score": 90,
            "estimated_views": 15000,
            "estimated_likes": 1800,
            "recommendation": "Ready to publish"
        }
    )

    print(agent.summary(report))

from datetime import datetime
from pathlib import Path
import json


class ReportAgent:

    def generate(
        self,
        topic: str,
        competitors: dict,
        trends: dict,
        keywords: dict
    ):

        return {
            "topic": topic,
            "competitors": competitors,
            "trends": trends,
            "keywords": keywords,
            "generated_at": datetime.now().isoformat(),
            "status": "COMPLETED"
        }

    def save(
        self,
        report: dict,
        filename: str
    ):

        path = Path(filename)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
                ensure_ascii=False
            )

        return {
            "file": str(path),
            "status": "SAVED"
        }

    def summary(self, report: dict):

        return {
            "topic": report["topic"],
            "competitors": len(
                report["competitors"]["competitors"]
            ),
            "trends": len(
                report["trends"]["results"]
            ),
            "keywords": report["keywords"]["count"],
            "generated_at": report["generated_at"]
        }


if __name__ == "__main__":

    agent = ReportAgent()

    report = agent.generate(
        topic="Artificial Intelligence",
        competitors={
            "competitors": [
                {"name": "A"},
                {"name": "B"}
            ]
        },
        trends={
            "results": [
                {"keyword": "AI"}
            ]
        },
        keywords={
            "count": 10
        }
    )

    print(agent.summary(report))

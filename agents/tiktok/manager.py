from .content_agent import ContentAgent
from .script_agent import ScriptAgent
from .trend_agent import TrendAgent
from .analytics_agent import AnalyticsAgent
from .report_agent import ReportAgent


class TikTokManager:

    def __init__(self):
        self.content = ContentAgent()
        self.script = ScriptAgent()
        self.trend = TrendAgent()
        self.analytics = AnalyticsAgent()
        self.report = ReportAgent()

    def create_content(self, topic: str):

        trends = self.trend.search(topic)

        script = self.script.generate(
            topic=topic,
            trends=trends
        )

        content = self.content.create(script)

        analysis = self.analytics.evaluate(content)

        report = self.report.generate(
            topic=topic,
            analysis=analysis
        )

        return {
            "topic": topic,
            "trends": trends,
            "script": script,
            "content": content,
            "analysis": analysis,
            "report": report,
            "status": "COMPLETED"
        }


if __name__ == "__main__":

    manager = TikTokManager()

    result = manager.create_content(
        "AI Technology"
    )

    print(result)

from datetime import datetime

class TrendAgent:

    def search(self, topic: str):

        return [
            f"{topic}",
            f"{topic} 2026",
            f"{topic} Tips",
            f"{topic} Tutorial",
            "Trending",
            "For You",
            "Viral"
        ]

    def score(self, keywords):

        return {
            keyword: 90 - index * 5
            for index, keyword in enumerate(keywords)
        }

    def report(self, topic: str):

        keywords = self.search(topic)

        return {
            "topic": topic,
            "keywords": keywords,
            "scores": self.score(keywords),
            "generated_at": datetime.now().isoformat()
        }


if __name__ == "__main__":

    agent = TrendAgent()

    print(agent.report("AI Technology"))

from datetime import datetime


class KeywordAgent:

    def generate(self, topic: str):

        keywords = [
            topic,
            f"{topic} ไทย",
            f"{topic} 2026",
            f"{topic} รีวิว",
            f"{topic} วิธีใช้",
            f"{topic} ราคา",
            f"Best {topic}",
            f"{topic} Tutorial",
            f"{topic} AI",
            f"{topic} TikTok"
        ]

        return {
            "topic": topic,
            "keywords": keywords,
            "count": len(keywords),
            "generated_at": datetime.now().isoformat()
        }

    def filter(self, keywords: list):

        unique = sorted(set(keywords))

        return {
            "keywords": unique,
            "count": len(unique)
        }

    def top(self, keywords: list, limit: int = 5):

        return keywords[:limit]


if __name__ == "__main__":

    agent = KeywordAgent()

    result = agent.generate(
        "Artificial Intelligence"
    )

    print(result)

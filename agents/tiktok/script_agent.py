from datetime import datetime
class ScriptAgent:
    def generate(self, topic: str, trends=None):

        trends = trends or []

        intro = f"วันนี้เราจะพูดเกี่ยวกับ {topic}"

        body = (
            f"{topic} กำลังได้รับความสนใจ "
            "และมีแนวโน้มเติบโตอย่างต่อเนื่อง "
            "มาดูประเด็นสำคัญกัน"
        )

        ending = (
            "ถ้าชอบเนื้อหานี้ "
            "กดติดตามเพื่อไม่พลาดคลิปใหม่"
        )

        return "\n\n".join([
            intro,
            body,
            f"เทรนด์ที่เกี่ยวข้อง: {', '.join(trends)}",
            ending
        ])

    def shorten(self, script: str, max_length: int = 300):

        if len(script) <= max_length:
            return script

        return script[:max_length] + "..."

    def estimate_duration(self, script: str):

        words = len(script.split())

        seconds = max(10, int(words / 2.5))

        return {
            "seconds": seconds,
            "created_at": datetime.now().isoformat()
        }


if __name__ == "__main__":

    agent = ScriptAgent()

    script = agent.generate(
        topic="AI Technology",
        trends=["AI", "Automation", "Business"]
    )

    print(script)

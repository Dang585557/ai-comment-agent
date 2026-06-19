from datetime import datetime
from pathlib import Path


class ThumbnailAgent:

    def generate(
        self,
        title: str,
        style: str = "modern"
    ):

        return {
            "title": title,
            "style": style,
            "width": 1080,
            "height": 1920,
            "status": "GENERATED",
            "created_at": datetime.now().isoformat()
        }

    def save(self, output_path: str):

        return {
            "file": str(Path(output_path)),
            "status": "SAVED"
        }

    def recommend_text(self, topic: str):

        return [
            f"{topic}",
            "ห้ามพลาด!",
            "รู้ไว้ก่อน!",
            "มาแรง 2026",
            "AI แนะนำ"
        ]

    def templates(self):

        return [
            "modern",
            "minimal",
            "gaming",
            "business",
            "technology"
        ]


if __name__ == "__main__":

    agent = ThumbnailAgent()

    print(
        agent.generate(
            title="AI Technology"
        )
    )

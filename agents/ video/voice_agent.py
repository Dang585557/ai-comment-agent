from datetime import datetime
from pathlib import Path


class VoiceAgent:

    def generate(
        self,
        text: str,
        voice: str = "default",
        language: str = "th"
    ):

        return {
            "text": text,
            "voice": voice,
            "language": language,
            "status": "GENERATED",
            "generated_at": datetime.now().isoformat()
        }

    def save(self, output_path: str):

        path = Path(output_path)

        return {
            "file": str(path),
            "status": "SAVED"
        }

    def estimate_duration(self, text: str):

        words = len(text.split())

        seconds = max(3, int(words / 2.5))

        return {
            "seconds": seconds
        }

    def supported_languages(self):

        return [
            "th",
            "en",
            "zh",
            "ja"
        ]


if __name__ == "__main__":

    agent = VoiceAgent()

    result = agent.generate(
        text="สวัสดีครับ ยินดีต้อนรับสู่ AI-COMPANY",
        voice="female"
    )

    print(result)

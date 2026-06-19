from datetime import datetime

class SubtitleAgent:

    def generate(self, script: str):

        lines = script.split("\n")

        subtitles = []

        current_time = 0

        for line in lines:

            if not line.strip():
                continue

            subtitles.append({
                "start": current_time,
                "end": current_time + 3,
                "text": line.strip()
            })

            current_time += 3

        return {
            "subtitles": subtitles,
            "count": len(subtitles),
            "generated_at": datetime.now().isoformat()
        }

    def export_srt(self, subtitles: list):

        output = []

        for index, subtitle in enumerate(subtitles, start=1):

            output.append(str(index))
            output.append(
                f"00:00:{subtitle['start']:02d},000 --> 00:00:{subtitle['end']:02d},000"
            )
            output.append(subtitle["text"])
            output.append("")

        return "\n".join(output)


if __name__ == "__main__":

    agent = SubtitleAgent()

    result = agent.generate(
        "Hello World\nWelcome to AI Company"
    )

    print(
        agent.export_srt(
            result["subtitles"]
        )
    )

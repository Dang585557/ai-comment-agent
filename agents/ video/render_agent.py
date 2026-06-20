from datetime import datetime
from pathlib import Path


class RenderAgent:

    def render(
        self,
        project_name: str,
        output_file: str,
        resolution: str = "1080x1920",
        fps: int = 30
    ):

        return {
            "project": project_name,
            "output": output_file,
            "resolution": resolution,
            "fps": fps,
            "status": "RENDERING",
            "started_at": datetime.now().isoformat()
        }

    def complete(self, output_file: str):

        return {
            "file": str(Path(output_file)),
            "status": "COMPLETED",
            "finished_at": datetime.now().isoformat()
        }

    def estimate_time(
        self,
        duration_seconds: int
    ):

        minutes = max(1, duration_seconds // 30)

        return {
            "estimated_minutes": minutes
        }

    def supported_formats(self):

        return [
            "mp4",
            "mov",
            "avi",
            "mkv",
            "webm"
        ]


if __name__ == "__main__":

    agent = RenderAgent()

    job = agent.render(
        project_name="TikTok AI",
        output_file="storage/videos/output.mp4"
    )

    print(job)

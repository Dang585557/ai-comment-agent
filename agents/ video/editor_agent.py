from datetime import datetime
from pathlib import Path


class EditorAgent:

    def create_project(self, name: str):

        return {
            "project": name,
            "created_at": datetime.now().isoformat(),
            "status": "CREATED"
        }

    def import_assets(self, files: list):

        return {
            "assets": files,
            "count": len(files),
            "status": "IMPORTED"
        }

    def build_timeline(self, assets: list):

        return {
            "timeline": assets,
            "tracks": len(assets),
            "status": "READY"
        }

    def export(self, output_path: str):

        return {
            "output": str(Path(output_path)),
            "status": "EXPORTED",
            "time": datetime.now().isoformat()
        }


if __name__ == "__main__":

    agent = EditorAgent()

    project = agent.create_project("TikTok AI")

    print(project)

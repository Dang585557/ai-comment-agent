from datetime import datetime
from pathlib import Path


class DeployAgent:

    def deploy(
        self,
        project_name: str,
        target: str = "production"
    ):

        return {
            "project": project_name,
            "target": target,
            "status": "DEPLOYING",
            "started_at": datetime.now().isoformat()
        }

    def complete(
        self,
        url: str
    ):

        return {
            "url": url,
            "status": "SUCCESS",
            "finished_at": datetime.now().isoformat()
        }

    def rollback(
        self,
        version: str
    ):

        return {
            "version": version,
            "status": "ROLLED_BACK",
            "time": datetime.now().isoformat()
        }

    def deployment_report(
        self,
        project: str,
        url: str
    ):

        return {
            "project": project,
            "url": url,
            "result": "SUCCESS",
            "generated_at": datetime.now().isoformat()
        }


if __name__ == "__main__":

    agent = DeployAgent()

    job = agent.deploy(
        project_name="AI-COMPANY"
    )

    print(job)

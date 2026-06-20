from datetime import datetime
from pathlib import Path


class DocumentationAgent:

    def generate(
        self,
        project_name: str,
        description: str,
        modules: list
    ):

        return {
            "project": project_name,
            "description": description,
            "modules": modules,
            "generated_at": datetime.now().isoformat()
        }

    def markdown(self, document: dict):

        lines = [
            f"# {document['project']}",
            "",
            document["description"],
            "",
            "## Modules",
            ""
        ]

        for module in document["modules"]:
            lines.append(f"- {module}")

        lines.extend([
            "",
            f"Generated: {document['generated_at']}"
        ])

        return "\n".join(lines)

    def save(
        self,
        filename: str,
        content: str
    ):

        path = Path(filename)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            content,
            encoding="utf-8"
        )

        return {
            "file": str(path),
            "status": "SAVED"
        }


if __name__ == "__main__":

    agent = DocumentationAgent()

    doc = agent.generate(
        project_name="AI-COMPANY",
        description="Multi-Agent AI Automation Platform",
        modules=[
            "CEO",
            "Manager",
            "Dashboard",
            "LLM",
            "Monitoring"
        ]
    )

    markdown = agent.markdown(doc)

    print(markdown)

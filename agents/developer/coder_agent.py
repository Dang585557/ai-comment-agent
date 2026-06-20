from datetime import datetime
from pathlib import Path


class CoderAgent:

    def generate_code(
        self,
        filename: str,
        code: str
    ):

        return {
            "filename": filename,
            "lines": len(code.splitlines()),
            "status": "GENERATED",
            "created_at": datetime.now().isoformat()
        }

    def save(
        self,
        filename: str,
        code: str
    ):

        path = Path(filename)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            code,
            encoding="utf-8"
        )

        return {
            "file": str(path),
            "status": "SAVED"
        }

    def append(
        self,
        filename: str,
        code: str
    ):

        path = Path(filename)

        with open(
            path,
            "a",
            encoding="utf-8"
        ) as file:
            file.write(code)

        return {
            "file": str(path),
            "status": "UPDATED"
        }

    def statistics(self, code: str):

        return {
            "characters": len(code),
            "lines": len(code.splitlines()),
            "generated_at": datetime.now().isoformat()
        }


if __name__ == "__main__":

    agent = CoderAgent()

    print(
        agent.generate_code(
            "main.py",
            "print('Hello AI-COMPANY')"
        )
    )

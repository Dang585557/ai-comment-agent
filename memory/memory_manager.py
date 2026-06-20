from datetime import datetime
from pathlib import Path
import json


class MemoryManager:

    def __init__(self):

        self.base_path = Path("memory")

        self.short_term = self.base_path / "short_term"

        self.long_term = self.base_path / "long_term"

        self.logs = self.base_path / "conversation_logs"

        for directory in [
            self.short_term,
            self.long_term,
            self.logs
        ]:
            directory.mkdir(
                parents=True,
                exist_ok=True
            )

    def save_short_term(
        self,
        key: str,
        data: dict
    ):

        file = self.short_term / f"{key}.json"

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        return str(file)

    def save_long_term(
        self,
        key: str,
        data: dict
    ):

        file = self.long_term / f"{key}.json"

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        return str(file)

    def load(self, file_path: str):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def conversation_log(
        self,
        user: str,
        assistant: str
    ):

        filename = datetime.now().strftime(
            "%Y%m%d"
        ) + ".jsonl"

        file = self.logs / filename

        record = {
            "time": datetime.now().isoformat(),
            "user": user,
            "assistant": assistant
        }

        with open(
            file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(
                    record,
                    ensure_ascii=False
                )
                + "\n"
            )

    def list_memory(self):

        return {
            "short_term": len(
                list(self.short_term.glob("*.json"))
            ),
            "long_term": len(
                list(self.long_term.glob("*.json"))
            )
        }


if __name__ == "__main__":

    memory = MemoryManager()

    memory.save_short_term(
        "demo",
        {
            "task": "Create TikTok video"
        }
    )

    print(
        memory.list_memory()
    )

import json
from datetime import datetime
from pathlib import Path
from typing import Any


class MemoryManager:

    def __init__(self, base_path: str = "memory"):

        self.base_path = Path(base_path)

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

    def write(
        self,
        bucket: str,
        key: str,
        data: dict[str, Any]
    ):

        if bucket == "short_term":
            return self.save_short_term(key, data)

        if bucket == "long_term":
            return self.save_long_term(key, data)

        raise ValueError(f"Unknown memory bucket: {bucket}")

    def read(
        self,
        bucket: str,
        key: str
    ):

        directory = self._bucket_path(bucket)

        file = directory / f"{key}.json"

        if not file.exists():
            return None

        return self.load(str(file))

    def search(
        self,
        query: str,
        bucket: str | None = None,
        limit: int = 10
    ):

        terms = {
            term.lower()
            for term in query.split()
            if term.strip()
        }

        directories = [
            self._bucket_path(bucket)
        ] if bucket else [
            self.short_term,
            self.long_term
        ]

        results = []

        for directory in directories:

            for file in directory.glob("*.json"):

                try:

                    data = self.load(str(file))

                except json.JSONDecodeError:

                    continue

                text = json.dumps(
                    data,
                    ensure_ascii=False
                ).lower()

                score = sum(
                    1
                    for term in terms
                    if term in text
                )

                if score or not terms:

                    results.append({
                        "key": file.stem,
                        "bucket": directory.name,
                        "score": score,
                        "data": data
                    })

        return sorted(
            results,
            key=lambda item: item["score"],
            reverse=True
        )[:limit]

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
            ),
            "conversation_logs": len(
                list(self.logs.glob("*.jsonl"))
            )
        }

    def _bucket_path(
        self,
        bucket: str
    ):

        if bucket == "short_term":

            return self.short_term

        if bucket == "long_term":

            return self.long_term

        raise ValueError(f"Unknown memory bucket: {bucket}")


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

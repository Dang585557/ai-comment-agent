from pathlib import Path
from datetime import datetime
import json


class LongTermMemory:

    def __init__(
        self,
        storage_path: str = "memory/long_term"
    ):

        self.storage = Path(storage_path)

        self.storage.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(
        self,
        key: str,
        data: dict
    ):

        file = self.storage / f"{key}.json"

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {
                    "created_at": datetime.now().isoformat(),
                    "data": data
                },
                f,
                indent=4,
                ensure_ascii=False
            )

        return str(file)

    def load(
        self,
        key: str
    ):

        file = self.storage / f"{key}.json"

        if not file.exists():
            return None

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def delete(
        self,
        key: str
    ):

        file = self.storage / f"{key}.json"

        if file.exists():
            file.unlink()

    def list_all(self):

        return [
            file.stem
            for file in self.storage.glob("*.json")
        ]

    def count(self):

        return len(
            list(
                self.storage.glob("*.json")
            )
        )


if __name__ == "__main__":

    memory = LongTermMemory()

    memory.save(
        "user_profile",
        {
            "name": "AI-COMPANY",
            "version": "1.0"
        }
    )

    print(
        memory.list_all()
    )

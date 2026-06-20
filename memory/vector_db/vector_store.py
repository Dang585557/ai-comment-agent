from pathlib import Path
from datetime import datetime
import json


class VectorStore:

    def __init__(
        self,
        storage_path: str = "memory/vector_db"
    ):

        self.storage = Path(storage_path)

        self.storage.mkdir(
            parents=True,
            exist_ok=True
        )

    def add(
        self,
        document_id: str,
        embedding: list,
        metadata: dict | None = None
    ):

        file = self.storage / f"{document_id}.json"

        record = {
            "id": document_id,
            "embedding": embedding,
            "metadata": metadata or {},
            "created_at": datetime.now().isoformat()
        }

        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                record,
                f,
                indent=4,
                ensure_ascii=False
            )

        return str(file)

    def get(
        self,
        document_id: str
    ):

        file = self.storage / f"{document_id}.json"

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
        document_id: str
    ):

        file = self.storage / f"{document_id}.json"

        if file.exists():
            file.unlink()

    def list_documents(self):

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

    store = VectorStore()

    store.add(
        document_id="doc001",
        embedding=[0.12, 0.87, 0.34, 0.91],
        metadata={
            "title": "AI Company"
        }
    )

    print(
        store.list_documents()
    )

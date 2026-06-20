from datetime import datetime
import hashlib


class EmbeddingManager:

    def __init__(self):

        self.provider = "default"

    def set_provider(
        self,
        provider: str
    ):

        self.provider = provider

    def generate(
        self,
        text: str
    ):

        digest = hashlib.sha256(
            text.encode("utf-8")
        ).digest()

        embedding = [
            round(byte / 255.0, 6)
            for byte in digest
        ]

        return {
            "provider": self.provider,
            "dimensions": len(embedding),
            "embedding": embedding,
            "created_at": datetime.now().isoformat()
        }

    def similarity(
        self,
        embedding_a: list,
        embedding_b: list
    ):

        length = min(
            len(embedding_a),
            len(embedding_b)
        )

        if length == 0:
            return 0.0

        score = sum(
            1 - abs(
                embedding_a[i] - embedding_b[i]
            )
            for i in range(length)
        )

        return round(
            score / length,
            4
        )


if __name__ == "__main__":

    manager = EmbeddingManager()

    first = manager.generate(
        "Artificial Intelligence"
    )

    second = manager.generate(
        "AI Company"
    )

    print(
        manager.similarity(
            first["embedding"],
            second["embedding"]
        )
    )

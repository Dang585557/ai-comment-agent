from datetime import datetime
class ShortTermMemory:
    def __init__(self):

        self.memory = {}

    def set(
        self,
        key: str,
        value
    ):

        self.memory[key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }

    def get(
        self,
        key: str
    ):

        item = self.memory.get(key)

        if item is None:
            return None

        return item["value"]

    def remove(
        self,
        key: str
    ):

        if key in self.memory:
            del self.memory[key]

    def clear(self):

        self.memory.clear()

    def keys(self):

        return list(
            self.memory.keys()
        )

    def size(self):

        return len(
            self.memory
        )


if __name__ == "__main__":

    memory = ShortTermMemory()

    memory.set(
        "current_task",
        "Create TikTok Video"
    )

    print(
        memory.get(
            "current_task"
        )
    )

    print(
        memory.size()
    )

from datetime import datetime


class ContentAgent:

    def create(self, script: str):

        return {
            "title": script[:60],
            "description": script,
            "hashtags": [
                "#AI",
                "#TikTok",
                "#Automation",
                "#Technology"
            ],
            "created_at": datetime.now().isoformat(),
            "status": "READY"
        }

    def optimize(self, content: dict):

        content["optimized"] = True
        content["updated_at"] = datetime.now().isoformat()

        return content

    def publish_data(self, content: dict):

        return {
            "platform": "TikTok",
            "content": content,
            "status": "WAITING_FOR_PUBLISH"
        }


if __name__ == "__main__":

    agent = ContentAgent()

    print(
        agent.create(
            "Example TikTok script."
        )
    )

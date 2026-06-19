import os
import requests


class LocalModelClient:

    def __init__(self):

        self.base_url = os.getenv(
            "LOCAL_MODEL_URL",
            "http://localhost:11434"
        )

        self.model = os.getenv(
            "LOCAL_MODEL_NAME",
            "llama3.1"
        )

    def generate(

        self,

        prompt: str,

        temperature: float = 0.7,

    ):

        response = requests.post(

            f"{self.base_url}/api/generate",

            json={

                "model": self.model,

                "prompt": prompt,

                "temperature": temperature,

                "stream": False

            },

            timeout=300

        )

        response.raise_for_status()

        return response.json()["response"]

    def chat(self, messages):

        response = requests.post(

            f"{self.base_url}/api/chat",

            json={

                "model": self.model,

                "messages": messages,

                "stream": False

            },

            timeout=300

        )

        response.raise_for_status()

        return response.json()["message"]["content"]

    def health(self):

        try:

            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5
            )

            online = response.status_code == 200

        except Exception:

            online = False

        return {

            "provider": "Local Model",

            "model": self.model,

            "url": self.base_url,

            "status": "ONLINE" if online else "OFFLINE"

        }


if __name__ == "__main__":

    model = LocalModelClient()

    print(model.health())

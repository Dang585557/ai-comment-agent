import os
from openai import OpenAI


class OpenAIClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.model = os.getenv(
            "OPENAI_MODEL",
            "gpt-5"
        )

    def generate(

        self,

        prompt: str,

        system: str = "You are a helpful AI assistant.",

        temperature: float = 0.7,

        max_tokens: int = 2048,

    ):

        response = self.client.responses.create(

            model=self.model,

            input=[

                {
                    "role": "system",
                    "content": system
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=temperature,
            max_output_tokens=max_tokens

        )

        return response.output_text

    def chat(self, messages):

        response = self.client.responses.create(

            model=self.model,

            input=messages

        )

        return response.output_text

    def health(self):

        return {

            "provider": "OpenAI",

            "model": self.model,

            "status": "ONLINE"

        }


if __name__ == "__main__":

    ai = OpenAIClient()

    print(ai.health())

import os
import anthropic


class ClaudeClient:

    def __init__(self):

        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

        self.model = os.getenv(
            "CLAUDE_MODEL",
            "claude-sonnet-4"
        )

    def generate(

        self,

        prompt: str,

        system: str = "You are a helpful AI assistant.",

        temperature: float = 0.7,

        max_tokens: int = 2048,

    ):

        response = self.client.messages.create(

            model=self.model,

            max_tokens=max_tokens,

            temperature=temperature,

            system=system,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return response.content[0].text

    def chat(self, messages):

        response = self.client.messages.create(

            model=self.model,

            max_tokens=2048,

            messages=messages

        )

        return response.content[0].text

    def health(self):

        return {

            "provider": "Claude",

            "model": self.model,

            "status": "ONLINE"

        }


if __name__ == "__main__":

    ai = ClaudeClient()

    print(ai.health())

from llm.openai_client import OpenAIClient
from llm.gemini_client import GeminiClient
from llm.claude_client import ClaudeClient
from llm.local_model_client import LocalModelClient


class LLMRouter:

    def __init__(self):

        self.models = {

            "openai": OpenAIClient(),

            "gemini": GeminiClient(),

            "claude": ClaudeClient(),

            "local": LocalModelClient(),

        }

    def generate(
        self,
        prompt: str,
        provider: str = "openai",
        **kwargs
    ):

        if provider not in self.models:

            raise ValueError(
                f"Unknown provider: {provider}"
            )

        return self.models[provider].generate(
            prompt=prompt,
            **kwargs
        )

    def available_models(self):

        return list(self.models.keys())

    def add_model(self, name, client):

        self.models[name] = client

    def remove_model(self, name):

        if name in self.models:

            del self.models[name]


if __name__ == "__main__":

    router = LLMRouter()

    print(router.available_models())

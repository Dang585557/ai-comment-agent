import os
import google.generativeai as genai


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        genai.configure(api_key=api_key)

        self.model_name = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-pro"
        )

        self.model = genai.GenerativeModel(
            self.model_name
        )

    def generate(

        self,

        prompt: str,

        temperature: float = 0.7,

    ):

        response = self.model.generate_content(

            prompt,

            generation_config=genai.GenerationConfig(
                temperature=temperature
            )

        )

        return response.text

    def chat(self, history, message):

        chat = self.model.start_chat(
            history=history
        )

        response = chat.send_message(message)

        return response.text

    def health(self):

        return {

            "provider": "Gemini",

            "model": self.model_name,

            "status": "ONLINE"

        }


if __name__ == "__main__":

    ai = GeminiClient()

    print(ai.health())

import openai
import yaml
from config import config

class AICodeGenerator:
    def __init__(self):
        self.model = config.get("aws.ai_service.nlp_model", "Amazon Bedrock")

    def generate_code(self, prompt: str) -> str:
        """
        Uses AI to generate Python code based on a natural language prompt.
        """
        if "sum of two numbers" in prompt.lower():
            return "def add(a, b):\n    return a + b"

        # Example: Calling GPT API (to be replaced with AWS model)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    ai = AICodeGenerator()
    prompt = input("Describe what you want to build: ")
    print("\nGenerated Code:\n")
    print(ai.generate_code(prompt))

from openai import OpenAI

from app.config.settings import settings


class LLMService:
    """
    Handles AI interactions using OpenRouter.

    Features:
    - Uses OpenRouter if an API key is available.
    - Automatically tries multiple models.
    - Falls back to a mock AI summary if:
        • No API key is configured.
        • All models fail.
    """

    def __init__(self):

        self.client = None

        if settings.OPENROUTER_API_KEY:

            self.client = OpenAI(
                api_key=settings.OPENROUTER_API_KEY.strip(),
                base_url="https://openrouter.ai/api/v1",
            )

        self.models = [

            "deepseek/deepseek-chat-v3-0324:free",

            "meta-llama/llama-3.3-70b-instruct:free",

            "google/gemma-3-27b-it:free",

            "openai/gpt-oss-120b:free"

        ]

    # ==================================================
    # Generate AI Summary
    # ==================================================

    def generate(self, prompt):

        # ----------------------------------------------
        # No API Key
        # ----------------------------------------------

        if self.client is None:

            print("No OpenRouter API key found. Using mock summary.")

            return self.mock_summary()

        last_error = None

        # ----------------------------------------------
        # Try Available Models
        # ----------------------------------------------

        for model in self.models:

            try:

                print(f"Trying model: {model}")

                response = self.client.chat.completions.create(

                    model=model,

                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],

                    temperature=0.3,

                    max_tokens=300,

                )

                print(f"Using model: {model}")

                return response.choices[0].message.content

            except Exception as e:

                print(f"{model} failed")

                print(e)

                last_error = e

                continue

        # ----------------------------------------------
        # Every Model Failed
        # ----------------------------------------------

        print("All models failed. Using mock summary.")

        return self.mock_summary()

    # ==================================================
    # Mock Summary
    # ==================================================

    def mock_summary(self):

        return """
Prospect Research Summary

The alumnus appears to be an experienced professional with a strong
career background in their respective industry.

Based on the available profile information, this individual may be a
valuable contact for:

• Alumni networking
• Mentorship opportunities
• Industry collaboration
• Guest lectures
• Career guidance
• Fundraising initiatives

This summary was generated using the project's built-in fallback mode.
Configure an OpenRouter API key to enable live AI-generated summaries.
"""
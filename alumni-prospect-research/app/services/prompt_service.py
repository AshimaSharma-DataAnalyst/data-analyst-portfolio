from pathlib import Path


class PromptService:

    def __init__(self):

        self.prompt_directory = Path("app/prompts")

    def load_prompt(self, filename):

        file_path = self.prompt_directory / filename

        with open(

            file_path,

            "r",

            encoding="utf-8"

        ) as file:

            return file.read()

    def build_prompt(self, profile):

        template = self.load_prompt(

            "prospect_prompt.txt"

        )

        return template.format(

            name=profile.get("name", ""),

            company=profile.get("company", ""),

            designation=profile.get("designation", ""),

            education=profile.get("education", ""),

            city=profile.get("city", "")

        )

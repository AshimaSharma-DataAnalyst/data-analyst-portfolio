import re


class AlumniExtractor:

    def extract_name(self, data):

        return data.get("heading", "")


    def extract_company(self, data):

        info = data.get("infobox", {})

        title = info.get("Title", "")

        occupation = info.get("Occupation", "")

        text = f"{title} {occupation}".lower()

        mapping = {

            "microsoft": "Microsoft",

            "google": "Google",

            "amazon": "Amazon",

            "meta": "Meta",

            "apple": "Apple",

            "openai": "OpenAI"

        }

        for key, value in mapping.items():

            if key in text:

                return value

        return "Unknown"


    def extract_designation(self, data):

        info = data.get("infobox", {})

        title = info.get("Title", "")

        if title:

            return title

        return info.get("Occupation", "Unknown")


    def extract_education(self, data):

        info = data.get("infobox", {})

        return info.get("Alma mater", "")


    def extract_city(self, data):

        info = data.get("infobox", {})

        born = info.get("Born", "")

        match = re.search(r"([A-Za-z ]+),\s*India", born)

        if match:

            return match.group(1).strip()

        return ""


    def extract_summary(self, data):

        paragraphs = data.get("paragraphs", [])

        if paragraphs:

            return paragraphs[0]

        return ""


    def extract_profile(self, data):

        return {

            "name": self.extract_name(data),

            "company": self.extract_company(data),

            "designation": self.extract_designation(data),

            "education": self.extract_education(data),

            "city": self.extract_city(data),

            "summary": self.extract_summary(data)

        }

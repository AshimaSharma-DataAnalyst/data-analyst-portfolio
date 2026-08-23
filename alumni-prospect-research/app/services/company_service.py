class CompanyService:

    def __init__(self):

        self.company_database = {

            "microsoft": {

                "industry": "Technology",

                "company_type": "Public",

                "headquarters": "Redmond, Washington, USA",

                "founded": 1975,

                "employees": 228000,

                "website": "https://www.microsoft.com"

            },

            "google": {

                "industry": "Technology",

                "company_type": "Public",

                "headquarters": "Mountain View, California, USA",

                "founded": 1998,

                "employees": 182000,

                "website": "https://www.google.com"

            },

            "amazon": {

                "industry": "E-Commerce",

                "company_type": "Public",

                "headquarters": "Seattle, Washington, USA",

                "founded": 1994,

                "employees": 1525000,

                "website": "https://www.amazon.com"

            },

            "meta": {

                "industry": "Social Media",

                "company_type": "Public",

                "headquarters": "Menlo Park, California, USA",

                "founded": 2004,

                "employees": 86000,

                "website": "https://about.meta.com"

            }

        }

    def get_company_information(self, company):

        if not company:

            return {

                "industry": "Unknown",

                "company_type": "Unknown",

                "headquarters": "Unknown",

                "founded": None,

                "employees": None,

                "website": ""

            }

        company = company.lower()

        for key in self.company_database:

            if key in company:

                return self.company_database[key]

        return {

            "industry": "Unknown",

            "company_type": "Unknown",

            "headquarters": "Unknown",

            "founded": None,

            "employees": None,

            "website": ""

        }

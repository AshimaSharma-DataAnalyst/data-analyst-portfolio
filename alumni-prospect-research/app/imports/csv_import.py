import pandas as pd

from app.models.alumni import Alumni


class CSVImporter:
    """
    Handles importing alumni records from CSV.
    """

    @staticmethod
    def import_file(file_path):

        dataframe = pd.read_csv(file_path)

        alumni_records = []

        required_columns = [

            "Name",
            "Company",
            "Designation",
            "City",
            "LinkedIn URL",
            "Source",
            "Summary"

        ]

        for column in required_columns:

            if column not in dataframe.columns:

                raise ValueError(
                    f"Missing required column: {column}"
                )

        for _, row in dataframe.iterrows():

            alumni = Alumni(

                name=str(row["Name"]).strip(),

                company=str(row["Company"]).strip(),

                designation=str(row["Designation"]).strip(),

                city=str(row["City"]).strip(),

                linkedin_url=str(
                    row["LinkedIn URL"]
                ).strip(),

                source=str(row["Source"]).strip(),

                summary=str(row["Summary"]).strip()

            )

            alumni_records.append(alumni)

        return alumni_records
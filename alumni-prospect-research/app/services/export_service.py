import json
import pandas as pd


class ExportService:

    def export_csv(self, dataframe, file_path):

        dataframe.to_csv(

            file_path,

            index=False

        )

        print(f"CSV exported to {file_path}")

    def export_excel(self, dataframe, file_path):

        dataframe.to_excel(

            file_path,

            index=False

        )

        print(f"Excel exported to {file_path}")

    def export_json(self, dataframe, file_path):

        records = dataframe.to_dict(

            orient="records"

        )

        with open(

            file_path,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                records,

                file,

                indent=4,

                ensure_ascii=False

            )

        print(f"JSON exported to {file_path}")

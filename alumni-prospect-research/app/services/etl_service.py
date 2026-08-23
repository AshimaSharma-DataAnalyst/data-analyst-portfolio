import os
import pandas as pd

from app.scraper.wiki_scraper import WikiScraper
from app.services.database_service import DatabaseService
from app.services.export_service import ExportService
from app.services.research_service import ResearchService
from app.utils.logger import logger


class ETLPipeline:
    """
    ETL Pipeline for Alumni Intelligence Platform.

    Workflow:
    1. Load alumni names from CSV
    2. Scrape alumni profile
    3. Generate AI research summary
    4. Store data in database
    5. Export results to CSV, Excel and JSON
    """

    EXPORT_FOLDER = "exports"

    def __init__(self, db):

        self.scraper = WikiScraper()

        self.database = DatabaseService(db)

        self.exporter = ExportService()

        self.research = ResearchService()

        os.makedirs(
            self.EXPORT_FOLDER,
            exist_ok=True
        )

        logger.info("ETL Pipeline initialized.")

    # =====================================================
    # LOAD CSV
    # =====================================================

    def load_csv(
        self,
        file_path: str
    ) -> pd.DataFrame:
        """
        Load a CSV file into a pandas DataFrame.
        """

        try:

            dataframe = pd.read_csv(file_path)

            logger.info(
                f"Loaded CSV with {len(dataframe)} rows."
            )

            return dataframe

        except Exception as e:

            logger.exception(e)

            raise

    # =====================================================
    # PROCESS ONE ALUMNI
    # =====================================================

    def process_person(
        self,
        name: str
    ):
        """
        Process one alumni record.

        Steps:
        1. Scrape profile
        2. Generate AI research
        3. Save to database
        """

        try:

            logger.info(
                f"Processing alumni: {name}"
            )

            profile = self.scraper.scrape_page(name)

            if profile.get("status") != "Success":

                logger.warning(
                    f"Scraping failed for {name}"
                )

                return None

            research = self.research.build_profile(
                profile
            )

            alumni = self.database.create_alumni(
                research
            )

            logger.success(
                f"Successfully processed {name}"
            )

            return alumni

        except Exception as e:

            logger.exception(
                f"Failed processing {name}: {e}"
            )

            return None

    # =====================================================
    # PROCESS ENTIRE DATAFRAME
    # =====================================================

    def process_dataframe(
        self,
        dataframe: pd.DataFrame
    ):
        """
        Process every alumni record in the DataFrame.

        Returns:
            List of created Alumni objects.
        """

        try:

            if dataframe.empty:

                logger.warning(
                    "Input dataframe is empty."
                )

                return []

            if "Name" not in dataframe.columns:

                raise ValueError(
                    "CSV must contain a 'Name' column."
                )

            results = []

            export_rows = []

            for _, row in dataframe.iterrows():

                alumni = self.process_person(

                    row["Name"]

                )

                if alumni is None:

                    continue

                results.append(alumni)

                export_rows.append({

                    "ID": alumni.id,

                    "Name": alumni.name,

                    "Company": alumni.company,

                    "Designation": alumni.designation,

                    "City": alumni.city,

                    "Source": alumni.source,

                    "Summary": alumni.summary

                })

            export_df = pd.DataFrame(export_rows)

            if not export_df.empty:

                csv_path = os.path.join(

                    self.EXPORT_FOLDER,

                    "alumni.csv"

                )

                excel_path = os.path.join(

                    self.EXPORT_FOLDER,

                    "alumni.xlsx"

                )

                json_path = os.path.join(

                    self.EXPORT_FOLDER,

                    "alumni.json"

                )

                self.exporter.export_csv(

                    export_df,

                    csv_path

                )

                self.exporter.export_excel(

                    export_df,

                    excel_path

                )

                self.exporter.export_json(

                    export_df,

                    json_path

                )

                logger.success(

                    f"""
ETL Pipeline Completed Successfully

Processed Records : {len(results)}

CSV Export        : {csv_path}

Excel Export      : {excel_path}

JSON Export       : {json_path}
"""

                )

            else:

                logger.warning(

                    "No alumni records were exported."

                )

            return results

        except Exception as e:

            logger.exception(e)

            raise
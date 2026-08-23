import os
import csv
import pandas as pd

from typing import Optional

from sqlalchemy import asc, desc, func
from sqlalchemy.orm import Session

from app.models.alumni import Alumni
from app.utils.logger import logger


class DatabaseService:
    """
    Handles all database operations for Alumni.
    """

    # =====================================================
    # INITIALIZE DATABASE SESSION
    # =====================================================

    def __init__(self, db: Session):
        self.db = db

    # =====================================================
    # CREATE
    # =====================================================

    def create_alumni(self, alumni_data) -> Alumni:
        """
        Create a new alumni record.
        """

        try:

            if hasattr(alumni_data, "model_dump"):
                data = alumni_data.model_dump()
            else:
                data = alumni_data

            # Convert HttpUrl → string
            if data.get("linkedin_url"):
                data["linkedin_url"] = str(data["linkedin_url"])

            alumni = Alumni(**data)

            self.db.add(alumni)
            self.db.commit()
            self.db.refresh(alumni)

            logger.info(f"Created alumni: {alumni.name}")

            return alumni

        except Exception as e:

            self.db.rollback()
            logger.exception(e)
            raise

    # =====================================================
    # READ ALL
    # Pagination + Sorting + Metadata
    # =====================================================

    def get_all_alumni(
        self,
        page: int,
        size: int,
        sort_by: str,
        order: str
    ) -> dict:

        try:

            offset = (page - 1) * size

            sortable_columns = {

                "id": Alumni.id,
                "name": Alumni.name,
                "company": Alumni.company,
                "city": Alumni.city,
                "designation": Alumni.designation

            }

            column = sortable_columns.get(
                sort_by,
                Alumni.id
            )

            sort_order = (
                desc(column)
                if order.lower() == "desc"
                else asc(column)
            )

            total_records = self.db.query(
                func.count(Alumni.id)
            ).scalar()

            total_pages = (
                total_records + size - 1
            ) // size

            items = (

                self.db.query(Alumni)

                .order_by(sort_order)

                .offset(offset)

                .limit(size)

                .all()

            )

            logger.info(

                f"Fetched page={page}, "
                f"size={size}, "
                f"records={len(items)}"

            )

            return {

                "page": page,

                "size": size,

                "total_records": total_records,

                "total_pages": total_pages,

                "items": items

            }

        except Exception as e:

            logger.exception(e)

            raise

    # =====================================================
    # READ ONE
    # =====================================================

    def get_alumni_by_id(
        self,
        alumni_id: int
    ) -> Optional[Alumni]:

        try:

            alumni = (

                self.db.query(Alumni)

                .filter(
                    Alumni.id == alumni_id
                )

                .first()

            )

            if alumni:

                logger.info(
                    f"Fetched alumni ID {alumni_id}"
                )

            else:

                logger.warning(
                    f"Alumni ID {alumni_id} not found"
                )

            return alumni

        except Exception as e:

            logger.exception(e)

            raise

    # =====================================================
    # SEARCH
    # Filter + Pagination + Metadata
    # =====================================================

    def search_alumni(

        self,

        name: str | None = None,

        company: str | None = None,

        city: str | None = None,

        designation: str | None = None,

        page: int = 1,

        size: int = 10

    ) -> dict:

        try:

            query = self.db.query(Alumni)

            if name:

                query = query.filter(

                    Alumni.name.ilike(f"%{name}%")

                )

            if company:

                query = query.filter(

                    Alumni.company.ilike(f"%{company}%")

                )

            if city:

                query = query.filter(

                    Alumni.city.ilike(f"%{city}%")

                )

            if designation:

                query = query.filter(

                    Alumni.designation.ilike(
                        f"%{designation}%"
                    )

                )

            total_records = query.count()

            offset = (page - 1) * size

            items = (

                query

                .order_by(Alumni.name)

                .offset(offset)

                .limit(size)

                .all()

            )

            total_pages = (

                total_records + size - 1

            ) // size

            logger.info(

                f"Search returned "

                f"{len(items)} records"

            )

            return {

                "page": page,

                "size": size,

                "total_records": total_records,

                "total_pages": total_pages,

                "items": items

            }

        except Exception as e:

            logger.exception(e)

            raise

    # =====================================================
    # UPDATE
    # =====================================================

    def update_alumni(

        self,

        alumni_id: int,

        alumni_data

    ) -> Optional[Alumni]:

        try:

            alumni = self.get_alumni_by_id(
                alumni_id
            )

            if alumni is None:

                return None

            if hasattr(alumni_data, "model_dump"):
                update_data = alumni_data.model_dump()
            else:
                update_data = alumni_data

            # Convert HttpUrl to string
            if update_data.get("linkedin_url"):
                update_data["linkedin_url"] = str(update_data["linkedin_url"])

            for key, value in update_data.items():

                setattr(
                    alumni,
                    key,
                    value
                )

            self.db.commit()

            self.db.refresh(alumni)

            logger.info(
                f"Updated alumni ID {alumni_id}"
            )

            return alumni

        except Exception as e:

            self.db.rollback()

            logger.exception(e)

            raise

    # =====================================================
    # DELETE
    # =====================================================

    def delete_alumni(
        self,
        alumni_id: int
    ) -> bool:

        try:

            alumni = self.get_alumni_by_id(
                alumni_id
            )

            if alumni is None:

                return False

            self.db.delete(alumni)

            self.db.commit()

            logger.info(
                f"Deleted alumni ID {alumni_id}"
            )

            return True

        except Exception as e:

            self.db.rollback()

            logger.exception(e)

            raise

    # =====================================================
    # DASHBOARD STATISTICS
    # =====================================================

    def get_statistics(self) -> dict:

        try:

            total_alumni = self.db.query(

                func.count(
                    Alumni.id
                )

            ).scalar()

            total_companies = self.db.query(

                func.count(

                    func.distinct(
                        Alumni.company
                    )

                )

            ).scalar()

            total_cities = self.db.query(

                func.count(

                    func.distinct(
                        Alumni.city
                    )

                )

            ).scalar()

            return {

                "total_alumni": total_alumni,

                "total_companies": total_companies,

                "total_cities": total_cities

            }

        except Exception as e:

            logger.exception(e)

            raise

    # =====================================================
    # COMPANY STATISTICS
    # =====================================================

    def company_statistics(self) -> list:

        try:

            result = (

                self.db.query(

                    Alumni.company,

                    func.count(
                        Alumni.id
                    ).label("count")

                )

                .group_by(
                    Alumni.company
                )

                .order_by(

                    func.count(
                        Alumni.id
                    ).desc()

                )

                .all()

            )

            return [

                {

                    "company": company,

                    "count": count

                }

                for company, count in result

            ]

        except Exception as e:

            logger.exception(e)

            raise

    # =====================================================
    # CITY STATISTICS
    # =====================================================

    def city_statistics(self) -> list:

        try:

            result = (

                self.db.query(

                    Alumni.city,

                    func.count(
                        Alumni.id
                    ).label("count")

                )

                .group_by(
                    Alumni.city
                )

                .order_by(

                    func.count(
                        Alumni.id
                    ).desc()

                )

                .all()

            )

            return [

                {

                    "city": city,

                    "count": count

                }

                for city, count in result

            ]

        except Exception as e:

            logger.exception(e)

            raise

    # =====================================================
    # EXPORT CSV
    # =====================================================

    def export_csv(self):

        try:

            alumni = (

                self.db.query(Alumni)

                .order_by(Alumni.name)

                .all()

            )

            from app.exports.csv_export import CSVExporter

            return CSVExporter.export_alumni(

                alumni

            )

        except Exception as e:

            logger.exception(e)

            raise

    # =====================================================
    # EXPORT EXCEL
    # =====================================================

    def export_excel(self):

        try:

            alumni = (

                self.db.query(Alumni)

                .order_by(Alumni.name)

                .all()

            )

            from app.exports.excel_export import ExcelExporter

            return ExcelExporter.export_alumni(

                alumni

            )

        except Exception as e:

            logger.exception(e)

            raise

# =====================================================
# IMPORT CSV
# =====================================================

    def import_csv(self, filepath):

        try:

            from app.imports.csv_import import CSVImporter

            alumni_records = CSVImporter.import_file(

                filepath

            )

            self.db.add_all(

                alumni_records

            )

            self.db.commit()

            logger.info(

                f"Imported {len(alumni_records)} alumni"

            )

            return {

                "success": True,

                "records_imported": len(alumni_records)

            }

        except Exception as e:

            self.db.rollback()

            logger.exception(e)

            raise

    # =====================================================
    # EXPORT ALL ALUMNI
    # =====================================================

    def export_alumni(self):

        try:

            alumni = (

                self.db.query(Alumni)

                .order_by(Alumni.name)

                .all()

            )

            logger.info(

                f"Exported {len(alumni)} alumni"

            )

            return alumni

        except Exception as e:

            logger.exception(e)

            raise
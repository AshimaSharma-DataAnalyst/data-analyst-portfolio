"""
SQLAlchemy ORM model for the Alumni table.

This model defines the structure of the 'alumni' table
used throughout the application.
"""

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class Alumni(Base):
    """
    Represents an alumni profile stored in the database.
    """

    # -------------------------------------------------
    # Database Table Name
    # -------------------------------------------------

    __tablename__ = "alumni"

    # -------------------------------------------------
    # Primary Key
    # -------------------------------------------------

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # -------------------------------------------------
    # Alumni Information
    # -------------------------------------------------

    name = Column(
        String(100),
        nullable=False
    )

    company = Column(
        String(100),
        nullable=False
    )

    designation = Column(
        String(255)
    )

    city = Column(
        String(100)
    )

    linkedin_url = Column(
        String(255)
    )

    source = Column(
        String(100)
    )

    summary = Column(
        String
    )
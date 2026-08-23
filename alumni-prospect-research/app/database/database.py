"""
Database configuration.

This module is responsible for:

- Creating the SQLAlchemy engine
- Creating database sessions
- Providing the Base class for ORM models
- Managing database connections for FastAPI
"""

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings


# -------------------------------------------------
# Database Engine
# -------------------------------------------------

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True
)


# -------------------------------------------------
# Database Session Factory
# -------------------------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# -------------------------------------------------
# Base Class for SQLAlchemy Models
# -------------------------------------------------

Base = declarative_base()


# -------------------------------------------------
# Dependency for FastAPI
# -------------------------------------------------

def get_db() -> Generator:
    """
    Creates a new database session for each request.

    The session is automatically closed after the
    request is completed.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
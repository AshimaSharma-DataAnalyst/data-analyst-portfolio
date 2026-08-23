"""
Application configuration settings.

This file loads environment variables from the .env file
and provides a single place to access project settings.

Any configuration required by the application should be
defined here instead of being hardcoded in the codebase.
"""

import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Settings:
    """
    Central configuration class.

    Stores all application settings so that other modules
    can access them through the 'settings' object.
    """

    # -------------------------------------------------
    # Project Information
    # -------------------------------------------------

    PROJECT_NAME: str = os.getenv(
        "PROJECT_NAME",
        "Alumni Intelligence & Prospect Research Platform"
    )

    VERSION: str = "1.0.0"

    # -------------------------------------------------
    # Database Configuration
    # -------------------------------------------------

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./alumni.db"
    )

    # -------------------------------------------------
    # AI Configuration
    # -------------------------------------------------

    OPENROUTER_API_KEY: str = os.getenv(
        "OPENROUTER_API_KEY",
        ""
    )

    LLM_PROVIDER: str = os.getenv(
        "LLM_PROVIDER",
        "openrouter"
    )

    LLM_MODEL: str = os.getenv(
        "LLM_MODEL",
        "deepseek/deepseek-chat-v3-0324:free"
    )

    # -------------------------------------------------
    # Logging Configuration
    # -------------------------------------------------

    LOG_LEVEL: str = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    JWT_SECRET = os.getenv(
        "JWT_SECRET",
        "CHANGE_THIS_TO_A_LONG_RANDOM_SECRET"
    )

    JWT_ALGORITHM = os.getenv(
        "JWT_ALGORITHM",
        "HS256"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES",
            "60"
        )
    )


# Global settings instance
settings = Settings()
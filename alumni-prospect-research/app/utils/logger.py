import os
import sys

from loguru import logger


# =====================================================
# Create logs directory
# =====================================================

LOG_DIR = "logs"

os.makedirs(

    LOG_DIR,

    exist_ok=True

)


# =====================================================
# Remove Default Logger
# =====================================================

logger.remove()


# =====================================================
# Console Logger
# =====================================================

logger.add(

    sys.stdout,

    level="INFO",

    colorize=True,

    enqueue=True,

    backtrace=True,

    diagnose=True,

    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:"
        "<cyan>{function}</cyan>:"
        "<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )

)


# =====================================================
# File Logger
# =====================================================

logger.add(

    f"{LOG_DIR}/application.log",

    rotation="10 MB",

    retention="30 days",

    compression="zip",

    level="INFO",

    enqueue=True,

    backtrace=True,

    diagnose=True,

    encoding="utf-8",

    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level:<8} | "
        "{name}:{function}:{line} | "
        "{message}"
    )

)


# =====================================================
# Error Logger
# =====================================================

logger.add(

    f"{LOG_DIR}/errors.log",

    rotation="5 MB",

    retention="60 days",

    compression="zip",

    level="ERROR",

    enqueue=True,

    backtrace=True,

    diagnose=True,

    encoding="utf-8",

    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level:<8} | "
        "{name}:{function}:{line} | "
        "{message}"
    )

)
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.settings import settings
from app.database.database import Base
from app.database.database import engine

from app.middleware.request_logging import RequestLoggingMiddleware
from app.middleware.exception_handler import ExceptionHandler

from app.routers import alumni
from app.routers import health
from app.routers import auth
from app.routers import research

from app.utils.logger import logger

# =====================================================
# Create Database Tables
# =====================================================

Base.metadata.create_all(bind=engine)

logger.success("Database initialized successfully.")


# =====================================================
# Lifespan Events
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.success("Application Startup Completed.")

    yield

    logger.success("Application Shutdown Completed.")


# =====================================================
# FastAPI Application
# =====================================================

app = FastAPI(

    title=settings.PROJECT_NAME,

    version=settings.VERSION,

    description="Alumni Intelligence & Prospect Research Platform",

    lifespan=lifespan

)


# =====================================================
# Middleware
# =====================================================

app.add_middleware(

    RequestLoggingMiddleware

)


# =====================================================
# Global Exception Handler
# =====================================================

ExceptionHandler.register(app)


# =====================================================
# Routers
# =====================================================

app.include_router(

    health.router

)

app.include_router(
    auth.router
)


app.include_router(

    alumni.router

)

app.include_router(
    research.router
)

logger.success("FastAPI application started successfully.")


# =====================================================
# Root Endpoint
# =====================================================

@app.get(

    "/",

    tags=["Root"]

)

def root():

    return {

        "project": settings.PROJECT_NAME,

        "version": settings.VERSION,

        "status": "Running",

        "docs": "/docs",

        "health": "/health"

    }
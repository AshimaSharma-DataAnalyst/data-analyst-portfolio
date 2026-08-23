from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request

from fastapi.responses import JSONResponse

from app.utils.logger import logger


class ExceptionHandler:
    """
    Registers global exception handlers.
    """

    @staticmethod
    def register(app: FastAPI):

        # ==========================================
        # HTTP Exceptions
        # ==========================================

        @app.exception_handler(HTTPException)
        async def http_exception_handler(
            request: Request,
            exc: HTTPException
        ):

            logger.warning(

                f"{request.method} {request.url.path} | "
                f"HTTP {exc.status_code} | {exc.detail}"

            )

            return JSONResponse(

                status_code=exc.status_code,

                content={

                    "success": False,

                    "status": exc.status_code,

                    "message": exc.detail

                }

            )

        # ==========================================
        # Validation Errors
        # ==========================================

        @app.exception_handler(ValueError)
        async def value_error_handler(
            request: Request,
            exc: ValueError
        ):

            logger.error(

                f"{request.method} {request.url.path} | {str(exc)}"

            )

            return JSONResponse(

                status_code=400,

                content={

                    "success": False,

                    "status": 400,

                    "message": str(exc)

                }

            )

        # ==========================================
        # Generic Exceptions
        # ==========================================

        @app.exception_handler(Exception)
        async def generic_exception_handler(
            request: Request,
            exc: Exception
        ):

            logger.exception(exc)

            return JSONResponse(

                status_code=500,

                content={

                    "success": False,

                    "status": 500,

                    "message": "Internal Server Error"

                }

            )
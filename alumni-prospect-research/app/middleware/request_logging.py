import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.utils.logger import logger


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware to log every incoming request and outgoing response.
    """

    async def dispatch(self, request: Request, call_next):

        start_time = time.perf_counter()

        client_ip = (
            request.client.host
            if request.client
            else "Unknown"
        )

        logger.info(
            f"Incoming Request | "
            f"Method={request.method} | "
            f"Path={request.url.path} | "
            f"Client={client_ip}"
        )

        try:

            response = await call_next(request)

        except Exception:

            logger.exception(
                f"Unhandled Exception | "
                f"Method={request.method} | "
                f"Path={request.url.path}"
            )

            raise

        process_time = round(

            time.perf_counter() - start_time,

            4

        )

        logger.info(
            f"Completed Request | "
            f"Method={request.method} | "
            f"Path={request.url.path} | "
            f"Status={response.status_code} | "
            f"Time={process_time}s"
        )

        response.headers["X-Process-Time"] = str(process_time)

        return response

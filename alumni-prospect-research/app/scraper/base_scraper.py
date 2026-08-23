import requests

from app.config.logging_config import logger
from app.utils.retry import retry


class BaseScraper:

    def __init__(self):

        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"
            )
        }

        self.timeout = 20

    def download_page(self, url):

        try:

            logger.info(f"Downloading: {url}")

            response = retry(
                lambda: requests.get(
                    url,
                    headers=self.headers,
                    timeout=self.timeout
                )
            )

            response.raise_for_status()

            logger.info("Download Successful")

            return response.text

        except requests.exceptions.Timeout:

            logger.error("Request Timed Out")
            raise

        except requests.exceptions.HTTPError as e:

            logger.error(f"HTTP Error: {e}")
            raise

        except requests.exceptions.RequestException as e:

            logger.error(f"Network Error: {e}")
            raise
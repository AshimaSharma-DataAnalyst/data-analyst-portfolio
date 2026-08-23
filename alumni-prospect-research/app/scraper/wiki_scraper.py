from app.scraper.base_scraper import BaseScraper
from app.scraper.parser import HTMLParser
from app.scraper.extractor import AlumniExtractor
from app.utils.logger import logger

class WikiScraper(BaseScraper):

    BASE_URL = "https://en.wikipedia.org/wiki/"

    def __init__(self):

        super().__init__()

        self.parser = HTMLParser()
        self.extractor = AlumniExtractor()

    def build_url(self, person_name):

        return self.BASE_URL + person_name.replace(" ", "_")

    def scrape_page(self, person_name):

        try:

            url = self.build_url(person_name)

            html = self.download_page(url)

            soup = self.parser.parse_html(html)

            data = {

                "status": "Success",

                "name": person_name,

                "url": url,

                "title": self.parser.get_title(soup),

                "heading": self.parser.get_h1(soup),

                "meta_description": self.parser.get_meta_description(soup),

                "paragraphs": self.parser.get_all_paragraphs(soup),

                "links": self.parser.get_all_links(soup),

                "images": self.parser.get_all_images(soup),

                "tables": self.parser.get_all_tables(soup),

                "infobox": self.parser.get_infobox(soup)

            }

            profile = self.extractor.extract_profile(data)

            profile["status"] = "Success"

            profile["url"] = url

            return profile

        except Exception as e:

            return {

                "status": "Failed",

                "name": person_name,

                "error": str(e)

            }

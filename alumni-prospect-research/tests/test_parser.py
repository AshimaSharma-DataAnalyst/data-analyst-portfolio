from app.scraper.base_scraper import BaseScraper
from app.scraper.parser import HTMLParser


scraper = BaseScraper()

parser = HTMLParser()


html = scraper.download_page(

    "https://en.wikipedia.org/wiki/Satya_Nadella"

)

soup = parser.parse_html(html)


print("=" * 60)

print("TITLE")

print(parser.get_title(soup))


print("=" * 60)

print("H1")

print(parser.get_h1(soup))


print("=" * 60)

print("META")

print(parser.get_meta_description(soup))


print("=" * 60)

print("PARAGRAPHS")

print(len(parser.get_all_paragraphs(soup)))


print("=" * 60)

print("LINKS")

print(len(parser.get_all_links(soup)))


print("=" * 60)

print("IMAGES")

print(len(parser.get_all_images(soup)))


print("=" * 60)

print("TABLES")

print(len(parser.get_all_tables(soup)))


print("=" * 60)

print("INFOBOX")

info = parser.get_infobox(soup)

for key, value in info.items():

    print(key, ":", value)

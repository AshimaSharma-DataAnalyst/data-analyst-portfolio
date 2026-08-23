from app.scraper.wiki_scraper import WikiScraper

scraper = WikiScraper()

result = scraper.scrape_page("Satya Nadella")

print("=" * 70)

print("STATUS")

print(result["status"])

print("=" * 70)

print("TITLE")

print(result["title"])

print("=" * 70)

print("HEADING")

print(result["heading"])

print("=" * 70)

print("URL")

print(result["url"])

print("=" * 70)

print("META DESCRIPTION")

print(result["meta_description"])

print("=" * 70)

print("NUMBER OF PARAGRAPHS")

print(len(result["paragraphs"]))

print("=" * 70)

print("NUMBER OF LINKS")

print(len(result["links"]))

print("=" * 70)

print("NUMBER OF IMAGES")

print(len(result["images"]))

print("=" * 70)

print("INFOBOX")

for key, value in result["infobox"].items():

    print(f"{key}: {value}")
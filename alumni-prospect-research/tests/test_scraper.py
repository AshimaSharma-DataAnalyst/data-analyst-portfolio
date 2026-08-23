from app.scraper.base_scraper import BaseScraper

scraper = BaseScraper()

html = scraper.download_page(

    "https://en.wikipedia.org/wiki/Satya_Nadella"

)

print("=" * 60)

print(html[:500])

print("=" * 60)

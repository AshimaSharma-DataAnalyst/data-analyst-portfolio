from app.scraper.wiki_scraper import WikiScraper

scraper = WikiScraper()

profile = scraper.scrape_page("Satya Nadella")

print("="*70)

for key, value in profile.items():

    print(f"{key}: {value}")

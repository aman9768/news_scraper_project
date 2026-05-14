from src.scraper import scrape_headlines
from src.save_csv import save_to_csv

def main():
    print("Scraping headlines...")

    data = scrape_headlines()

    save_to_csv(data)

    print("Project completed successfully!")

if __name__ == "__main__":
    main()
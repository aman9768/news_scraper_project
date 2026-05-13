import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = "https://news.ycombinator.com"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("span", class_="titleline")

    news_data = []

    for headline in headlines[:100]:
        title = headline.text

        link = headline.find("a")["href"]

        news_data.append({
            "title": title,
            "link": link
        })

    return news_data
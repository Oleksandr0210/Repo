import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "http://quotes.toscrape.com"
AUTHORS_URL = "/author/"


def scrape_quotes():
    quotes = []
    authors_info = {}
    page = 1

    while True:
        response = requests.get(f"{BASE_URL}/page/{page}/")
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quote_blocks = soup.find_all("div", class_="quote")

        for block in quote_blocks:
            quote_text = block.find("span", class_="text").get_text(strip=True)
            author = block.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True)
                    for tag in block.find_all("a", class_="tag")]

            quotes.append({
                "quote": quote_text,
                "author": author,
                "tags": tags,
            })

            if author not in authors_info:
                author_link = block.find("a", href=True)["href"]
                authors_info[author] = scrape_author_info(
                    BASE_URL + author_link)

        page += 1

    return quotes, list(authors_info.values())


def scrape_author_info(author_url):
    response = requests.get(author_url)
    soup = BeautifulSoup(response.text, "html.parser")

    fullname = soup.find("h3", class_="author-title").get_text(strip=True)
    born_date = soup.find(
        "span", class_="author-born-date").get_text(strip=True)
    born_location = soup.find(
        "span", class_="author-born-location").get_text(strip=True)
    description = soup.find(
        "div", class_="author-description").get_text(strip=True)

    return {
        "fullname": fullname,
        "born_date": born_date,
        "born_location": born_location,
        "description": description,
    }


def main():
    quotes, authors = scrape_quotes()

    with open("qoutes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)

    with open("authors.json", "w", encoding="utf-8") as f:
        json.dump(authors, f, ensure_ascii=False, indent=4)

    print("Дані збережено у файли: qoutes.json та authors.json.")


if __name__ == "__main__":
    main()
import requests
from bs4 import BeautifulSoup

WEBSITE_URL = "https://quotes.toscrape.com/"


def get_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def get_authors(content):
    soup = BeautifulSoup(content, "html.parser")
    authors = soup.find_all('small', class_='author')
    return [author.get_text() for author in authors]


if __name__ == '__main__':
    content = get_website_content(WEBSITE_URL)
    if content:
        authors = get_authors(content)
        for author in authors:
            print(author)

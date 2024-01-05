import requests
from bs4 import BeautifulSoup

WEBSITE_URL = "https://techcrunch.com/"


def get_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == '__main__':
    content = get_website_content(WEBSITE_URL)
    if content:
        soup = BeautifulSoup(content, "html.parser")

        headlines = soup.find_all('h2')
        for headline in headlines:
            print(headline.text.strip())

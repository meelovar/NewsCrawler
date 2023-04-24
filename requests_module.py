import requests
from bs4 import BeautifulSoup

GNEWS_BASE_URL = "https://news.google.com"


def get_links():
    response = requests.get(f"{GNEWS_BASE_URL}/home")
    soup = BeautifulSoup(response.text, "html.parser")
    result = []

    for a in soup.find_all("a", href=True):
        href = a["href"]

        if "/articles/" in href:
            result.append(f"{GNEWS_BASE_URL}{href[1:]}")

    return result

import requests
from bs4 import BeautifulSoup
import pandas as pd


def mainfunction():
    start_url = 'https://en.wikipedia.org/wiki/Rust_(programming_language)'

    downloaded_html = requests.get(start_url)
    soup = BeautifulSoup(downloaded_html.text, features="html.parser")

    with open('downloaded_html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
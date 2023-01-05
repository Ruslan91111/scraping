import os

import requests
from bs4 import BeautifulSoup

def get_all_pages():
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like "
                      "Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
    }
    r = requests.get(url="https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/", headers=headers)

    if not os.path.exists("data"):
        os.mkdir("data")

    # Запись главной страницы
    with open("data/page_1.html", "w", encoding="utf-8") as file:
        file.write(r.text)


def main():
    get_all_pages()


if __name__ == '__main__':
    main()

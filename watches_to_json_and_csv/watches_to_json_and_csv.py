"""
Программа для скрапинга данных и их дальнейшей записи в json и csv форматах.
Scraping с сайта с пяти страниц пагинации.
"""
import csv
import json
import os
import time

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_all_pages():
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like "
                      "Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
    }
    # r = requests.get(url="https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/", headers=headers)
    #
    # if not os.path.exists("data"):
    #     os.mkdir("data")
    #
    # # Запись главной страницы
    # with open("data/page_1.html", "w", encoding="utf-8") as file:
    #     file.write(r.text)


    # читаем созданный файл с html кодом и сохраняем в переменную
    with open("data/page_1.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # собираем колличество страниц - код для пагинации
    pages_count = int(soup.find("div", class_="bx-pagination-container").find_all("a")[-2].text)

    for i in range(1, pages_count + 1):
        url = f"https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/?PAGEN_1={i}"
        # направляем запрос к каждой из страниц
        r = requests.get(url=url, headers=headers)

        # записываем каждую страницу как отдельный файл
        with open(f"data/page_{i}.html", "w", encoding="utf-8") as file:
            file.write(r.text)

        time.sleep(2)

    # функция возвращает количество страниц
    return pages_count + 1


def collect_data(pages_count):
    cur_date = datetime.now().strftime("%d_%m_%y")


    # создаем и открываем на запись файл формата .csv
    with open(f"data_{cur_date}.csv", "w", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "Артикул",
                "Ссылка",
            )
        )

    data = []

    # цикл, который будет читать полученные ранее страницы
    for page in range(1, pages_count):
        with open(f"data/page_{page}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        items_cards = soup.find_all("a", class_="product-item__link")

        for item in items_cards:
            product_article = item.find("p", class_ ="product-item__articul").text.strip()
            product_url = f"https://shop.casio.ru{item.get('href')}"

            # print(f"Article: {product_article} - Url: {product_url}")
            data.append(
                {"product_article": product_article,
                 "product_url": product_url
                 }
            )

            with open(f"data_{cur_date}.csv", "a", encoding='utf-8') as file:
                writer = csv.writer(file)

                writer.writerow(
                    (
                        product_article,
                        product_url
                    )
                )

        print(f"[INFO] Обработана страница {page}/5")

    # запись в json-файл
    with open(f"data_{cur_date}.json", "a") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pages_count = get_all_pages()
    collect_data(pages_count=pages_count)


if __name__ == '__main__':
    main()

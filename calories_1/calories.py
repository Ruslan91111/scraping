"""     Парсинг данных с вебсайта о здоровом питании, а именно каллорийность, БЖУ по позициям
 с сохранением данных в форматах: csv по каждай итерации и одним общим файлом json """


import csv
import json
import random
from time import sleep

import requests
from bs4 import BeautifulSoup

# код запроса и сохранения страницы.html на ПК в формате .html


# url = "https://health-diet.ru/table_calorie"       # страница, подлежащая парсингу
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
}
# req = requests.get(url, headers=headers)      # осуществить get запрос
# src = req.text                                # передать текст из результата запроса

# сохранить страницу, на случай бана или ограничения во времени
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

# прочитать страницу.html с ПК
# with open("index.html", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")      # объект супа, "lxml" - парсер
# all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")   # найти все теги определенного класса со стр-цы
#

# сохранить в словарь ключ - текст, значение - ссылка
# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#
#     all_categories_dict[item_text] = item_href
#
# # сохранение в json документ
# with open("all_categories_dict.json", "w", encoding="utf-8") as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)  # indent - отступ, без него всё будет в ряд
#                                                 #ensure_ascii не экранирует символы и помогает при работе с кириллицей
#


# загрузить содержимое json документа в переменную
with open("all_categories_dict.json", encoding="UTF-8") as file:
    all_categories = json.load(file)

iteration_count = int(len(all_categories)) - 1
count = 0
print(f"Всего итераций: {iteration_count}")

for category_name, category_href in all_categories.items():

    rep = [",", " ", "-", "'", '"']
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")  # заменить набор символов в ключах на "_"
    # print(category_name)

    # запросы со списка категорий на страницы
    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", "w", encoding="UTF-8") as file:     # сохраняем
        file.write(src)

    with open(f"data/{count}_{category_name}.html", encoding="UTF-8") as file:  # читаем нашу страницу
        src = file.read()

    soup = BeautifulSoup(src, "lxml")

    # проверка страницы на наличие таблицы с продуктами
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue

    # собираем в файл csv заголовки таблицы
    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    # ставим файл на запись
    with open(f"data/{count}_{category_name}.csv", "w", encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (product, calories, proteins, fats, carbohydrates)
        )

    # собираем все остальные данные
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    product_info = []  # список для json документа
    for item in products_data:
        products_tds = item.find_all("td")

        title = products_tds[0].find("a").text  # выводит первую колонку
        calories = products_tds[1].text
        proteins = products_tds[2].text
        fats = products_tds[3].text
        carbohydrates = products_tds[4].text

        product_info.append({  # добавляем для json документа
            "title": title,
            "calories_1": calories,
            "proteins": proteins,
            "fats": fats,
            "carbohydrates": carbohydrates,
        })

    # ставим файл на запись csv
    with open(f"data/{count}_{category_name}.csv", "a", encoding="UTF-8") as file:  # a - append
        writer = csv.writer(file)
        writer.writerow(
            (title, calories, proteins, fats, carbohydrates)
        )

    # ставим файл на запись json
    with open(f"data/{count}_{category_name}.json", "w", encoding="UTF-8") as file:
        json.dump(product_info, file, indent=4, ensure_ascii=False)

    count += 1
    print(f"#Итерация {count}. {category_name} записан...")
    iteration_count -= 1

    if iteration_count == 0:
        print("Работа завершена")
        break

    print(f"Осталось {iteration_count} итераций")
    sleep(random.randrange(2, 4))

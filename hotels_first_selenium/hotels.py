"""
Парсинг сайта с отелями.
1 - сохранить на ПК html-страницу.
2 - прочитать сохраненный на пк html-файл, выбрать и вывести ссылки отелей
3 - сохранить файл html при помощи selenium и WebDriver
"""

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# 1 КОД: сохранить  html-страницу на ПК.
# Записать html-файл c html кодом страницы
# def get_data(url):
#     headers = {
#         "Accept": "text/html, application/xhtml+xml, application/xml; q = 0.9, image/avif, image/webp, image/apng,"
#                   " */*; q=0.8, application/signed-exchange;v = b3;q = 0.9",
#         "Accept-encoding": "gzip, deflate",
#         "Accept - language": "en",
#         "Cache-controlA": "max-age=0",
#         "Connection": "keep-alive",
#         "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36(KHTML, like Gecko)" \
#                       "Chrome/108.0.0.0 Mobile Safari/537.36"
#     }
#
#     r = requests.get(url=url, headers=headers)
#     # запись запроса в файл
#     with open("index2.html", "w", encoding="UTF-16") as file:
#         file.write(r.text)
#
# def main():
#     get_data("https://tury.ru/hotel/")
#
# if __name__ == '__main__':
#     main()



# КОД 2 - прочитать сохраненную на пк html-страницу, выбрать и вывести ссылки отелей
# прочитать страницу.html с ПК
# with open("index.html", encoding="utf-16") as file:
#     src = file.read()
#
# # объект супа, "lxml" - парсер
# soup = BeautifulSoup(src, "lxml")
#
# # найти все теги определенного класса со стр-цы
# all_hotels = soup.find_all(class_="reviews-info__item")
#
# for hotel in all_hotels:
#     hotel_url = hotel.get("href")
#
#     print(hotel_url)


# КОД 3 сохранить код html с сайта при помощи selenium и WebDriver
def get_data_with_selenium(url):
    # создать объект опций запуска через Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)

    try:
        driver.get(url=url)
        time.sleep(5)

        with open("index_selenium.html", "w", encoding='utf-16') as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_data_with_selenium("https://tury.ru/hotel/")


if __name__ == '__main__':
    main()
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_data(url):
    headers = {
        "Accept": "text/html, application/xhtml+xml, application/xml; q = 0.9, image/avif, image/webp, image/apng,"
                  " */*; q=0.8, application/signed-exchange;v = b3;q = 0.9",
        "Accept-encoding": "gzip, deflate",
        "Accept - language": "en",
        "Cache-controlA": "max-age=0",
        "Connection": "keep-alive",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36(KHTML, like Gecko)" \
                      "Chrome/108.0.0.0 Mobile Safari/537.36"
    }

    r = requests.get(url=url, headers=headers)

    with open("index.html", "w", encoding="UTF-16") as file:
        file.write(r.text)

# def main():
    get_data("https://tury.ru/hotel/?cat=1317")

# if __name__ == '__main__':
    main()


# прочитать страницу.html с ПК
# with open("index.html", encoding="utf-16") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")      # объект супа, "lxml" - парсер
# all_hotels = soup.find_all(class_="reviews-info__item")   # найти все теги определенного класса со стр-цы
#
# for hotel in all_hotels:
#     hotel_url = hotel.get("href")
#
#     print(hotel_url)

def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0")

    try:
        driver = webdriver.Firefox(
            executable_path="D:\pythonProject\scraping\hotels_first_selenium\geckodriver.exe",
            options=options
        )
        driver.get(url=url)
        time.sleep(5)

        with open("index_selenium.html", "w") as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_data_with_selenium("https://tury.ru/hotel/?cat=1317")


if __name__ == '__main__':
    main()





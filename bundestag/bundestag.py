"""
Задача - спарсить данные с сайта немецкого Бундестага, а именно забрать информацию о всех членах парламента,
в том числе ссылки на социальные сети
"""
import json
import random
from time import sleep
import requests
from bs4 import BeautifulSoup

# persons_url_list = []
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
}

# проходим по разделу сайта, где выводится по 20 депутатов
# for i in range(0, 740, 20):
#     url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}"
#     q = requests.get(url, headers)
#     result = q.content

#     создаем объект суп, парсим
#     soup = BeautifulSoup(result, 'lxml')

#     находим класс с ссылками
#     persons = soup.find_all('a')

#     извлекаем ссылки и добавляем в список
#     for person in persons:
#         person_page_url = person.get('href')
#         persons_url_list.append(person_page_url)
#         sleep(random.randrange(2, 4))

# записываем все ссылки на каждого из 740 депутатов в файл
# with open('persons_url_list.txt', 'w') as file:
#     for line in persons_url_list:
#         file.write(f"{line}\n")


# открываем для дальнейшей работы наш ранее сохраненный файл
with open('persons_url_list.txt') as file:

    lines = [line.strip() for line in file.readlines()]  # при помощи списк.включения формируем список со всеми ссылками

    data_dict = []
    count = 0


    for line in lines:      # перебираем список, парсим, находим класс
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, "lxml")
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1]

        social_networks = soup.find_all(class_='bt-link-extern')

        social_networks_urls = []
        for item in social_networks:
            social_networks_urls.append(item.get('href'))

        data = {
            'person_name': person_name,
            'person_company': person_company,
            'social_networks': social_networks_urls
        }
        count += 1
        print(f"#{count}: {line} is done!")

        data_dict.append(data)

        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file, indent=4)

        # sleep(1)



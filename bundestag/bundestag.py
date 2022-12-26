"""
Задача - спарсить данные с сайта немецкого Бундестага, а именно забрать информацию о всех членах парламента,
в том числе ссылки на социальные сети
"""

import random
from time import sleep
import requests
from bs4 import BeautifulSoup

persons_url_list = []

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
}


for i in range(0, 740, 20):
    url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}"

    q = requests.get(url, headers)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')
    persons = soup.find_all('a')

    for person in persons:
        person_page_url = person.get('href')
        print(person_page_url)

        persons_url_list.append(person_page_url)

        sleep(random.randrange(2, 4))


# with open('persons_url_list.txt', 'w') as file:
#     for line in persons_url_list:
#         file.write(f"{line}\n")



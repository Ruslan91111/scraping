"""   Онлайн каталог Cosmopolitan спарсить фотоизображения формата .jpg и конвертировать в 1 PDF файл  """

# import os
# from bs4 import BeautifulSoup

import img2pdf    # библиотека для конвертации .jpg в .PDF
import requests



def get_data():
    """ Функция сохраняет файлы формата .jpg с сайта онлайн каталога, в дальнейшем сохраняет в формате PDF """

    headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
    }

    img_list = []
    for i in range(1, 10):
        url = f"https://catalog-n.com/images/cosmopolitan/0/cosmopolitan-4-2022-00{i}.jpg"
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f"media/{i}.jpg", "wb") as file:
            file.write(response)
            print(f"Downloaded {i} of 10")
            img_list.append(f"media/{i}.jpg")

    print('*' * 20)
    print(img_list)

    # создание единного PDF-файла
    with open("img_catalog.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF файл создан")


def write_to_pdf_from_directory():
    """ Функция выбирает изображения формата .jpg из директории на ПК и конвертирует их в единный файл формата .PDF"""
    # print(os.listdir("media"))
    img_list = [f"media/{i}.jpg" for i in range(1, 10)]

    # создание PDF-файла
    with open("img_catalog.pdf", "wb") as f:
        f.write(img2pdf.convert(img_list))

    print("PDF файл создан")


def main():
    write_to_pdf_from_directory()


if __name__ == '__main__':
    main()







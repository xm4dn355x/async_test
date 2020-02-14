#
#   Общие функции для всех парсеров
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from time import sleep
import requests


def get_htmls(urls):
    """
        Получает список URL-адресов
        Возвращает список из всех полученных HTML документов

        :param urls: Список URL-адресов
        :type urls: list
        :return: Возвращаем список HTML-документов
    """
    htmls = []  # Готовим болванку для возвращаемого значения
    for url in urls:  # Прогоняем все URL из списка
        html = get_html(url)  # Получаем HTML по полученному URL из списка
        htmls.append(html)  # Добавляем полученный HTML в возвращаемый список
        sleep(1)
    return htmls  # Возвращаем список в котором каждый элемент - это HTML документ


def get_html(url):
    """
        Получает URL-адрес
        Возвращает тело HTML документа

        :param url: URL-адрес
        :type url: str
        :return: Возвращаем HTML-документ
    """
    print(f"""get_html url={url}""")
    r = requests.get(url, headers={'User-Agent': 'Custom'})  # Создаем объект web-страницы по полученному url
    print(r)  # Ответ от сервера <Response [200]>
    return r.text  # Возвращаем тело HTML документа


if __name__ == '__main__':
    pass
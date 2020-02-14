#
#   Девятнадцатый простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNSuVf0JNKeklWEL1AwL3jkap2bGFw%3A1581685026466&ei=I' \
      'plGXv77G-TnrgTDtKXAAw&q=python+popen&oq=python+pope&gs_l=psy-ab.3.0.0i20i263j0l9.43501.49812..51212...2.2..0.' \
      '167.897.0j7......0....1..gws-wiz.......0i71j35i39j0i67j0i131i67j0i131.yrBhVFvuqps'


def parse_nineteenth():
    return get_pages_data(get_htmls(get_urls(URL)))


def get_urls(url):
    res = []
    for i in range(10):
        res.append(url)
    return res


def get_pages_data(htmls):
    """
        Получает список HTML документов
        Возвращает список словарей с спарсенными данными со страниц

        :param htmls: список HTML документов
        :type htmls: list of str
        :return: list of str с данными спарсенными со страниц
    """
    data = []  # Создаем болванку для возвращаемого значения
    for html in htmls:  # Прогоняем каждый HTML из списка и достаем данные из него
        page_data = get_page_data(html)  # Получаем список c данными в HTML документе
        for pd in page_data:  # Проходимся по каждому элементу списка
            data.append(pd)  # Добавляем словарь в список с данными на return
    return data  # список со всеми спаренными данными из полученного списка HTML документов


def get_page_data(html):
    """
        Получает HTML документ, парсит его, и находит заголовки поисковой выдачи

        :param html: HTML документ
        :type html: str
        :return: list of str
    """
    res = []
    soup = BeautifulSoup(html, 'lxml')  # Создаем объект супа
    raw_titles = soup.find_all('div', 'BNeawe vvjwJb AP7Wnd')  # находит заголовки поисковой выдачи
    for raw in raw_titles:
        res.append(raw.text)
    return res


if __name__ == '__main__':
    # print(get_html(URL))
    print(parse_first())

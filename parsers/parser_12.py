#
#   Двенадцатый простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNTicbqMc0s6oAC31XkjX6XlL2w8-w%3A1581684590430&ei=bp' \
      'dGXrbkGcXLrgTJrrnADA&q=%D0%B0%D1%81%D1%82%D0%B0%D0%BD%D0%B0%D0%B2%D0%B8%D1%82%D0%B5%D1%81%D1%8C+%D0%BC%D0%B5%D' \
      '0%BC&oq=%D0%B0%D1%81%D1%82%D0%B0%D0%BD%D0%B0%D0%B2%D0%B8%D1%82%D0%B5%D1%81%D1%8C&gs_l=psy-ab.3.1.0l10.63205.86' \
      '605..87868...17.1..0.147.3375.0j28......0....1..gws-wiz.....10..0i71j35i39j0i131j0i67j0i131i67j0i20i263j0i70i2' \
      '55j0i22i30j35i362i39j0i67i70i249j0i10.D75M0gVdSEo'


def parse_twelfth():
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

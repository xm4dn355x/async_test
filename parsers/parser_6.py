#
#   Шестой простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from .parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNTaPvKhLhb6kkgP-lCya1f1sCt8AA%3A1581684040010&ei=SJ' \
      'VGXuUPoq2uBN3yt6gI&q=%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C+%D0%B3%D1%83%D0%B3%D0%BB+%D1%85%D1%80%D0%BE%D0' \
      '%BC+%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE+%D0%B8+%D0%B1%D0%B5%D0%B7+%D1%80%D0%B5%D0%B3%D0%B8%' \
      'D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8+%D0%BD%D0%B0+%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC+%D1%8F%D0%B7' \
      '%D1%8B%D0%BA%D0%B5&oq=%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C+%D0%B3%D1%83%D0%B3+%D1%85%D0%BB%D0%BE%D0%BC+%' \
      'D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE+%D0%B8+%D0%B1%D0%B5%D0%B7+%D1%80%D0%B5&gs_l=psy-ab.3.0.0' \
      'i13j0i22i30l9.48249.55351..56287...0.4..0.207.5080.0j34j1......0....1..gws-wiz.......0i71j35i39j0i20i263j0i67j' \
      '0i131j0j0i10j0i22i10i30j0i13i30j0i8i13i30.hrxpnOQWGfU'


def parse_sixth():
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

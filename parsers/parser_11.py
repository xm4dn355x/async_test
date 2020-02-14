#
#   Одиннадцатый простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from .parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNRDicu0wUZBrWgJvRNyC5BhbbT0Gw%3A1581684497703&ei=EZ' \
      'dGXt2_KsXJrgSY8qhI&q=%D1%85%D0%B2%D0%B0%D1%82%D0%B8%D1%82+%D1%8D%D1%82%D0%BE+%D1%82%D0%B5%D1%80%D0%BF%D0%B5%D1' \
      '%82%D1%8C&oq=%D1%85%D0%B2%D0%B0%D1%82%D0%B8%D1%82+&gs_l=psy-ab.3.0.0l10.89255.90015..91894...0.1..0.162.936.0j' \
      '7......0....1..gws-wiz.......0i71j35i39j0i131.Rzuzu0iaqys'


def parse_eleventh():
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

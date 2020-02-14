#
#   Четырнадцатый простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from .parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNQuXwWtBYhDIDQqYNwIJjJXKzc0vA%3A1581684725876&ei=9ZdGXpWLNeOkrgTb6I7oAQ&q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD+%D0%B2+%D0%BA%D0%B0%D1%80%D0%BC%D0%B0%D0%BD&oq=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD+%D0%B2+%D0%BA%D0%B0%D1%80%D0%BC%D0%B0%D0%BD&gs_l=psy-ab.3..33i22i29i30.44753.74899..75659...0.1..0.139.3630.0j30......0....1..gws-wiz.......0i71j35i39j0j0i131j0i67j0i131i67j0i22i30j0i22i10i30j0i70i255.Uqv7MwIJSQg&ved=0ahUKEwjV2e3hitHnAhVjkosKHVu0Ax0Q4dUDCAs&uact=5'


def parse_fourteenth():
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

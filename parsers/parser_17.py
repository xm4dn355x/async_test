#
#   Семнадцатый простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNQDN7oUsJMZ10_EdMWMCHcY_5fzxQ%3A1581684931900&ei=w5hGXpq3NuqGrwSOo6SoAQ&q=%D0%BD%D0%B5%D1%82+%D0%BC%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B0%D1%8F+%D0%B6%D0%B8%D1%80%D0%BD%D0%B0%D1%8F+%D0%B6%D0%BE%D0%BF%D0%B0&oq=%D0%BD%D0%B5%D1%82+%D0%BC%D0%B0%D0%BB%D0%B5%D0%BD%D1%8C%D0%BA%D0%B0%D1%8F+%D0%B6%D0%B8%D1%80%D0%BD%D0%B0%D1%8F+%D0%B6%D0%BE%D0%BF%D0%B0&gs_l=psy-ab.3...43468.48628..48812...0.1..0.132.1543.0j13......0....1..gws-wiz.......0i71j35i39j0j0i131j0i67j0i20i263j0i10j0i22i30.5GvP2utCGhg&ved=0ahUKEwjapIzEi9HnAhVqw4sKHY4RCRUQ4dUDCAs&uact=5'


def parse_seventeenth():
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

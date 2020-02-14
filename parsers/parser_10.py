#
#   Десятый простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNQOIfLLP2bVQCZU2YgvdIRwKrq-mg%3A1581684422340&ei=x' \
      'pZGXs6ZFOjKrgSno6DYCA&q=%D0%BC%D0%BE%D0%B5+%D1%83%D0%B2%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5&oq=vjt+edj&gs_l=p' \
      'sy-ab.3.0.0i10i1i42j0i10i203.68846.73036..74084...6.1..0.231.1211.0j8j1......0....1..gws-wiz.....10..0i71j35i' \
      '39j0i131j0i10i1j0j0i10j35i362i39j0i10i42j0i10i203i42j0i203j0i22i10i30j0i22i30.MC3lBG2olH8'


def parse_tenth():
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

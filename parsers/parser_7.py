#
#   Седьмой простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNQ4OMzRKxQcP7MkgRt0XCEj-zKakA%3A1581684097137&ei=gZVGXuH7B8zLrgSIwLmgCg&q=%D0%BA%D0%B0%D0%BA+%D0%BF%D0%BE%D0%B4%D0%BD%D1%8F%D1%82%D1%8C+%D0%B1%D0%B0%D0%B1%D0%BB%D0%B0&oq=rfr+gjlyznm+%2Cf%2C&gs_l=psy-ab.3.0.0i1l10.132716.139163..140579...1.4..0.252.1978.0j14j1......0....1..gws-wiz.....10..0i71j35i362i39j35i39j0j0i131j0i10i1i67j0i67j0i10i67j0i10i1j0i10j0i10i42j0i10i203j0i10i1i42.06gRFOKKtiE'


def parse_seventh():
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

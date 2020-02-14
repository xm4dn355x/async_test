#
#   Пятый простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from .parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNRbqGyOkBxq2OcBqi86rFEsTGoq0Q%3A1581684034104&ei=Qp' \
      'VGXuHiBYT5qwG6prLQAw&q=%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C+%D1%82%D1%83%D1%85%D0%BB%D1%8B%D0%B5+%D0%BA%D0%BE%' \
      'D0%BD%D1%81%D0%B5%D1%80%D0%B2%D1%8B&oq=%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C+%D1%82%D1%83%D1%85%D0%BB%D1%8B%D0%' \
      'B5+%D0%BA%D0%BE%D0%BD%D1%81%D0%B5%D1%80%D0%B2%D1%8B&gs_l=psy-ab.3...2842.4643..5081...0.2..0.169.911.0j7......' \
      '0....1..gws-wiz.......0i71j35i39j0j0i7i30j0i8i7i30.9iNsaVhBCmY&ved=0ahUKEwjhi_-XiNHnAhWE_CoKHTqTDDoQ4dUDCAs&ua' \
      'ct=5'


def parse_fifth():
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

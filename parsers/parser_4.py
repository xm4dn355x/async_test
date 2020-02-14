#
#   Четвертый простой парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from .parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNTBd3AWeI0KOtMi2cJjzmT_9GZQ-Q%3A1581683369170&ei=qZ' \
      'JGXuL7CYyJrwT6_7u4Ag&q=%D1%80%D0%B8%D0%BA%D0%BE%D0%BD+%D0%B3%D0%B0%D0%B2%D0%BD%D0%BE&oq=%D1%80%D0%B8%D0%BA%D0%' \
      'BE%D0%BD+%D0%B3%D0%B0%D0%B2%D0%BD%D0%BE&gs_l=psy-ab.3...79165.82355..82802...0.0..0.128.1494.0j13......0....1.' \
      '.gws-wiz.......35i39j0j0i131j0i67j0i131i67j0i10j0i22i30j0i22i10i30j33i160.ksa17P6RUOY&ved=0ahUKEwii9PbahdHnAhW' \
      'MxIsKHfr_DicQ4dUDCAs&uact=5'


def parse_fourth():
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

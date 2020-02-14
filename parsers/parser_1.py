#
#   Первый парсер для тестирования скорости работы.
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from bs4 import BeautifulSoup
from parsers_base import get_htmls, get_html

URL = 'https://www.google.com/search?newwindow=1&hl=ru&sxsrf=ACYBGNSXe1h4xMmCx1DCsoez3C_-NS5Otg%3A1581667945103&ei=a' \
      'VZGXqbjBe2xrgTyi4LwBg&q=%D1%87%D1%82%D0%BE+%D0%B1%D1%83%D0%B4%D0%B5%D1%82+%D0%B5%D1%81%D0%BB%D0%B8+%D0%BD%D0%' \
      'B5+%D1%81%D0%BF%D0%B0%D1%82%D1%8C&oq=%D1%87%D1%82%D0%BE+%D0%B1%D1%83%D0%B4%D0%B5%D1%82+%D0%B5%D1%81%D0%BB%D0%' \
      'B8+%D0%BD%D0%B5&gs_l=psy-ab.3.2.0l10.11030.20883..23194...8.1..0.359.3177.0j22j1j1......0....1..gws-wiz.....1' \
      '0..0i71j35i362i39j35i39j0i131j0i67.AbzvA9VEf6k'

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
    print(get_pages_data(get_htmls(get_urls(URL))))

#
#   main.py файл сравнения производительности с обычным линейным вызовом парсеров.
#   Блокирующий, отвратительный, но работает :)
#
#   Автор: Никитенко Михаил
#   Лицензия: MIT License
#

from datetime import datetime
from parsers.parser_1 import parse_first
from parsers.parser_2 import parse_second
from parsers.parser_3 import parse_third
from parsers.parser_4 import parse_fourth
from parsers.parser_5 import parse_fifth
from parsers.parser_6 import parse_sixth
from parsers.parser_7 import parse_seventh
from parsers.parser_8 import parse_eighth
from parsers.parser_9 import parse_nineth
from parsers.parser_10 import parse_tenth
from parsers.parser_11 import parse_eleventh
from parsers.parser_12 import parse_twelfth
from parsers.parser_13 import parse_thirteenth
from parsers.parser_14 import parse_fourteenth
from parsers.parser_15 import parse_fifteenth
from parsers.parser_16 import parse_sixteenth
from parsers.parser_17 import  parse_seventeenth
from parsers.parser_18 import parse_eighteenth
from parsers.parser_19 import parse_nineteenth
from parsers.parser_20 import parse_twentieth


if __name__ == '__main__':
    start_time = datetime.now()
    print(f'Начало работы парсера : {start_time}')
    parsed = []
    parsed.append(parse_first())
    parsed.append(parse_second())
    parsed.append(parse_third())
    parsed.append(parse_fourth())
    parsed.append(parse_fifth())
    parsed.append(parse_sixth())
    parsed.append(parse_seventh())
    parsed.append(parse_eighth())
    parsed.append(parse_nineth())
    parsed.append(parse_tenth())
    parsed.append(parse_eleventh())
    parsed.append(parse_twelfth())
    parsed.append(parse_thirteenth())
    parsed.append(parse_fourteenth())
    parsed.append(parse_fifteenth())
    parsed.append(parse_sixteenth())
    parsed.append(parse_seventeenth())
    parsed.append(parse_eighteenth())
    parsed.append(parse_nineteenth())
    parsed.append(parse_twentieth())
    print(parsed)
    time_delta = datetime.now() - start_time
    print(f'Потраченное на парсинг время: {time_delta}')
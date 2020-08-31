# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as ch1_r1, room2 as ch1_r2
from district.central_street.house2 import room1 as ch2_r1, room2 as ch2_r2
from district.soviet_street.house1 import room1 as sh1_r1, room2 as sh1_r2
from district.soviet_street.house2 import room1 as sh2_r1, room2 as sh2_r2

str_tabulate = ", "
str_total = "На районе живут: "

# help_list.extend(ch1_r1.folks)
# help_list.extend(ch1_r2.folks)
# help_list.extend(ch2_r1.folks)
# help_list.extend(ch2_r2.folks)
# help_list.extend(sh1_r1.folks)h
# help_list.extend(sh1_r2.folks)
# help_list.extend(sh2_r1.folks)
# help_list.extend(sh2_r2.folks)

help_list = (ch1_r1.folks + ch1_r2.folks + ch2_r1.folks + ch2_r2.folks + sh1_r1.folks + sh1_r2.folks + sh2_r1.folks +
             sh2_r2.folks)

# Посмотрите, что мне написали во втором модуле:
# У списков есть специальный метод для расширения его
#  элементами других коллекций. Использовать сложение двух
#  списков можно, но в этом случае создаётся новый список,
#  содержащий элементы списков zoo и birds, и заменяет
#  существующий. Это менее оптимально.

str_total += str_tabulate.join(help_list)

print(str_total)

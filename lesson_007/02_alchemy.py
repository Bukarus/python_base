# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
class Air:
    def __init__(self):
        self.name = "Воздух"

    def __add__(self, other):
        if other == "Вода":
            my_storm = Storm()
            return my_storm
        elif other.name == "Огонь":
            my_thunder = Thunder()
            return my_thunder
        elif other.name == "Земля":
            my_dust = Dust()
            return my_dust
        else:
            return None

    def __str__(self):
        print(self.name)


class Water:
    def __init__(self):
        self.name = "Вода"

    def __add__(self, other):
        if other.name == "Воздух":
            my_storm = Storm()
            return my_storm
        elif other.name == "Огонь":
            my_steam = Steam()
            return my_steam
        elif other.name == "Земля":
            my_dirt = Dirt()
            return my_dirt
        else:
            return None

    def __str__(self):
        print(self.name)


class Fire:
    def __init__(self):
        self.name = "Огонь"

    def __add__(self, other):
        if other.name == "Воздух":
            my_thunder = Thunder()
            return my_thunder
        elif other.name == "Вода":
            my_steam = Steam()
            return my_steam
        elif other.name == "Земля":
            my_lava = Lava()
            return my_lava
        else:
            return None

    def __str__(self):
        print(self.name)

class Earth:
    def __init__(self):
        self.name = "Земля"

    def __add__(self, other):
        if other.name == "Воздух":
            my_dust = Dust()
            return my_dust
        elif other.name == "Вода":
            my_dirt = Dirt()
            return my_dirt
        elif other.name == "Огонь":
            my_lava = Lava()
            return my_lava
        else:
            return None

    def __str__(self):
        print(self.name)


class Lava:
    def __init__(self):
        self.name = "Лава"

    def __str__(self):
        print(self.name)

class Dust:
    def __init__(self):
        self.name = "Пыль"

    def __str__(self):
        print(self.name)

class Dirt:
    def __init__(self):
        self.name = "Грязь"

    def __str__(self):
        print(self.name)

class Steam:
    def __init__(self):
        self.name = "Пар"

    def __str__(self):
        print(self.name)

class Storm:
    def __init__(self):
        self.name = "Шторм"

    def __str__(self):
        print(self.name)

class Thunder:
    def __init__(self):
        self.name = "Молния"

    def __str__(self):
        print(self.name)

Water
print(Water() + Air())
# print(Fire(), '+', Air(), '=', Fire() + Air())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

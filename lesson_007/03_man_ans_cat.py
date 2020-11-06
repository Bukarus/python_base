# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.wiskas < 10:
            self.buy_whiskas()
        elif self.house.dirt >= 100:
            if self.fullness >= 30:
                self.clean_house()
            else:
                self.eat()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()

    def take_a_cat(self, cat):
        cat.house = self.house
        cprint('{} взял кота'.format(self.name), color='green')

    def buy_whiskas(self):
        self.house.wiskas += 50
        self.house.money -= 50
        cprint('{} купил кошачего корма'.format(self.name), color='magenta')

    def clean_house(self):
        self.house.dirt -= 100
        self.fullness -= 20
        cprint('{} затеял уборку'.format(self.name), color='blue')


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.wiskas = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, вискаса осталось {}, грязи {}'.format(
            self.food, self.money, self.wiskas, self.dirt
        )


# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня
class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - кот {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def sleep(self):
        self.fullness -= 10
        cprint('кот {} поспал'.format(self.name), color='yellow')

    def eat(self):
        self.fullness += 20
        self.house.food -= 10
        cprint('кот {} поел'.format(self.name), color='green')

    def tear_up_wallpapers(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('кот {} ободрал обои'.format(self.name), color='yellow')

    def act(self):
        if self.fullness <= 0:
            cprint('кот {} умер...'.format(self.name), color='red')
            return

        if self.fullness < 20:
            self.eat()
        elif self.fullness > 40:
            self.sleep()
        else:
            self.tear_up_wallpapers()


# my_cat = Cat(name="Мурзик")
# print(my_cat)
my_sweet_home = House()
my_man = Man('Бивис')
pretty_cat = Cat('Барсик')
my_man.go_to_the_house(my_sweet_home)
my_man.take_a_cat(pretty_cat)

for day in range(1, 366):
    print('================ день {} =================='.format(day))

    my_man.act()
    pretty_cat.act()
    print('--- в конце дня ---')

    print(my_man)
    print(pretty_cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

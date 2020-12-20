# -*- coding: utf-8 -*-

from termcolor import cprint


# from random import randint


# Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

# Часть вторая
#
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в                                                                  начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов
# ######################################################## Часть вторая бис
# #
# # После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
# #
# # Ребенок может:
# #   есть,
# #   спать,
# #
# # отличия от взрослых - кушает максимум 10 единиц еды,
# # степень счастья  - не меняется, всегда ==100 ;)
#
# ######################################################## Часть третья
# #
# # после подтверждения учителем второй части (обоих веток)
# # влить в мастер все коммиты из ветки develop и разрешить все конфликты
# # отправить на проверку учителем.

class House:

    def __init__(self):
        self.quantity_of_money = 100
        self.amount_of_food = 50
        self.amount_of_dirt = 0
        self.cat_food = 30

    def __str__(self):
        # super(House, self).__str__()
        #  Не нужно оставлять код с таким большим отступом. Переносите
        #  аргументы на новую строку. Так код будет более читаемым.
        return "Денег в тумбочке - {}, еды в холодильнике - {}, грязи - {}, кошачей еды - {}".format(
            self.quantity_of_money, self.amount_of_food, self.amount_of_dirt, self.cat_food
        )


class Human:

    def __init__(self, name, house=None):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = house
        self.food_eaten = 0

    def __str__(self):
        return 'Имя - {}, сытость - {}, счастье - {}'.format(self.name, self.fullness, self.happiness)

    def act(self):
        if self.fullness <= 20:
            self.eat()
            return False
        elif self.fullness == 0:
            cprint('{} умер'.format(self.name), color='magenta')
        elif self.happiness < 10:
            cprint('{} умер'.format(self.name), color='magenta')
        elif self.happiness <= 15:
            self.pet_the_cat()
            return False

        if self.house.amount_of_dirt >= 90:
            self.happiness -= 10

        return True

    def eat(self):
        self.fullness += 30
        self.house.amount_of_food -= 30
        self.food_eaten += 30

    def pet_the_cat(self):
        self.happiness += 5


class Husband(Human):

    def __init__(self, name, house=None):
        super().__init__(name, house)
        self.money_earned = 0

    def act(self):
        if super().act():
            if self.happiness <= 10:
                self.gaming()
            elif self.house.quantity_of_money <= 20:
                self.work()
            else:
                self.work()

    # def eat(self):
    #     super().eat()

    def work(self):
        self.fullness -= 10
        self.house.quantity_of_money += 150
        self.money_earned += 150

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20


class Wife(Human):

    def __init__(self, name, house=None):
        super().__init__(name, house)
        self.purchased_fur_coats = 0
        self.total_amount_of_cat_food = 30

    def act(self):
        self.house.amount_of_dirt += 5
        if super().act():
            if self.happiness <= 15 and self.house.quantity_of_money >= 500:
                self.buy_fur_coat()
            elif self.house.amount_of_food <= 80:
                self.shopping()
            elif self.house.cat_food <= 40:
                self.shopping()
            elif self.house.amount_of_dirt >= 90:
                self.clean_house()

    def shopping(self):
        self.fullness -= 10
        self.house.amount_of_food += 60
        self.house.quantity_of_money -= 60
        if self.house.cat_food <= 20:
            self.house.cat_food += 40
            self.house.quantity_of_money -= 40
            self.total_amount_of_cat_food += 40

    def buy_fur_coat(self):
        self.fullness -= 10
        self.house.quantity_of_money -= 350
        self.happiness += 60
        self.purchased_fur_coats += 1

    def clean_house(self):
        self.fullness -= 10
        if self.house.amount_of_dirt >= 100:
            self.house.amount_of_dirt -= 100
        else:
            self.house.amount_of_dirt = 0


class Cat:

    def __init__(self, name, house=None):
        self.name = name
        self.fullness = 30
        self.house = house

    def act(self):
        if self.fullness <= 0:
            print('Кот {} умер от голода'.format(self.name))
        elif self.fullness >= 30:
            self.soil()
        elif 20 <= self.fullness < 30:
            self.sleep()
        else:
            self.eat()

    def eat(self):
        if self.house.cat_food >= 10:
            self.house.cat_food -= 10
            self.fullness += 20
        else:
            self.sleep()

    def sleep(self):
        self.fullness -= 10

    def soil(self):
        self.fullness -= 10
        self.house.amount_of_dirt += 5

    def __str__(self):
        return 'кот - {}, сытость - {}'.format(self.name, self.fullness)


class Child(Human):

    # def __init__(self, name, house=None):
    #     super(Child, self).__init__(name=name, house=house)

    # def __str__(self):
    #     return super().__str__()

    def act(self):
        if self.fullness <= 10:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        self.fullness += 10
        self.house.amount_of_food -= 10
        self.food_eaten += 10

    def sleep(self):
        self.fullness -= 10


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)
murka = Cat(name='Мурка', house=home)

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    murka.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')
    cprint(murka, color='cyan')
    cprint(home, color='cyan')

print(home)
print('За год заработано - {}, еды съедено - {}, шуб куплено - {}, вискаса закуплено - {} единиц'.format(
    serge.money_earned, serge.food_eaten, masha.purchased_fur_coats, masha.total_amount_of_cat_food
))

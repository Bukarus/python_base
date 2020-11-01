# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    pass

    def __init__(self):
        self.x = sd.random_number(0, sd.resolution[0])
        self.y = 700
        self.length = sd.random_number(5, 15)
        self.factor_a = sd.random_number(1, 8) / 10
        self.factor_b = sd.random_number(1, 8) / 10
        self.factor_c = sd.random_number(30, 60)
        self.speed = sd.random_number(5, 10)

    def move(self):
        self.x += sd.random_number(-15, 15)
        self.y -= self.speed

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, factor_a=self.factor_a, factor_b=self.factor_b,
                     factor_c=self.factor_c, color=sd.COLOR_WHITE)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, factor_a=self.factor_a, factor_b=self.factor_b,
                     factor_c=self.factor_c, color=sd.background_color)

    def can_fall(self):
        return self.y >= 10


# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
sd.resolution = (1200, 600)
N = 100


def get_flakes(count=N):
    my_list = list()
    for _ in range(count):
        new_flake = Snowflake()
        my_list.append(new_flake)
    return my_list


def get_fallen_flakes():
    global flakes
    number_fallen_flakes = 0
    for a_flake in flakes:
        if not a_flake.can_fall():
            flakes.remove(a_flake)
            number_fallen_flakes += 1
    return number_fallen_flakes


def append_flakes(count):
    global flakes
    for _ in range(count):
        new_flake = Snowflake()
        flakes.append(new_flake)


flakes = get_flakes(count=N)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

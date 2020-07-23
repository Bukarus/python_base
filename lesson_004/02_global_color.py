# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

COLOR_RED = sd.COLOR_RED
COLOR_ORANGE = sd.COLOR_ORANGE
COLOR_YELLOW = sd.COLOR_YELLOW
COLOR_GREEN = sd.COLOR_GREEN
COLOR_CYAN = sd.COLOR_CYAN
COLOR_BLUE = sd.COLOR_BLUE
COLOR_PURPLE = sd.COLOR_PURPLE


colors = {
    0: COLOR_RED,
    1: COLOR_ORANGE,
    2: COLOR_YELLOW,
    3: COLOR_GREEN,
    4: COLOR_CYAN,
    5: COLOR_BLUE,
    6: COLOR_PURPLE,
}

color_names = {
    0: 'red',
    1: 'orange',
    2: 'yellow',
    3: 'green',
    4: 'cyan',
    5: 'blue',
    6: 'purple',
}


point_initial_triangle = sd.get_point(100, 300)
point_initial_square = sd.get_point(300, 150)
point_initial_pentagon = sd.get_point(500, 300)
point_initial_hexagon = sd.get_point(150, 400)
length_initial = 100
angle_initial = 60
user_color = COLOR_YELLOW


def triangle(point=point_initial_triangle, angle=angle_initial, length=length_initial, color=user_color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw(color=color)


def square(point=point_initial_square, angle=angle_initial, length=length_initial, color=user_color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw(color=color)

    sd.line(start_point=v3.end_point, end_point=v1.start_point, width=3, color=color)


def pentagon(point=point_initial_pentagon, angle=angle_initial, length=length_initial, color=user_color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw(color=color)


def hexagon(point=point_initial_hexagon, angle=angle_initial, length=length_initial, color=user_color):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=color)

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw(color=color)

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw(color=color)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw(color=color)

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw(color=color)

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw(color=color)


print('Возможные цвета: ')
for color_name in color_names:
    print("{}: {}".format(color_name, color_names[color_name]))
# print('0: red')
# print('1: orange')
# print('2: yellow')
# print('3: green')
# print('4: cyan')
# print('5: blue')
# print('6: puple')

user_input = input("Введите, пожалуйста, желаемый цвет: ")
user_color = int(user_input)

while user_color in colors:
    triangle(color=colors[user_color])
    square(color=colors[user_color])
    pentagon(color=colors[user_color])
    hexagon(color=colors[user_color])
    # sd.pause()
    user_input = input("Введите, пожалуйста, желаемый цвет: ")
    user_color = int(user_input)
else:
    print("Вы ввели некорректный номер!")

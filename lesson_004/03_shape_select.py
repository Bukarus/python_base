# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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


point_initial_triangle = sd.get_point(300, 300)
point_initial_square = sd.get_point(300, 300)
point_initial_pentagon = sd.get_point(300, 300)
point_initial_hexagon = sd.get_point(300, 300)
length_initial = 100
angle_initial = 60
user_color = COLOR_YELLOW


# TODO Нужно разместить функции над остальным кодом.
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


figures = {
    0: ["треугольник", triangle],
    1: ["квадрат", square],
    2: ["пятиугольник", pentagon],
    3: ["шестиугольник", hexagon],
}


print('Возможные фигуры: ')
for figure_item in figures:
    print("{}: {}".format(figure_item, figures[figure_item][0]))


user_input = input("Введите, пожалуйста, желаемую фигуру: ")
user_figure = int(user_input)
#
while user_figure in figures:
    sd.clear_screen()
    figures[user_figure][1]()
    user_input = input("Введите, пожалуйста, желаемую фигуру: ")
    user_figure = int(user_input)
else:
    print("Вы ввели некорректный номер!")
# sd.pause()

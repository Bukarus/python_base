# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
point_initial_triangle = sd.get_point(300, 300)
point_initial_square = sd.get_point(300, 300)
point_initial_pentagon = sd.get_point(300, 300)
point_initial_hexagon = sd.get_point(300, 300)
length_initial = 100
angle_initial = 60
user_color = sd.COLOR_YELLOW


def triangle(point=point_initial_triangle, angle=angle_initial, length=length_initial, color=user_color):
    number_of_angles = 3
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw(color=color)


def square(point=point_initial_square, angle=angle_initial, length=length_initial, color=user_color):
    number_of_angles = 4
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw(color=color)


def pentagon(point=point_initial_pentagon, angle=angle_initial, length=length_initial, color=user_color):
    number_of_angles = 5
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw(color=color)


def hexagon(point=point_initial_hexagon, angle=angle_initial, length=length_initial, color=user_color):
    number_of_angles = 6
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw(color=color)


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

while user_figure in figures:
    sd.clear_screen()
    figures[user_figure][1]()
    user_input = input("Введите, пожалуйста, желаемую фигуру: ")
    user_figure = int(user_input)
else:
    print("Вы ввели некорректный номер!")
# sd.pause()

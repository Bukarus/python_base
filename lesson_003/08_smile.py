# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x_coord=300, y_coord=300, color=simple_draw.COLOR_YELLOW):
    length_x = 100
    length_y = 100
    left_bottom = simple_draw.get_point(x_coord, y_coord)
    right_top = simple_draw.get_point(x_coord + length_x, y_coord + length_y)
    simple_draw.ellipse(left_bottom=left_bottom, right_top=right_top, color=color, width=1)
    center_point_eye1 = simple_draw.get_point(x_coord + 0.30 * length_x, y_coord + 0.70 * length_y)
    center_point_eye2 = simple_draw.get_point(x_coord + 0.70 * length_x, y_coord + 0.70 * length_y)
    simple_draw.circle(center_point_eye1, radius=10)
    simple_draw.circle(center_point_eye2, radius=10)
    point1 = simple_draw.get_point(x_coord + 0.10 * length_x, y_coord + 0.5 * length_y)
    point2 = simple_draw.get_point(x_coord + (3 / 8) * length_x, y_coord + 0.25 * length_y)
    point3 = simple_draw.get_point(x_coord + (5 / 8) * length_x, y_coord + 0.25 * length_y)
    point4 = simple_draw.get_point(x_coord + 0.90 * length_x, y_coord + 0.5 * length_y)
    point_list = [point1, point2, point3, point4]
    simple_draw.lines(point_list=point_list)


for _ in range(10):
    point = simple_draw.random_point()
    x_coord_range = point.x
    y_coord_range = point.y
    smile(x_coord=x_coord_range, y_coord=y_coord_range)

simple_draw.pause()

# Зачёт!

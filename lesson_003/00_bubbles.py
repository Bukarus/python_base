# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
radius_bubble = 50
point_bubble = sd.get_point(500, 450)
for _ in range(3):
    radius_bubble += 5
    sd.circle(center_position=point_bubble, radius=radius_bubble)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(center_position=sd.get_point(300, 450), color_of_circle=sd.COLOR_ORANGE, radius_of_circle=25,
           step_to_next=5):
    for _ in range(3):
        sd.circle(center_position=center_position, radius=radius_of_circle, color=color_of_circle)
        radius_of_circle += step_to_next


# пробный вызов функции
point1 = sd.get_point(500, 200)
bubble(center_position=point1, radius_of_circle=radius_bubble, color_of_circle=sd.COLOR_GREEN)
bubble()

# Нарисовать 10 пузырьков в ряд
y = 200
radius = 30
for x in range(650, 1151, 50):
    point = sd.get_point(x=x, y=y)
    color = sd.COLOR_WHITE
    bubble(center_position=point, color_of_circle=color, radius_of_circle=radius)

# Нарисовать три ряда по 10 пузырьков
for y in range(350, 501, 50):
    for x in range(650, 1151, 50):
        point = sd.get_point(x=x, y=y)
        bubble(center_position=point, step_to_next=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
sd.resolution = (330, 600)
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    radius = random.randint(10, 40)
    color = sd.random_color()
    bubble(center_position=point, color_of_circle=color, radius_of_circle=radius, step_to_next=step)

sd.pause()

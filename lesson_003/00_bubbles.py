# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
radius = 50
point = sd.get_point(500, 450)
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point=sd.get_point(300, 450), color=sd.COLOR_ORANGE, radius=25, step=5):
    for _ in range(3):
        sd.circle(center_position=point, radius=radius, color=color)
        radius += step

# пробный вызов функции
point = sd.get_point(500, 200)
bubble(point=point, radius=radius, color=sd.COLOR_GREEN)
bubble()

# Нарисовать 10 пузырьков в ряд
y = 200
radius = 30
for x in range(650, 1151, 50):
    point = sd.get_point(x=x, y=y)
    color = sd.COLOR_WHITE
    bubble(point=point, color=color, radius=radius)

# Нарисовать три ряда по 10 пузырьков
for y in range(350, 501, 50):
    for x in range(650, 1151, 50):
        point = sd.get_point(x=x, y=y)
        bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
sd.resolution = (330, 600)
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    radius = random.randint(10, 40)
    color = sd.random_color()
    bubble(point=point, color=color, radius=radius, step=step)

sd.pause()

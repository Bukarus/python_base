# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd

from landscape_animated.house import house_paint
from landscape_animated.snow import snowflow
from landscape_animated.sun import sun_paint
from landscape_animated.smile import smile
from landscape_animated.tree import draw_random_branches
from landscape_animated.rainbow import rainbow_paint

sd.resolution = (1200, 600)

# draw_random_branches()
initial_angle = 0
delta = 0
number_of_snowflakes = 100
snowflakes = {}
for i in range(number_of_snowflakes):
    snowflakes[i] = {}
    snowflakes[i]['x'] = sd.random_number(0, 300)
    snowflakes[i]['y'] = 700
    snowflakes[i]['length'] = sd.random_number(5, 15)
    snowflakes[i]['factor_a'] = sd.random_number(1, 8) / 10
    snowflakes[i]['factor_b'] = sd.random_number(1, 8) / 10
    snowflakes[i]['factor_c'] = sd.random_number(30, 60)
    snowflakes[i]['speed'] = sd.random_number(5, 20)
width_of_eye = 0
rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
root_point = sd.get_point(700, 30)

draw_random_branches(point=root_point)
while True:
    sd.start_drawing()
    delta = -15
    initial_angle += delta
    width_of_eye = 1 - width_of_eye
    last_color = rainbow_colors.pop(0)
    rainbow_colors.append(last_color)
    rainbow_paint(rainbow_colors=rainbow_colors)
    house_paint()
    sun_paint(angle_0=initial_angle, delta=delta)
    snowflow(snowflakes=snowflakes)
    smile(350, 50, width_of_eye=width_of_eye)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

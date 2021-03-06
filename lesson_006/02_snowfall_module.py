# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall as sn

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
sd.resolution = (1200, 600)

# создать_снежинки(N)
sn.make_snowflakes(sn.Number_of_snowflakes)

while True:
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    sn.paint_snowflake_with_color(color=sd.background_color)
    #  сдвинуть_снежинки()
    sn.move_snowflakes()
    #  нарисовать_снежинки_цветом(color)
    sn.paint_snowflake_with_color(color=sd.COLOR_WHITE)
    #  если есть номера_достигших_низа_экрана() то
    sn.list_of_bottoms = sn.list_of_bottom_snowflakes()
    if sn.list_of_bottoms:
        # print(sn.list_of_bottoms)
        #       удалить_снежинки(номера)
        sn.remove_list_of_bottoms(sn.list_of_bottoms)
        #       создать_снежинки(count)
        sn.make_snowflakes(len(sn.list_of_bottoms))
        sn.list_of_bottoms = []
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# Зачёт!

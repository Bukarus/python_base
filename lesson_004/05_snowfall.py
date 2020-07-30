# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 100

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snowflakes = {}
for i in range(N):
    snowflakes[i] = {}
    snowflakes[i]['x'] = sd.random_number(i * 12, (i + 1) * 12 - 12)
    snowflakes[i]['y'] = 700
    snowflakes[i]['length'] = sd.random_number(5, 15)
    snowflakes[i]['factor_a'] = sd.random_number(1, 8)/10
    snowflakes[i]['factor_b'] = sd.random_number(1, 8)/10
    snowflakes[i]['factor_c'] = sd.random_number(30, 60)
    snowflakes[i]['speed'] = sd.random_number(5, 20)

flag_of_stop = False

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл
while True:
    sd.start_drawing()
    for i, snowflake_item in snowflakes.items():
        point = sd.get_point(snowflake_item['x'], snowflake_item['y'])
        sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                     factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'],
                     color=sd.background_color)
        snowflake_item['y'] -= snowflake_item['speed']
        snowflake_item['x'] += sd.random_number(-15, 15)
        point = sd.get_point(snowflake_item['x'], snowflake_item['y'])
        sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                     factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'])
        if snowflake_item['y'] < 10:
            sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                         factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'])
            snowflake_item['y'] = 700
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

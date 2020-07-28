# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO Удобнее хранить координаты и параметры снежинок в одной структуре данных.
#  Так работать с ними будет проще:
#  список со списками:
#  snowflakes = [[0, 2, 4], [5, 6, 7], ...]
#  for x, y, length in snowflakes:
#      point = Point(x, y)
#      snowflake(point, length)
#  или список со словарями:
#  snowflakes = [{"x": 0, "y": 2, "length": 4}, {"x": 5, "y": 6, "length": 7}, ]
#  for snowflake in snowflakes:
#      point = Point(snowflake['x'], snowflake['y'])
#      snowflake(point, snowflake["length"])
#  или словарь со словарями:
#  snowflakes = {1: {"x": 0, "y": 2, "length": 4}, {"x": 5, "y": 6, "length": 7}, }
#  for i, snowflake in snowflakes.items():
#      point = Point(snowflake['x'], snowflake['y'])
#      snowflake(point, snowflake["length"])
#  Или с использованием enumerate, если нужен индекс элемента в списке:
#  for i, (x, y, length) in enumerate(snowflake_param):
#  Пример для словаря, содержащего список параметров снежинки:
#  for i, (x, y, length) in snowflake_param.items():
list_of_coords = []
list_of_length = []
factor_a_list = []
factor_b_list = []
factor_c_list = []

for i in range(N):
    list_of_coords.append([sd.random_number(i * 60, (i + 1) * 60 - 20), 700])
    list_of_length.append(sd.random_number(10, 30))
    factor_a_list.append(sd.random_number(1, 8)/10)
    factor_b_list.append(sd.random_number(1, 8)/10)
    factor_c_list.append(sd.random_number(30, 60))


flag_of_stop = False

while True:
    sd.clear_screen()
    for i, coord in enumerate(list_of_coords):
        point = sd.get_point(coord[0], coord[1])
        sd.snowflake(center=point, length=list_of_length[i], factor_a=factor_a_list[i], factor_b=factor_b_list[i],
                     factor_c=factor_c_list[i])
        coord[1] -= 10
        coord[0] += 5
        if coord[1] < 10:
            flag_of_stop = True
            break
    if flag_of_stop:
        for i, coord in enumerate(list_of_coords):
            point = sd.get_point(coord[0], coord[1])
            sd.snowflake(center=point, length=list_of_length[i], factor_a=factor_a_list[i], factor_b=factor_b_list[i],
                         factor_c=factor_c_list[i])
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()

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

# TODO Переходите ко второй части задания.
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


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

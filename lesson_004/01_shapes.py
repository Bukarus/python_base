# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор тиз текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# triangle()
# square()
# pentagon()
# hexagon()


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def n_angle_figure(number_of_angles, point=sd.get_point(300, 300), angle=0, length=60):
    angle_delta = 180 - (number_of_angles - 2) * 180 / number_of_angles
    end_point = point
    for i in range(number_of_angles-1):
        v = sd.get_vector(start_point=end_point, angle=angle + angle_delta * i, length=length, width=3)
        end_point = v.end_point
        v.draw()
    sd.line(start_point=point, end_point=end_point, width=3)


def triangle(point=sd.get_point(300, 300), angle=0, length=100):
    number_of_angles = 3
    n_angle_figure(number_of_angles=number_of_angles, point=point, angle=angle, length=length)


def square(point=sd.get_point(300, 300), angle=0, length=100):
    number_of_angles = 4
    n_angle_figure(number_of_angles=number_of_angles, point=point, angle=angle, length=length)


def pentagon(point=sd.get_point(300, 300), angle=0, length=100):
    number_of_angles = 5
    n_angle_figure(number_of_angles=number_of_angles, point=point, angle=angle, length=length)


def hexagon(point=sd.get_point(300, 300), angle=0, length=100):
    number_of_angles = 6
    n_angle_figure(number_of_angles=number_of_angles, point=point, angle=angle, length=length)


point_initial_triangle = sd.get_point(100, 200)
point_initial_square = sd.get_point(300, 150)
point_initial_pentagon = sd.get_point(450, 300)
point_initial_hexagon = sd.get_point(150, 300)


triangle(point=point_initial_triangle)
square(point=point_initial_square)
pentagon(point=point_initial_pentagon)
hexagon(point=point_initial_hexagon)


sd.pause()

# Зачёт!

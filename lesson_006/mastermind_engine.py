from random import choice


digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
required_number = ""
bulls_and_cows = {
    'bulls': 0,
    'cows': 0,
}


def take_a_number():
    # TODO Не самый оптимальный способ генерации числа.
    #  В библиотеке random есть более подходящие функции.
    #  Например shuffle или sample. С sample можно получить
    #  сразу всю случайную последовательность одной командой.
    #  Если хотите избегать 0 на первой позиции,
    #  то генерировать последовательлность можно в цикле,
    #  пока не получится последовательность начинающуася не с 0.
    #  Или можно вместо последовательности в 4 символа сгенерировать 5
    #  И если на первой позиции 0 сделать срез списка [1:], если не 0 [:4]
    #  Функция shuffle позволяет перемешать элементы списка,
    #  который можно сделать как list(range(10)). Останется только проверить
    #  0 элемент и использовать срез.
    global required_number
    one_digit = choice(list(digits))
    digits.add(0)
    digits.remove(one_digit)
    str_number = str(one_digit)
    for i in range(3):
        one_digit = choice(list(digits))
        digits.remove(one_digit)
        str_number += str(one_digit)
        required_number = str_number


def verify_number(str_user_number):
    global bulls_and_cows
    bulls_and_cows['bulls'] = 0
    bulls_and_cows['cows'] = 0
    my_set = set(str_user_number)
    required_number_set = set(required_number)

    for i in range(4):
        if str_user_number[i] == required_number[i]:
            bulls_and_cows['bulls'] += 1
            my_set.remove(required_number[i])
            required_number_set.remove(required_number[i])
    bulls_and_cows['cows'] = len(my_set & required_number_set)

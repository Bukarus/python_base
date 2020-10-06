import simple_draw as sd

Number_of_snowflakes = 100
snowflakes = list()
list_of_bottoms = list()


def make_snowflakes(number):
    # TODO При изменении содержимого объекта из глобальной области видимости
    #  не нужно объявлять её глобальной. global нужно только в случае, когда вы
    #  вы меняете саму переменную. Например для my_list.append() global не нужен.
    #  А для my_list = [] без global не обойтись.
    global snowflakes
    for i in range(number):
        additional_list = list()
        additional_list.append(sd.random_number(0, sd.resolution[0]))  # x
        additional_list.append(700)  # y
        additional_list.append(sd.random_number(5, 15))  # length
        additional_list.append(sd.random_number(1, 8) / 10)  # 'factor_a'
        additional_list.append(sd.random_number(1, 8) / 10)  # 'factor_b'
        additional_list.append(sd.random_number(30, 60))  # 'factor_c'
        additional_list.append(sd.random_number(5, 20))  # 'speed'
        snowflakes.append(additional_list)


def paint_snowflake_with_color(color):
    for i, snowflake_item in enumerate(snowflakes):
        point = sd.get_point(snowflake_item[0], snowflake_item[1])
        sd.snowflake(center=point, length=snowflake_item[2], factor_a=snowflake_item[3],
                     factor_b=snowflake_item[4], factor_c=snowflake_item[5], color=color)


def move_snowflakes():
    for i, snowflake_item in enumerate(snowflakes):
        snowflake_item[1] -= snowflake_item[6]
        snowflake_item[0] += sd.random_number(-15, 15)


def list_of_bottom_snowflakes():
    # TODO В этой функции лучше не использовать глобальные переменные.
    #  Список с индексами упавших снежинок нужно возвращать через return.
    global list_of_bottoms
    for i, snowflake_item in enumerate(snowflakes):
        if snowflake_item[1] < 10:
            list_of_bottoms.append(i)


# TODO По условиям задания в эту функцию нужно явно передавать список с элементами для удаления
def remove_list_of_bottoms():
    _list = []
    global snowflakes
    global list_of_bottoms
    _list = list_of_bottoms
    _list.reverse()
    for i, item in enumerate(_list):
        snowflakes.pop(item)

import simple_draw as sd

Number_of_snowflakes = 100
snowflakes = {}


def make_snowflakes(number):
    global snowflakes
    for i in range(number):
        snowflakes[i] = {}
        snowflakes[i]['x'] = sd.random_number(i * 12, (i + 1) * 12 - 12)
        snowflakes[i]['y'] = 700
        snowflakes[i]['length'] = sd.random_number(5, 15)
        snowflakes[i]['factor_a'] = sd.random_number(1, 8) / 10
        snowflakes[i]['factor_b'] = sd.random_number(1, 8) / 10
        snowflakes[i]['factor_c'] = sd.random_number(30, 60)
        snowflakes[i]['speed'] = sd.random_number(5, 20)


def paint_snowflake_with_color(color):
    for i, snowflake_item in snowflakes.items():
        point = sd.get_point(snowflake_item['x'], snowflake_item['y'])
        sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                     factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'],
                     color=color)


def move_snowflakes():
    for i, snowflake_item in snowflakes.items():
        snowflake_item['y'] -= snowflake_item['speed']
        snowflake_item['x'] += sd.random_number(-15, 15)


def list_of_bottom_snowflakes():
    list_of_bottoms = []
    for i, snowflake_item in snowflakes.items():
        if snowflake_item['y'] < 10:
            list_of_bottoms.append(i)
    return list_of_bottoms


def remove_list_of_bottoms(list):
    global snowflakes
    for i in list.reverse():
        snowflakes.pop(i)
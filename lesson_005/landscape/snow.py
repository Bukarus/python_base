import simple_draw as sd

sd.resolution = (1200, 600)


def snowflow():
    number_of_snowflakes = 100

    snowflakes = {}
    for i in range(number_of_snowflakes):
        snowflakes[i] = {}
        snowflakes[i]['x'] = sd.random_number(0, 300)
        snowflakes[i]['y'] = 10
        snowflakes[i]['length'] = sd.random_number(5, 15)
        snowflakes[i]['factor_a'] = sd.random_number(1, 8) / 10
        snowflakes[i]['factor_b'] = sd.random_number(1, 8) / 10
        snowflakes[i]['factor_c'] = sd.random_number(30, 60)
        snowflakes[i]['speed'] = sd.random_number(5, 20)

    while True:
        for i, snowflake_item in snowflakes.items():
            point = sd.get_point(snowflake_item['x'], snowflake_item['y'])
            sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                         factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'])
        if sd.user_want_exit():
            break

# snowflow()
# sd.pause()

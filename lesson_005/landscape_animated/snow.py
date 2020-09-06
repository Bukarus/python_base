import simple_draw as sd

# sd.resolution = (1200, 600)


def snowflow():
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

    # while True:
    # sd.start_drawing()
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
    # sd.finish_drawing()
    # sd.sleep(0.1)
    # if sd.user_want_exit():
    #     break

# snowflow()
# sd.pause()

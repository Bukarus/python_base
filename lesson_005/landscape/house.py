import simple_draw as sd

import window_of_house

import smile

sd.resolution = (1200, 600)

def house_paint():
    shift = 20

    left_bottom = sd.get_point(300 - shift, 0)
    right_top = sd.get_point(500 + shift, 200)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)

    point1 = sd.get_point(300-50, 200)
    point2 = sd.get_point(500+50, 200)
    point3 = sd.get_point((300+500)/2, 200+100)
    sd.polygon([point1, point2, point3], color=sd.COLOR_RED, width=0)

    for y in range(0, 200, 20):
        length_x = 40
        length_y = 20
        shift = 20 - shift
        for x in range(300 - shift, 500, 40):
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + length_x, y + length_y)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)
            left_bottom = sd.get_point(x + 1, y + 1)
            right_top = sd.get_point(x + length_x - 1, y + length_y - 1)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.background_color, width=0)

    window_of_house.window_paint(sd.get_point(350, 50), sd.get_point(450, 150))
    smile.smile(350, 50)


# house_paint()
# sd.pause()
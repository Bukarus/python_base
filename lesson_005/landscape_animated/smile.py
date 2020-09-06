import simple_draw


def smile(x_coord=300, y_coord=300, color=simple_draw.COLOR_YELLOW, width_of_eye=0):
    # width_of_eye = 0
    # while True:
    # simple_draw.start_drawing()
    length_x = 50
    length_y = 50
    left_bottom = simple_draw.get_point(x_coord, y_coord)
    right_top = simple_draw.get_point(x_coord + length_x, y_coord + length_y)
    simple_draw.ellipse(left_bottom=left_bottom, right_top=right_top, color=color, width=1)
    center_point_eye1 = simple_draw.get_point(x_coord + 0.30 * length_x, y_coord + 0.70 * length_y)
    center_point_eye2 = simple_draw.get_point(x_coord + 0.70 * length_x, y_coord + 0.70 * length_y)
    width_of_eye = 1 - width_of_eye
    simple_draw.circle(center_point_eye1, radius=5, color=simple_draw.background_color, width=0)
    simple_draw.circle(center_point_eye1, radius=5, width=width_of_eye)
    simple_draw.circle(center_point_eye2, radius=5)
    point_list = []
    x = x_coord + 0.3 * length_x
    while x <= x_coord+0.7*length_x:
        square_r = ((length_x / 2 - 0.20 * length_x) ** 2 + (length_y / 2 - 0.40 * length_y) ** 2)
        y = - (square_r - ((x - x_coord - length_x / 2) ** 2)) ** .5 + y_coord + length_y / 2
        point_list.append(simple_draw.get_point(x, y))
        x += 1
    simple_draw.lines(point_list=point_list)
    # simple_draw.finish_drawing()
    # simple_draw.sleep(0.5)
    # if simple_draw.user_want_exit():
    #     break


# smile()
# simple_draw.pause()

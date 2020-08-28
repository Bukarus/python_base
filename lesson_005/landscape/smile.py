import simple_draw

def smile(x_coord=300, y_coord=300, color=simple_draw.COLOR_ORANGE):
    length_x = 150
    length_y = 100
    left_bottom = simple_draw.get_point(x_coord, y_coord)
    right_top = simple_draw.get_point(x_coord + length_x, y_coord + length_y)
    simple_draw.ellipse(left_bottom=left_bottom, right_top=right_top, color=color, width=1)
    center_point_eye1 = simple_draw.get_point(x_coord + 0.30 * length_x, y_coord + 0.70 * length_y)
    center_point_eye2 = simple_draw.get_point(x_coord + 0.70 * length_x, y_coord + 0.70 * length_y)
    simple_draw.circle(center_point_eye1, radius=10)
    simple_draw.circle(center_point_eye2, radius=10)
    point1 = simple_draw.get_point(x_coord + 0.10 * length_x, y_coord + 0.5 * length_y)
    point2 = simple_draw.get_point(x_coord + (3 / 8) * length_x, y_coord + 0.25 * length_y)
    point3 = simple_draw.get_point(x_coord + (5 / 8) * length_x, y_coord + 0.25 * length_y)
    point4 = simple_draw.get_point(x_coord + 0.90 * length_x, y_coord + 0.5 * length_y)
    point_list = [point1, point2, point3, point4]
    simple_draw.lines(point_list=point_list)
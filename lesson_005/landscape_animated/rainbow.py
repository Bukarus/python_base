import simple_draw as sd

# sd.resolution = (1200, 600)


def rainbow_paint():
    rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
    # while True:
    # sd.start_drawing()
    x_center, y_center = 600, -100
    center_position = sd.get_point(x_center, y_center)
    radius = 600
    width = 10
    for color_item in rainbow_colors:
        sd.circle(center_position=center_position, radius=radius, color=color_item, width=width)
        radius += 11
    last_color = rainbow_colors.pop(0)
    rainbow_colors.append(last_color)
    # sd.finish_drawing()
    # sd.sleep(0.1)
    # if sd.user_want_exit():
    #     break

# rainbow_paint()
# sd.pause()

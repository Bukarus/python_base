import simple_draw as sd


def sun_paint():
    center_point = sd.get_point(100, 500)
    sd.circle(center_position=center_point, radius=40, color=sd.COLOR_YELLOW, width=0)
    # while True:
    angle_0 = 0
    delta = -15
    # while True:
    # sd.start_drawing()

    for i in range(10):
        vector_angle = 360 / 10
        sd.vector(start=center_point, angle=angle_0+i*vector_angle, length=80, color=sd.background_color,
                  width=1)

    angle_0 += delta

    for i in range(10):
        sd.vector(start=center_point, angle=angle_0+i*vector_angle, length=80, width=1)
        sd.circle(center_position=center_point, radius=40, color=sd.COLOR_YELLOW, width=0)

    # sd.finish_drawing()
    # sd.sleep(0.1)
    # if sd.user_want_exit():
    #     break


# sun_paint()
# sd.pause()

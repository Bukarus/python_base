import simple_draw as sd

def sun_paint():
    center_point = sd.get_point(100, 500)
    sd.circle(center_position=center_point, radius=40, color=sd.COLOR_YELLOW, width=0)
    for i in range(10):
        vector_angle = 360 / 10
        sd.vector(start=center_point, angle=i*vector_angle, length=80)

# sun_paint()
# sd.pause()
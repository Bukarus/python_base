import simple_draw as sd

sd.resolution = (1200, 600)
start_point = sd.get_point(300, 30)
start_angle = 90
start_length = 100.
const_delta = 30
root_point = sd.get_point(900, 30)

def draw_random_branches(point=root_point, angle=start_angle, length=start_length, delta=const_delta):
    if length < 5:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    dynamic_delta = sd.random_number(int(delta - .4 * delta), int(delta + .4 * delta))
    next_point = v1.end_point
    next_angle1 = angle - dynamic_delta
    next_angle2 = angle + dynamic_delta
    next_length = (length * .75)
    next_length = sd.random_number(int(next_length - .2 * next_length), int(next_length + .2 * next_length))
    draw_random_branches(point=next_point, angle=next_angle1, length=next_length)
    draw_random_branches(point=next_point, angle=next_angle2, length=next_length)

draw_random_branches()
sd.pause()
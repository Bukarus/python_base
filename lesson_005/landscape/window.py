import simple_draw as sd

def window_paint(_left_bottom, _right_top):
    sd.rectangle(left_bottom=_left_bottom, right_top=_right_top, color=sd.COLOR_BLUE, width=0)
    sd.rectangle(left_bottom=_left_bottom, right_top=_right_top, color=sd.COLOR_YELLOW, width=1)
    x1 = _left_bottom.x
    x2 = _right_top.x
    y1 = _left_bottom.y
    y2 = _right_top.y
    sd.line(start_point=sd.get_point((x1+x2)/2, y1), end_point=sd.get_point((x1+x2)/2, y2), color=sd.COLOR_YELLOW)
    sd.line(start_point=sd.get_point(x1, (y1+y2)/2), end_point=sd.get_point(x2, (y1+y2)/2), color=sd.COLOR_YELLOW)

start_point = sd.get_point(100, 100)
finish_point = sd.get_point(200, 200)
window_paint(start_point, finish_point)
sd.pause()
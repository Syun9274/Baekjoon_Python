# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

axis_x = x
axis_y = y

if x > w - x:
    axis_x = w - x
if y > h - y:
    axis_y = h - y

if axis_x <= axis_y:
    print(axis_x)
else: print(axis_y)

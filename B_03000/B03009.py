arrX, arrY = [], []

for i in range(3):
    x, y = map(int, input().split())

    if x not in arrX:
        arrX.append(x)
    else:
        arrX.remove(x)

    if y not in arrY:
        arrY.append(y)
    else:
        arrY.remove(y)

print(f'{arrX[0]} {arrY[0]}')
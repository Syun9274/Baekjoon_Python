import sys
input = sys.stdin.readline

arrX, arrY = [], []
N = int(input())

for i in range(N):
    x, y = map(int, input().split())

    arrX.append(x)
    arrY.append(y)

row = max(arrX) - min(arrX)
col = max(arrY) - min(arrY)

print(f'{row * col}')
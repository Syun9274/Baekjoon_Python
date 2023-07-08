import sys

N = int(input())
coor = [list(map(int, sys.stdin.readline().split())) for a in range(N)]

for i in range(len(coor)):
    coor[i][0], coor[i][1] = coor[i][1], coor[i][0]

coor.sort()

for i in range(len(coor) - 1):
    if coor[i][0] == coor[i + 1][0]:
        if coor[i][1] > coor[i + 1][1]:
            coor[i][1], coor[i + 1][1] = coor[i + 1][1], coor[i][1]
        else:
            continue
    else:
        continue

for i in range(len(coor)):
    print(f'{coor[i][1]} {coor[i][0]}')
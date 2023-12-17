import sys
input = sys.stdin.readline

n = int(input())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

for i in range(n):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        axis += 1
    elif x > 0:
        if y > 0:
            q1 += 1
        else: q4 += 1
    else:
        if y > 0:
            q2 += 1
        else:
            q3 += 1

sys.stdout.write('Q1: ' + str(q1) + '\n')
sys.stdout.write('Q2: ' + str(q2) + '\n')
sys.stdout.write('Q3: ' + str(q3) + '\n')
sys.stdout.write('Q4: ' + str(q4) + '\n')
sys.stdout.write('AXIS: ' + str(axis) + '\n')

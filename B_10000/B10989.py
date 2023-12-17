import sys

N = int(input())
l = [0] * 10000

for i in range(N):
    l[int(sys.stdin.readline()) - 1] += 1

for idx in range(10000):
    if l[idx] != 0:
        for i in range(l[idx]):
            sys.stdout.write(str(idx + 1) + "\n")
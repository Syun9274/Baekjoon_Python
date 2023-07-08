import sys

N = int(input())
l = []

for i in range(N):
    l.append(int(sys.stdin.readline()))

l.sort()

for i in l:
    sys.stdout.write(str(i) + "\n")
import sys

N = int(input())
ans = []

for i in range(N):
    ans.append(int(sys.stdin.readline().rstrip()))

ans.sort()

for n in ans:
    sys.stdout.write(str(n) + '\n')
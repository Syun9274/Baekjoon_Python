import sys

N = int(input())
ans = []

for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    ans.append([int(age), i, name])

ans.sort()

for i in range(len(ans)):
    print(f'{ans[i][0]} {ans[i][2]}')
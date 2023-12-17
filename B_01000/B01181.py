import sys

N = int(input())
ans = []

for i in range(N):
    wd = str(sys.stdin.readline().strip())
    ans.append((len(wd), ord(wd[0]), wd))

ans.sort()

for i in range(len(ans)):
    if ans[i - 1][2] == ans[i][2] and (i - 1) >= 0:
        continue
    else: print(ans[i][2])

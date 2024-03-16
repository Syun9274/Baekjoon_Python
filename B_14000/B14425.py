import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arrN = set(input() for _ in range(N))

ans = 0
for _ in range(M):
    tmp = input()
    if tmp in arrN:
        ans += 1

print(ans)
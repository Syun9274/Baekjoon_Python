# 소수

A, B, N = map(int, input().split())

for i in range(N):
    A %= B
    A *= 10

ans = str(A // B)
print(ans)

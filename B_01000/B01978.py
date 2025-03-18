# 소수 찾기

K = int(input())
N = list(map(int, input().split()))

for n in N:
    if n == 1:
        K -= 1
    for i in range(2, n):
        if n % i == 0:
            K -= 1
            break

print(K)

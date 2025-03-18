# 소수 구하기

import sys

def isPrime(n):
    sqrt = int(n ** 0.5)

    if n == 1:
        return False
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    else: return True

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)

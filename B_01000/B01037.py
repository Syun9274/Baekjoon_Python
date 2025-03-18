# 약수

import sys

input = sys.stdin.readline

C = int(input())
real = list(map(int, input().split()))
real.sort()

if C % 2 != 0:
    print(real[C // 2] ** 2)
else:
    print(f'{real[0] * real[-1]}')

# 수 찾기

import sys

input = sys.stdin.readline

n = input()
arrN = set(map(int, input().split()))
m = input()
arrM = list(map(int, input().split()))

for num in arrM:
    print(1) if num in arrN else print(0)

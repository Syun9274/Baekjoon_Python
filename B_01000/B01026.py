# 보물

import sys

input = sys.stdin.readline

N = input()

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)

ans = 0
for idx in range(len(arrA)):
    ans += arrA[idx] * arrB[idx]

print(ans)

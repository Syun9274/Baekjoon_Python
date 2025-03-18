# 전쟁 - 땅따먹기

from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())

for idx in range(n):
    arr = list(map(int, input().split()))
    n, ans = len(arr), ""
    countNum = Counter(arr)

    if n % 2 == 1:
        if countNum.most_common(1)[0][1] > n // 2:
            print(countNum.most_common(1)[0][0])
        else: print("SYJKGW")
    else:
        if countNum.most_common(1)[0][1] >= n // 2:
            print(countNum.most_common(1)[0][0])
        else: print("SYJKGW")

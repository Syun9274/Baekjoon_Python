import sys

N = int(input())
nowhave = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

tmp = {check[i] : 0 for i in range(len(check))}

for i in range(N):
    if nowhave[i] in tmp.keys():
        tmp[nowhave[i]] += 1
print(" ".join(map(str, list(tmp.values()))))
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

value = []
for _ in range(N):
    cost = int(input())
    value.append(cost)
    
count = 0
while K > 0:
    for idx in range(len(value) - 1, -1, -1):
        if value[idx] <= K:
            count = count + (K // value[idx])
            K = K % value[idx]

print(count)
N = int(input())
S = list(map(int, input().split()))
M = max(S)
total = 0

for i in range(len(S)):
    S[i] = S[i] / M * 100
    total += S[i]

print(total / N)

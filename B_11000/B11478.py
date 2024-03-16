import sys
input = sys.stdin.readline

S = input().strip()
ans = set()

for rear in range(1, len(S) + 1):
    for front in range(len(S) - rear + 1):
        ans.add(S[front : front + rear])

print(len(ans))
import sys

A, B, C = map(int, sys.stdin.readline().split())

if B == C:
    print(-1)
else:
    n = int(A / (C - B) + 1)

    if n < 0:
        print(-1)
    else: print(n)

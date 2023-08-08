import heapq
import sys
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    X = int(input())
    
    if X == 0:
        if not hq:
            print(0)
        else:
            n, value = heapq.heappop(hq)
            print(value)
    else:
        heapq.heappush(hq, (abs(X), X))
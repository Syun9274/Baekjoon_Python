# 최소 힙

import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    n = int(input())
    
    if n == 0:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq))
            
    else:
        heapq.heappush(hq, n)

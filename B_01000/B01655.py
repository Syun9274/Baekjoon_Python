# 가운데를 말해요

import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())

# 중앙값보다 큰 값을 저장함 
# (루트 값이 힙 내에서 가장 작음 = 중앙값과 가장 가까운 값이 루트 값)
minheap = []

# 중앙값과 같거나 작은 값을 저장함 
# (루트 값이 힙 내에서 가장 큼 = 중앙값 또는 중앙값과 가장 가까운 값이 루트 값)
maxheap = []

for _ in range(N):
    x = int(input().rstrip())
    
    # 두 heap의 크기 차이가 최대 1개까지만 나도록 데이터 삽입을 조정
    # 데이터 삽입은 maxheap이 우선권을 가짐
    if len(maxheap) <= len(minheap):
        heapq.heappush(maxheap, -x)
    else:
        heapq.heappush(minheap, x)
        
    # 각 heap 데이터에 문제가 발생했을 경우 재조정
    if minheap and -maxheap[0] > minheap[0]:
        val1 = heapq.heappop(minheap)
        val2 = -heapq.heappop(maxheap)
        heapq.heappush(minheap, val2)
        heapq.heappush(maxheap, -val1)
        
    sys.stdout.write(str(-maxheap[0]) + '\n')

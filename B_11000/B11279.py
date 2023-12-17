import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = [0]
    
for _ in range(N):
    try:
        n = int(input())
        
        if n == 0:
            # -n으로 삽입했으므로 다시 '-'를 곱한 값 출력
            sys.stdout.write(str(-heapq.heappop(hq)) + '\n')
            
        else:
            # 최소 힙에서 최대 값 반환을 위해 -n 삽입
            heapq.heappush(hq, -n)
    
    except IndexError:
        print(0)
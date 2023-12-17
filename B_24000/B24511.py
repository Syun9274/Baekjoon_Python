from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = deque(map(int, input().split()))

result = deque()
for n in range(N):
    if A[n] == 1:
        continue
    
    result.appendleft(B[n])
    
result.extend(C)

for i in range(M):
    print(result.popleft(), end=" ")    
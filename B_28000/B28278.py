from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dq = deque()


for _ in range(N):
    command = list(map(int, input().rstrip().split()))
    
    if command[0] == 1:
        dq.append(command[1])
        
    elif command[0] == 2:
        if not dq:
            print(-1)
        else: print(dq.pop())
        
    elif command[0] == 3:
        print(len(dq))
        
    elif command[0] == 4:
        if not dq:
            print(1)
        else: print(0)
        
    elif command[0] == 5:
        if not dq:
            print(-1)
        else: print(dq[-1])  
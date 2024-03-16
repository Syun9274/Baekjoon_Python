from collections import deque
import sys
input = sys.stdin.readline

dq = deque()

N = int(input())

for _ in range(N):
    cmd = list(map(int, input().split()))
    com = cmd[0]
    
    if com == 1:
        dq.appendleft(cmd[1])
    elif com == 2:
        dq.append(cmd[1])
    elif com == 3:
        print(dq.popleft()) if dq else print(-1)
    elif com == 4:
        print(dq.pop()) if dq else print(-1)
    elif com == 5:
        print(len(dq))
    elif com == 6:
        print(0) if dq else print(1)
    elif com == 7:
        print(dq[0]) if dq else print(-1)
    elif com == 8:
        print(dq[-1]) if dq else print(-1)
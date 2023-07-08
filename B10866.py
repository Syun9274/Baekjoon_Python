from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
dp = deque()

for _ in range(N):
    command = list(map(str, input().split()))
    cmd = command[0]
    
    if cmd == "push_front":
        dp.appendleft(command[1])
    elif cmd == "push_back":
        dp.append(command[1])
    elif cmd == "pop_front":
        print(-1) if len(dp) == 0 else print(dp.popleft())
    elif cmd == "pop_back":
        print(-1) if len(dp) == 0 else print(dp.pop())
    elif cmd == "size":
        print(len(dp))    
    elif cmd == "empty":
        print(1) if len(dp) == 0 else print(0)
    elif cmd == "front":
        print(-1) if len(dp) == 0 else print(dp[0])
    elif cmd == "back":
        print(-1) if len(dp) == 0 else print(dp[-1])
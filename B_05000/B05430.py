import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip() 
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    
    reverse = False
    error = False
    
    dq = deque(arr)
    
    for func in p:
        if func == "R":
            reverse = not reverse
        elif func == "D":
            if len(dq) == 0 or n == 0:
                error = True
                break
            elif reverse:
                dq.pop()
            else:
                dq.popleft()
    
    if error:
        print("error")
    else:
        if reverse:
            dq.reverse()
        print("[" + ",".join(dq) + "]")
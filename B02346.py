from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
inputNums = list(enumerate(map(int, input().split()), start= 1))
dq = deque(inputNums)
result = []
index = 0

while dq:
    current = dq[index]
    result.append(current[0])
    num = current[1]
    
    dq.remove(current)
    
    if len(dq) == 1:
        result.append(dq[0][0])
        break
    
    if num > 0:
        index = (index + num - 1) % len(dq)
    else:
        index = (index + num) % len(dq)
        
print(" ".join(map(str, result)))
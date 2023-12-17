from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
nums = map(int, input().rstrip().split())
imsi = deque()
tmp = 0

for n in nums:
    
    if n == tmp + 1:
        tmp = n
        continue
    while imsi and imsi[-1] == tmp + 1:
            tmp = imsi.pop()

    imsi.append(n)
    
    while imsi and len(imsi) >= 2 and imsi[-2] < imsi[-1]:
        print("Sad")
        exit()
        
print("Nice")
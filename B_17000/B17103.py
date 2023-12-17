import math
import sys
input = sys.stdin.readline

num = [True for _ in range(1000001)]
num[0] = num[1] = False
prime = []

for i in range(2, len(num)):
    if num[i]:
        prime.append(i)
        
        for j in range(i + i, len(num), i):
            num[j] = False
            
T = int(input())

for i in range(T):
    N = int(input().strip())
    ans = 0
    
    for j in prime:
        if N < 2 * j:
            break
        
        if num[N - j]:
            ans += 1
    
    print(ans)
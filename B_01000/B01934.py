# 최소공배수

import math

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    
    print(math.lcm(a, b)) # 최소공배수 구하는 메소드 math.lcm()

# 스택 수열

import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]

stack = []
ans = []
current = 1

for num in seq:
    while current <= num:
        stack.append(current)
        ans.append('+')
        current += 1
        
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        exit(0)
        
print('\n'.join(ans))

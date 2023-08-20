import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))

time.sort()

ans, total = 0, 0
for n in time:
    ans = ans + n
    total += ans
    
print(total)
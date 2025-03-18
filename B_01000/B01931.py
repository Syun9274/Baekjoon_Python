# 회의실 배정

import sys
input = sys.stdin.readline

N = int(input())

time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append((end, start))

time.sort()

maxcount = 1
end_time = time[0][0]

for idx in range(1, N):
    if time[idx][1] >= end_time:
        maxcount += 1
        end_time = time[idx][0]

print(maxcount)

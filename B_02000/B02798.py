import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_sum = 0

for idx1 in range(N):
    for idx2 in range(idx1 + 1, N):
        for idx3 in range(idx2 + 1, N):
            tmp = nums[idx1] + nums[idx2] + nums[idx3]

            if tmp <= M and max_sum < tmp:
                max_sum = tmp

print(max_sum)
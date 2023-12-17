import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

dic = {0: 1}
currentSum = 0
counter = 0

for num in nums:
    currentSum += num
    remain = currentSum % M

    if remain in dic:
        counter += dic[remain]

    dic[remain] = dic.get(remain, 0) + 1

print(counter)
from collections import Counter

n = int(input())
ans = 0

for i in range(n):
    arr = list(map(int, input().split()))
    arr = Counter(arr).most_common(3)
    tmp = 0

    if arr[0][1] == 3:
        tmp = 10000 + arr[0][0] * 1000
    elif arr[0][1] == 2:
        tmp = 1000 + arr[0][0] * 100
    else:
        arr.sort()
        tmp = arr[2][0] * 100

    if tmp > ans:
        ans = tmp
    else: continue

print(ans)

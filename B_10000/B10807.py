n = int(input())
arr = list(map(int, input().split()))
fnum = int(input())
cnt = 0

for i in range(len(arr)):
    if arr[i] == fnum:
        cnt += 1
    else: pass

print(cnt)
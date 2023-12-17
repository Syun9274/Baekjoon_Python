N, X = map(int, input().split())
arr = list(map(int, input().split()))
ans = []

for num in arr:
    if num < X:
        ans.append(num)
    else: pass

for i in range(len(ans)):
    print(ans[i])
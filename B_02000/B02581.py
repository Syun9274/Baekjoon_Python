M = int(input())
N = int(input())
ans = []

for n in range(M, N + 1):
    if n == 1:
        continue
    elif n == 2:
        ans.append(n)
        continue
    for i in range(2, n):
        if n % i == 0:
            break
        elif i == n - 1:
            ans.append(n)
            break

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])

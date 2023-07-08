n = int(input())
n -= 1

ans = (int)((n - 1) / 6) + 1
while True:
    if 3 * ans * (ans - 1) + 1 <= n <= 3 * ans * (ans + 1) - 1:
        print(ans + 1)
        break
    ans += 1

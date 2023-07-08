K, N, M = map(int, input().split())

cost = K * N

ans = cost - M

if ans >= 0:
    print(ans)
else:
    print(0)
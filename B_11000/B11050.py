import math
FT = math.factorial

N, K = map(int, input().split())

ans = FT(N) / (FT(K) * FT(N - K))
print(int(ans))
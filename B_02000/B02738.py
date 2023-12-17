N, M = map(int, input().split())

m1 = [list(map(int, input().split())) for i in range(N)]
m2 = [list(map(int, input().split())) for i in range(N)]

for n in range(N):
    for m in range(M):
        print(f'{m1[n][m] + m2[n][m]}', end=' ')
    print()
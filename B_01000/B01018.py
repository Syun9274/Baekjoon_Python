import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]

min_count = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        count = 0

        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # 체스판의 시작점(0, 0)이 black인 경우를 기준으로
                if (x + y) % 2 == 0:
                    if board[x][y] != 'B':
                        count += 1
                else:
                    if board[x][y] != 'W':
                        count += 1

        min_count = min(min_count, count, 64 - count)

print(min_count)
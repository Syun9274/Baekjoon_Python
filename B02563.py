white = [[0] * 100 for _ in range(100)]
n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    for row in range(b, b + 10):
        for col in range(a, a + 10):
            white[row][col] = 1

ans = 0
for row in range(100):
    ans += white[row].count(1)

print(ans)

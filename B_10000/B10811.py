N, M = map(int, input().split())
arr = [str(A) for A in range(1, N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    count = (b - a + 1) // 2

    for j in range(count):
        arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]
        a += 1
        b -= 1

ans = ' '.join(arr)
print(ans)
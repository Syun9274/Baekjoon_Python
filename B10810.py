N, M = map(int, input().split())
arr = [None for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())

    for j in range(a - 1, b):
        arr[j] = c

for i in range(len(arr)):
    if arr[i] == None:
        arr[i] = '0'
    
    print(arr[i], end=' ')
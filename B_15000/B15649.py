def permutation(arr, m, result):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(len(arr)):
        if arr[i] in result:
            continue
        
        result.append(arr[i])
        permutation(arr, m, result)
        result.pop()


N, M = map(int, input().split())

numbers = list(range(1, N + 1))

permutation(numbers, M, [])
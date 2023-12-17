while True:
    n = int(input())
    arr = []
    total = 0

    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            arr.append(str(i))
            total += i

    if total == n:
        ansarr = ' + '.join(arr)

        print(f'{n} = {ansarr}')
    else:
        print(f'{n} is NOT perfect.')
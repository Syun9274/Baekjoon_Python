while True:
    n1, n2 = map(int, input().split())

    if n1 == n2 == 0:
        break

    print(f'{n1 + n2}')
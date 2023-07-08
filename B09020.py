def Prime(n):
    sqrt = int(n ** 0.5)

    if n == 1:
        return False
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    else: return True

N = int(input())

for i in range(N):
    n = int(input())
    a = n / 2
    c = 0

    if Prime(a) == True:
        print(f'{int(a)} {int(a)}')
    else:
        while True:
            a -= 1
            c += 1
            if Prime(a) == True and Prime(n / 2 + c) == True:
                print(f'{int(a)} {int(n / 2 + c)}')
                break
def factorization(n):
    c = 2

    while c <= n:
        if n % c == 0:
            print(c)
            n = n / c
        else: c += 1

N = int(input())
factorization(N)
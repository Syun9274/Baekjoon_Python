def sigma(n):
    return n * (n + 1) // 2

a, b = map(int, input().split())

if a > b:
    a, b = b, a

n1, n2 = sigma(a), sigma(b)
print(f'{n2 - n1 + a}')

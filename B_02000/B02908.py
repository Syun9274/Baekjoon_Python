n1, n2 = map(str, input().split())

n1, n2 = n1[::-1], n2[::-1]

if n1 > n2:
    print(n1)
else: print(n2)
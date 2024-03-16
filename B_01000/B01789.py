n = int(input())
a = 1

while True:
    total = a * (a + 1) // 2

    if total > n:
        print(a - 1)
        break

    a += 1

def Prime(n):
    if n == 1:
        return False
    
    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

l = list(range(2, 123456 * 2))
m = []

for i in l:
    if Prime(i):
        m.append(i)

n = int(input())

while True:
    c = 0
    if  n == 0:
        break

    for i in m:
        if n < i <= 2 * n:
            c += 1
    
    print(c)
    n = int(input())
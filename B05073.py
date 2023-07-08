while True:
    length = list(map(int, input().split()))
    
    if length == [0, 0, 0]:
        break
    elif sum(length) - max(length) <= max(length):
        print('Invalid')
        continue

    length = set(length)
    n = len(length)

    if n == 1:
        print('Equilateral')
    elif n == 2:
        print('Isosceles')
    elif n == 3:
        print('Scalene')

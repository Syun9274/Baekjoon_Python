n = int(input())
blank = ' '
star = '*'
a = n - 1

for i in range(1, 2 * n, 2):
    print(f'{blank * a}{star * i}')
    a -= 1

b = 1
for i in range(2 * n - 3, 0, -2):
    print(f'{blank * b}{star * i}')
    b += 1

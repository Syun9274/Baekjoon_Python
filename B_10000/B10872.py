import sys

def factorial(n, ans):
    if n == 1:
        return sys.stdout.write(str(ans) + '\n')
    elif n == 0:
        return print(1)

    ans = ans * n
    n -= 1

    factorial(n, ans)

n = int(input())
ans = 1

factorial(n, ans)
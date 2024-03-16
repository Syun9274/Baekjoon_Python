import math
import sys
input = sys.stdin.readline

def isPrime(n):
    if n < 2:
        return False

    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    num = int(input())
    
    if isPrime(num):
        print(num)
    else:
        while True:
            num += 1
            if isPrime(num):
                print(num)
                break
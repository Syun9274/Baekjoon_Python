# 분수 합

import math

numeratorA, denominatorA = map(int, input().split())
numeratorB, denominatorB = map(int, input().split())

denominator = denominatorA * denominatorB
numerator = (numeratorA * denominatorB) + (numeratorB * denominatorA)

gcd = math.gcd(numerator, denominator)
numerator //= gcd
denominator //= gcd

print(f'{numerator} {denominator}')

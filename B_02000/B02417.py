import math
import sys

n = int(sys.stdin.readline())
sqrt = math.isqrt(n)

if sqrt * sqrt >= n:
    print(sqrt)
else:
    print(sqrt + 1)
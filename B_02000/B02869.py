import math

A, B, V = map(int, input().split())
d = A - B

n = (V - B) / d

print(math.ceil(n))
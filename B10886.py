import sys
input = sys.stdin.readline

n = int(input())
a = 0

for i in range(n):
    b = int(input())
    a += b

if n // 2 < a:
    print("Junhee is cute!")
else: print("Junhee is not cute!")
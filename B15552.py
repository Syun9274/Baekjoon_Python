import sys

n = int(input())

for i in range(n):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(n1 + n2)
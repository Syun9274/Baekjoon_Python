# 대칭차집합

import sys

input = sys.stdin.readline

A, B = map(int, input().split())
arrA = set(map(int, input().split()))
arrB = set(map(int, input().split()))

AmB = arrA - arrB
BmA = arrB - arrA

ans = set(AmB | BmA)

print(len(ans))

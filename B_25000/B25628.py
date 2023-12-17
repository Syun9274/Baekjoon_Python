A, B = map(int, input().split())

if A < 2 or B < 1:
    print(0)
else:
    hamburger = min(A // 2, B)
    print(hamburger)
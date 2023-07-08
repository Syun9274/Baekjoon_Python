H, M = map(int, input().split())
time = int(input())

M += time

while M > 59:
    M -= 60
    H += 1
    if H == 24:
        H = 0

print(H, M)

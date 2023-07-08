total = int(input())
count = int(input())
prize = 0

for i in range(count):
    n1, n2 = map(int, input().split())
    prize += n1 * n2

if total == prize:
    print("Yes")
else: print("No")
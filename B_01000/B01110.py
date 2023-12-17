n = str(input())
start = n
cycle = 0

if int(n) < 10 :
        n = n + '0'
        n = n[::-1]

while True:
    cycle += 1

    if int(n) < 10 :
        n = n + '0'
        n = n[::-1]

    p1 = int(n[0]) + int(n[1])
    p2 = str(p1)[::-1]
    p2 = p2[0]
    p3 = n[1] + p2
    n = p3

    if int(n) == int(start):
        break

print(cycle)

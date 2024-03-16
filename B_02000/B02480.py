n1, n2, n3 = map(int, input().split())
reward = 0

if n1 == n2 and n2 == n3:
    reward = 10000 + n1 * 1000
elif n1 == n2 or n2 == n3 or n1 == n3:
    if n1 == n2: n = n1
    elif n2 == n3: n = n2
    else: n = n1
    reward = 1000 + n * 100
else: reward = max(n1, n2, n3) * 100

print(reward)

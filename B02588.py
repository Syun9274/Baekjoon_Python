A = int(input())
B = int(input())

B100 = B//100
B10 = B//10 - B100*10
B1 = B - B100*100 - B10*10

a1 = A * B1
a2 = A * B10
a3 = A * B100

print(a1)
print(a2)
print(a3)
print(f'{a1 + a2 * 10 + a3 * 100}')

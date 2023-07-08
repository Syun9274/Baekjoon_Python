l = []
sum = 0

for i in range(5):
    n = int(input())
    l.append(n)
    sum += n

l.sort()
avg = int(sum / len(l))

print(avg)
print(l[2])

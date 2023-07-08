arr = []

for i in range(9):
    num = int(input())
    arr.append(num)

for i in range(len(arr)):
    M = max(arr)
    idx = arr.index(M)

print(M)
print(idx + 1)

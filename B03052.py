arr = []

for i in range(10):
    n = int(input())
    R = n % 42

    if R in arr:
        pass
    else: arr.append(R)

print(len(arr))
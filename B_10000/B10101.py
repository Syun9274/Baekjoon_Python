from collections import Counter

arr = []

for i in range(3):
    arr.append(int(input()))

if sum(arr) != 180:
    print("Error")
    
else:
    arr = Counter(arr).most_common(3)

    n = arr[0][1]

    if n == 3:
        print("Equilateral")
    elif n == 2:
        print("Isosceles")
    elif n == 1:
        print("Scalene")
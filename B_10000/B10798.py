arr = []
for i in range(5):
    arr.append(str(input()))

for col in range(15):
    for row in range(5):
        if col < len(arr[row]):
            print(arr[row][col], end='')
        else: continue
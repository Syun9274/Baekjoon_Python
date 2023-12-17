arr = [int(0) for i in range(30)]
 
for i in range(28):
    Y  = int(input())
    arr[Y - 1] = 1

for idx in range(len(arr)):
    if arr[idx] == 0:
        print(idx + 1)
    else: pass
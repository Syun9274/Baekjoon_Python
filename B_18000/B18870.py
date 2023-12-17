import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr_sort = list(sorted(set(arr)))

arr_sort = {arr_sort[idx] : idx for idx in range(len(arr_sort))}

for num in arr:
    sys.stdout.write(str(arr_sort[num]) + ' ')
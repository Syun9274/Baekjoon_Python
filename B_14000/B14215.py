length = list(map(int, input().split()))

length.sort()

tmp = length[0] + length[1]
longest = length[2]

if tmp <= longest:
    print(tmp * 2 - 1)
else: print(sum(length))
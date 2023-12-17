from collections import Counter
import sys

N = int(input())
l = []

for i in range(N):
    l.append(int(sys.stdin.readline()))

l.sort()

tmp = Counter(l).most_common()
if len(tmp) > 1 and tmp[0][1] == tmp[1][1]:
    mode = tmp[1][0]
else:
    mode = tmp[0][0]
    
print(round(sum(l) / len(l)))
print(l[N // 2])
print(mode)
print(abs(l[-1] - l[0]))

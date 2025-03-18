# 단어 공부

W = input().upper()
DIR = {}

for wd in W:
    if wd not in DIR:
        DIR[wd] = 1
    else:
        DIR[wd] += 1

K = list(DIR.keys())
V = list(DIR.values())
M = V.count(max(V))

if M != 1:
    print('?')
else:
    print(K[V.index(max(V))])

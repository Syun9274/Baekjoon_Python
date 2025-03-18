# 그룹 단어 체커

N = int(input())
ans = 0

for i in range(N):
    wd = input()
    l = []
    for idx in range(len(wd)):
        if wd[idx] in l and idx - 1 >= 0 and wd[idx - 1] == wd[idx]:
            continue
        else:
            l.append(wd[idx])
            
    if len(set(wd)) == len(l):
        ans += 1

print(ans)

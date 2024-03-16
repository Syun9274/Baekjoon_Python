wds = str(input())
ans = True

for i in range(len(wds)):
    if wds[i] != wds[-(i + 1)]:
        ans = False
        print(0)
        break

if ans == True:
    print(1)
n = int(input())
ans = []

for i in range(n):
    a = int(input())
    ans.append(a)

ans.sort()

for num in ans:
    print(num)
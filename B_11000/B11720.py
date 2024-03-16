N = int(input())
n = str(input())
ans = 0

for i in range(0, len(n), int(len(n)/N)):
    ans += int(n[i : int(i + len(n)/N)])

print(ans)
import sys
input = sys.stdin.readline

N = int(input())
arr = []
ans = 0

for _ in range(N):
    string = input().strip()
    
    if string == "ENTER":
        arr = []
    elif string in arr:
        continue
    else:
        arr.append(string)
        ans += 1
        
print(ans)         
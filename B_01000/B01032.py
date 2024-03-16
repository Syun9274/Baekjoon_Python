import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(input())
else:
    fileName = [input().rstrip() for _ in range(N)]
    ans = ""

    for i in range(len(fileName[0])):
        char = fileName[0][i]
        
        for j in range(1, N):
            if char != fileName[j][i]:
                ans += "?"
                break
        
        else:
            ans += char
            
    print(ans)

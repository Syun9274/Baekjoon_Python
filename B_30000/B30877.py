import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input().strip())
ans = []

for _ in range(n):
    word1, word2 = map(str, input().split())

    idx = word1.lower().index('x')
    ans.append(word2[idx].upper())
    
print(''.join(ans))
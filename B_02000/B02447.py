import sys
input = sys.stdin.readline

# 재귀 호출의 최대 깊이 설정 값
sys.setrecursionlimit(10 ** 6)

def star(LEN):
    if LEN == 1:
        return ['*']
    
    stars = star(LEN // 3)
    arr = []
    
    for s in stars:
        arr.append(s * 3)
        
    for s in stars:
        arr.append(s + ' ' * (LEN // 3) + s)
        
    for s in stars:
        arr.append(s * 3)
        
    return arr

N = int(input().strip())
print('\n'.join(star(N)))
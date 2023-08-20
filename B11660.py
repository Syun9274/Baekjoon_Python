import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 누적 합 2차원 리스트로 변경
sumarr = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sumarr[i][j] = (arr[i - 1][j - 1] 
                        + sumarr[i - 1][j] 
                        + sumarr[i][j - 1] 
                        - sumarr[i - 1][j - 1])

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    result = (sumarr[x2][y2] 
              - sumarr[x2][y1 - 1] 
              - sumarr[x1 - 1][y2] 
              + sumarr[x1 - 1][y1 - 1])
    
    print(result)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

sumarr = [0]
for num in arr:
    sumarr.append(sumarr[-1] + num)
    
ans = arr[0]
for front in range(N - K + 1):
    if N == K:
        ans = sumarr[-1]
        break
    
    rear = front + K
    
    tmp = (sumarr[rear] - sumarr[front])
    if tmp > ans:
        ans = tmp
        
print(ans)
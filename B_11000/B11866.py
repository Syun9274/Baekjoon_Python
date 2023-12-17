N, K = map(int, input().split())
arr = [x for x in range(1, N + 1)]
ans = []

idx = K - 1

while len(arr) > 0:
    n = len(arr)
    
    while idx >= n:
        idx -= n
        
    ans.append(str(arr[idx]))
    del(arr[idx])
    
    idx += K - 1
    
print(f'<{", ".join(ans)}>')
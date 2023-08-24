import sys
input = sys.stdin.readline

def merge(arr, p, q, r):
    global count, K, ans
    tmp = []
    i = p
    j = q + 1
    
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
            
        else:
            tmp.append(arr[j])
            j += 1
            
    while i <= q:
        tmp.append(arr[i])
        i += 1
    
    while j <= r:
        tmp.append(arr[j])
        j += 1
        
    i = p
    t = 0
    
    while i <= r:
        arr[i] = tmp[t]
        count += 1
        
        if count == K:
            ans = arr[i]
            
        i += 1
        t += 1
    
def mergeSort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(arr, p, q)
        mergeSort(arr, q + 1, r)
        merge(arr, p, q, r)
    
    else:
        return
    
A, K = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
ans = -1
l = len(arr) - 1

mergeSort(arr, 0, l)
print(ans)
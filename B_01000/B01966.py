# 프린터 큐

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    count = 1
    current = 0
    
    while True:
        if current >= len(imp):
            current -= len(imp)
        
        if imp[current] == max(imp) and current == M:
            print(count)
            break
        
        elif imp[current] == max(imp):
            if current < M:
                M -= 1
            
            del[imp[current]]
            count += 1
            
        elif imp[current] != max(imp):
            current += 1
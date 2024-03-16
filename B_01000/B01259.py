while True:
    n = str(input())
    
    if n == '0':
        break
    
    for idx in range(len(n) // 2):
        if n[idx] != n[-(idx + 1)]:
            print("no")
            break
    
    else: print("yes")
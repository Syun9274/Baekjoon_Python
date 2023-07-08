def factorial(n):
    if n <= 1:
        return 1
    
    return factorial(n - 1) * n

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    ans = (factorial(M) // factorial(M - N)) // factorial(N)
    print(ans)
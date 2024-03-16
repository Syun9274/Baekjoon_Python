def sum_of_digits(n):
    total = 0
    
    while n > 0:
        total += n % 10
        n //= 10
        
    return total

N = int(input())
ans = 0

for n in range(N):
    tmp = n + sum_of_digits(n)
    
    if tmp == N:
        ans = n
        break
    
print(ans)
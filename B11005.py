n, b = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while n > 0:
    result += digits[n % b]
    n //= b

print(result[::-1])
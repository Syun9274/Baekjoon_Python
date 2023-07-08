X = int(input())

diagonal = 1
while diagonal * (diagonal + 1) // 2 < X:
    diagonal += 1

if diagonal % 2 == 0:
    numerator = X - diagonal * (diagonal - 1) // 2
    denominator = diagonal - numerator + 1
else:
    denominator = X - diagonal * (diagonal - 1) // 2
    numerator = diagonal - denominator + 1

print(f"{numerator}/{denominator}")
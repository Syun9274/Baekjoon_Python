num, totalKG = map(int, input().split())

table = [0] * (totalKG + 1)

for _ in range(num):
    weight, value = map(int, input().split())
    
    for j in range(totalKG, weight - 1, -1):
        table[j] = max(table[j], table[j - weight] + value)

print(max(table))
import math
import sys

input = sys.stdin.readline

N = int(input())
positions = []
distances = []

for _ in range(N):
    position = int(input())
    positions.append(position)

for idx in range(1, N):
    distance = positions[idx] - positions[idx - 1]
    distances.append(distance)

gcd_value = distances[0]
for idx in range(1, len(distances)):
    gcd_value = math.gcd(gcd_value, distances[idx])

ans = sum([(dist // gcd_value) - 1 for dist in distances])

print(ans)
import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    scores = list(map(int, input().split()))
    N = scores[0]
    total = sum(scores[1:])
    average = total / N

    count = 0
    for score in scores[1:]:
        if score > average:
            count += 1

    ratio = (count / N) * 100

    print(f"{ratio:.3f}%")
import sys
input = sys.stdin.readline

peo = {"ChongChong" : 1}

N = int(input())

for _ in range(N):
    p1, p2 = map(str, input().split())

    if p1 not in peo:
        peo[p1] = 0
    if p2 not in peo:
        peo[p2] = 0
    
    if p1 == "ChongChong" or p2 == "ChongChong":
        peo[p1] = peo[p2] = 1
    elif peo[p1] == 1 or peo[p2] == 1:
        peo[p1] = peo[p2] = 1
        
dancePeo = sum(peo.values())
print(dancePeo)
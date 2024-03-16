import sys
input = sys.stdin.readline

n = int(input())
inCompany = set()

for _ in range(n):
    name, command = map(str, input().split())
    
    if command == "enter":
        inCompany.add(name)
    elif command == "leave":
        inCompany.remove(name)
        
inCompany = sorted(inCompany, reverse=True)

for ans in inCompany:
    print(ans)
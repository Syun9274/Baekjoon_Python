import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_dict = {}
number_dict = {}

for i in range(1, N + 1):
    name = input().rstrip()
    name_dict[name] = i
    number_dict[i] = name

for _ in range(M):
    query = input().rstrip()

    if query.isdigit():
        print(number_dict[int(query)])
    else:
        print(name_dict[query])
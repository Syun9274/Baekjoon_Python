DIR = {3 : ['A', 'B', 'C'],
       4 : ['D', 'E', 'F'],
       5 : ['G', 'H', 'I'],
       6 : ['J', 'K', 'L'],
       7 : ['M', 'N', 'O'],
       8 : ['P', 'Q', 'R', 'S'],
       9 : ['T', 'U', 'V'],
       10 : ['W', 'X', 'Y', 'Z']}

K = list(DIR.keys())
V = list(DIR.values())
wd = str(input())
ans = 0

for w in wd:
    for i in range(3, 11):
        if w in DIR[i]:
            ans += i

print(ans)
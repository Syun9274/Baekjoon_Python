M = [list(map(int, input().split())) for i in range(9)]

row = []
for i in range(9):
    row.append(max(M[i]))

maxnum = max(row)
rowidx = row.index(maxnum)
colidx = M[rowidx].index(maxnum)

print(maxnum)
print(f'{rowidx + 1} {colidx + 1}')

board = list(input().split('.'))

for idx in range(len(board)):
    n = len(board[idx])

    if n % 2 != 0:
        n = -1
        break
    else:
        a = n // 4
        b = (n - (4 * a)) // 2
        board[idx] = "AAAA" * a + "BB" * b
        
if n == -1:
    print(n)
else: print('.'.join(board))

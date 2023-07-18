# PyPy3

def is_valid(row, col, num, board):
    if num in [elem[col] for elem in board]:
        return False
    
    if num in board[row]:
        return False
    
    if row < 3:
        tmpRow = 0
    elif row < 6:
        tmpRow = 3
    elif row < 9:
        tmpRow = 6
        
    if col < 3:
        tmpCol = 0
    elif col < 6:
        tmpCol = 3
    elif col < 9:
        tmpCol = 6
        
    cube = []
        
    for idx1 in range(tmpRow, tmpRow + 3):
        for idx2 in range(tmpCol, tmpCol + 3):
            cube.append(board[idx1][idx2])
    
    if num in cube:
        return False
    
    return True

def sudoku(row, col, board):
    if row == 9:
        return True

    if board[row][col] != 0:
        if col < 8:
            return sudoku(row, col + 1, board)
        else:
            return sudoku(row + 1, 0, board)

    for num in range(1, 10):
        if is_valid(row, col, num, board):
            board[row][col] = num

            if col < 8:
                if sudoku(row, col + 1, board):
                    return True
            else:
                if sudoku(row + 1, 0, board):
                    return True
        
            board[row][col] = 0
    
    return False
 
board = [list(map(int, input().split())) for _ in range(9)]

for col in range(9):
    for row in range(9):
        sudoku(row, col, board)
        
for col in range(9):
    print(f'{" ".join(map(str, board[col]))}')
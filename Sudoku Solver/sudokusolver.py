# Sudoku Solver in Python

def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> represented with -1
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None
    pass

def is_valid(puzzle, guess, row, col):
    # for rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # for columns
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # for 3x3 square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    if row is None:
        return True
    
    # step 2: if there is a place to put a number, them make a guess (1-9)
    for guess in range(1, 10):
        # step 3: check if guess is valid
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
            
        # step 5: if not valid OR if guess does not solve puzzle, then backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers we tried works, then puzzle is UNSOLVABLE!
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,    -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
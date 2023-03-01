'''
Sudoku Input Example:

puzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

main(puzzle)

'''

def is_valid(puzzle, row, col, num):
    # Check if num is already present in row
    for i in range(9):
        if puzzle[row][i] == num:
            return False

    # Check if num is already present in column
    if i in range(9):
        if puzzle[i][col] == num:
            return False

    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if puzzle[box_row + i][box_col + j] == num:
                return False

    return True


def solve_puzzle(puzzle, row=0, col=0):
    # Base case: puzzle is solved
    if row == 9:
        return puzzle

    # Calculate next row and column
    next_row = row
    next_col = col + 1

    if next_col == 9:
        next_row += 1
        next_col = 0

    if puzzle[row][col] != 0:
        return solve_puzzle(puzzle, next_row, next_col)

    # Sort from 1 to 9
    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num
            solution = solve_puzzle(puzzle, next_row, next_col)

            if solution is not None:
                return solution
            puzzle[row][col] = 0

    # No valid number found
    return None


def main(puzzle):
    solution = solve_puzzle(puzzle)

    if solution is None:
        print("No solution found!")

    else:
        print("Solution:")
        for row in solution:
            print(row)
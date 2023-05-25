# Function to check if a queen can be placed at the given position
def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function to solve the N-Queens problem
def solve_n_queens(board, row, n, count):
    if row == n:
        # Print the solution
        print_solution(board, n)
        count[0] += 1
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            # Recursively solve for the next row
            solve_n_queens(board, row + 1, n, count)

            # Backtrack and try other possibilities
            board[row][col] = 0

# Function to print the solution
def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
        

# Function to solve the N-Queens problem using branch and bound
def solve_n_queens_branch_and_bound(n):
    board = [[0] * n for _ in range(n)]
    count = [0]  # Keep track of the number of solutions
    solve_n_queens(board, 0, n, count)

    print(f"Number of solutions for {n}-queens: {count[0]}")

# Get user input for the number of queens
n = int(input("Enter the number of queens: "))

# Solve the N-Queens problem using branch and bound
solve_n_queens_branch_and_bound(n)
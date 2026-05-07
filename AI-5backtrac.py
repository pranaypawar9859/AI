# N-Queens using Backtracking
N = 4

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(board, row):
    if row == N:
        print("Solution:", board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_nqueens(board, row + 1):
                return True
            board[row] = -1  # backtrack
    return False

board = [-1] * N
print("Backtracking Solution for N-Queens:")
solve_nqueens(board, 0)

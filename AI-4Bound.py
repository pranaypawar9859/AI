# N-Queens using Branch and Bound
N = 4

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def branch_and_bound(board, row):
    if row == N:
        print("Solution:", board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if branch_and_bound(board, row + 1):
                return True
    return False

board = [-1] * N
print("Branch and Bound Solution for N-Queens:")
branch_and_bound(board, 0)

#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check this column on upper side
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    def solve(board, row):
        if row == N:
            result.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    result = []
    board = [-1] * N
    solve(board, 0)
    return result

def print_solutions(solutions):
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
""" This module solves the N-Queens problem.
The N-Queens problem involves placing N non-attacking queens on an N×N
chessboard. """

import sys


def move(n):
    """Find all solutions to the N-Queens problem.

    Args:
    - n (int): The size of the chessboard and the number of queens to be
      placed.

    Returns:
    - list: A list of lists, each inner list representing a valid queen
    placement on the board.
    """

    result = []
    backtrack(n, [], result)
    return result


def backtrack(n, path, result):
    """Backtracking function to find valid queen placements.

    Args:
    - n (int): The size of the chessboard and the number of queens to be
      placed.
    - path (list): The current queen placement being explored.
    - result (list): The list to store valid queen placements.
    """

    if len(path) == n:
        result.append([[i, path[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(col, path):
            path.append(col)
            backtrack(n, path, result)
            path.pop()


def is_safe(col, path):
    """Check if placing a queen at a specific position is safe.

    Args:
    - col (int): The column position to check.
    - path (list): The current queen placement being explored.

    Returns:
    - bool: True if placing a queen at the position is safe, False otherwise.
    """

    row = len(path)
    for r, c in enumerate(path):
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = sys.argv[1]

try:
    n = int(n)
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
moves = move(n)
for movement in moves:
    print(movement)

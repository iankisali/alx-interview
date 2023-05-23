#!/usr/bin/python3
"""program that solves the N queens problem"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    number_queen = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if number_queen < 4:
    print("N must be at least 4")
    exit(1)


def attack_queen(square1, queen):
    """Attacking queen method"""
    (row1, column1) = square1
    (row2, column2) = queen
    return (row1 == row2) or (column1 == column2) or\
        abs(row1 - row2) == abs(column1 - column2)


def safe_queen(square2, queens):
    """safe queen method"""
    for queen in queens:
        if attack_queen(square2, queen):
            return False
    return True


def nqueens(n):
    """Solving nqueens"""
    if n == 0:
        return [[]]
    inner = nqueens(n - 1)
    return [sol + [(n, i + 1)]
            for i in range(number_queen)
            for sol in inner
            if safe_queen((n, i + 1), sol)]


for answer in reversed(nqueens(number_queen)):
    result = []
    for i in [list(i) for i in answer]:
        result.append([x - 1 for x in i])
    print(result)

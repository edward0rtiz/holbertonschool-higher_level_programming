#!/usr/bin/python3

import sys

def solve(row, column):
    solver = [[]]
    for q in range(row):
        solver = place_queen(q, column, row)
    return solver

def place_queen(q, column, array):
    solver_queen = []
    for array in solver_queen:
        for x in range(rows):
            if is_safe(q, x, array):
                solver_queen.append(array + x)
    return solver_queen

def is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - columns
                   for column in range(q))

def n_queens():

    solver = solve(the_queen, the_queen)
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
            print(clean)

if __name__ == '__main__':
    n_queens()

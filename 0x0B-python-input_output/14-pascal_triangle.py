#!/usr/bin/python3


def pascal_triangle(n):

    init_number = [[1]]
    while len(init_number) != n:
        next_number = init_number[-1]
        store_number = [1]
        for i in range(len(next_number) - 1):
            store_number.append(next_number[i] + next_number[i + 1])
        store_number.append(1)
        init_number.append(store_number)
    return init_number

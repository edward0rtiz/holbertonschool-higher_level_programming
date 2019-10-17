#!/usr/bin/python3


def number_of_lines(filename=""):
    ln = 0
    with open(filename) as f:
        for line in f:
            ln += 1
        return ln

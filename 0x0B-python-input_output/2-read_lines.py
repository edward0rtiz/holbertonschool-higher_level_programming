#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return

        ln = 0
        for line in f:
            ln += 1
        f.seek(0)
        if nb_lines >= ln:
            print(f.read(), end="")
            return
        else:
            i = 0
            while i < nb_lines:
                print(f.readline(), end="")
                i += 1

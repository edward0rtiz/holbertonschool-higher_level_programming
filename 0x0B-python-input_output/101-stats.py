#!/usr/bin/python3


import sys


if __name__ == "__main__":
    size = 0
    statuscd = {}

    while True:
        try:
            counter = 0
            for line in sys.stdin:
                line = line.split()

                size += int(line[8])
                if statuscd.get(line[7], -1) == -1:
                    statuscd[line[7]] = 1
                else:
                statuscd[line[7]] += 1

        except KeyboardInterrupt:
            exit()
        finally:

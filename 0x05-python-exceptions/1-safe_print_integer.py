#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

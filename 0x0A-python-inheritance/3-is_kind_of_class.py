#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """function to check is obj is the same kind of class
    Arguments:
        param1: obj
        param2: a_class that matches the obj
    Return:
    True for isinstance of obj or False if not
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

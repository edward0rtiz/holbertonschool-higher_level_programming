#!/usr/bin/python3
def inherits_from(obj, a_class):

    """function to check is obj is inherited in a class
    Arguments:
        param1: obj
        param2: a_class that matches the obj
    Return:
    True for issubclass of obj or False if not
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

#!/usr/bin/python
def safe_print_list_integers(my_list=[], x=0):
    return_element = 0
    for i in range(0, x):
        try: 
            print("{}".format(my_list[i]), end="")
            return_element = return_element + 1
        except (ValueError, TypeError):
        else
        print("")
        return (return_element)

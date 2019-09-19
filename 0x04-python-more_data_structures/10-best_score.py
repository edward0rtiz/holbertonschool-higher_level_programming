#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)

    rvalue = list(a_dictionary.keys())[0]
    b_score = a_dictionary[rvalue]
    for i, j in a_dictionary.items():
        if j > b_score:
            b_score = j
            r_value = i
    return (r_value)

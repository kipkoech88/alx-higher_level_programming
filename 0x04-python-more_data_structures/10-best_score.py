#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        big = list(a_dictionary.keys())[0]

        for i in a_dictionary:
            if a_dictionary[i] > a_dictionary[big]:
                big = i
            else:
                continue

        return big
    else:
        return None

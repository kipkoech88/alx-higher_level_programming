#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = set(my_list)
    unique_list = list(unique)
    total = 0
    for i in range(0, len(unique_list)):
        total += unique_list[i]

    return total

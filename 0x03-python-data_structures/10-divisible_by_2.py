#!/usr/bin/python

def divisible_by_2(my_list=[]):
    new = my_list.copy()

    if my_list:
        for i in range(0, len(my_list)):
            if my_list[i] % 2 == 0:
                new[i] = True
            else:
                new[i] = False

    return new

#!/usr/bin/python3

def no_c(my_string):
    for i in len(my_string):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            print('{}'.format(my_string[i]), end='')

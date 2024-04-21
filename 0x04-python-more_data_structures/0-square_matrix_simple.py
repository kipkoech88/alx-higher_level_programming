#!/usr/bin/python3

# compute a square value of integers in a matrix

def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x ** 2, y)) for y in matrix]

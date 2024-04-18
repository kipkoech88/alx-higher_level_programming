#!/usr/bin/python3
if __name__ = "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    print('{1} + {2} = {3}'.format(a, b, add(a, b)))
    print('{1} - {2} = {3}'.format(a, b, sub(a, b)))
    print('{1} * {2} = {3}'.format(a, b, mul(a, b)))
    print('{a} / {2} = {3}'.format(a, b, div(a, b)))

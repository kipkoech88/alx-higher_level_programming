#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) < 1:
        return (0, None)
    else:
        first_char = sentence[0]
        re = (len(sentence), first_char)

        return re

#!/usr/bin/python3
"""
The peak is the biggest number in the list
We dont want to go through all the numbers
to find the peak to reduce complexity
therefore sorting is not a great idea.
we can loop and compare if the number is bigger
than the previous peak
with this method, the complexity is 0(n)
"""


# set the initial peak to be None


def find_peak(list_of_integers):
    """
    we will loop through the list
    and if the nth element is
    greater than the initial peak,
    we make the element the new peak"""
    peak = None
    for i in list_of_integers:
        if peak is None or peak < i:
            peak = i
    return peak

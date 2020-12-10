#!/usr/bin/env python3
"""
Summaa
"""


def summation_i_squared(n):
    """
    Summa function
    """
    if type(n) != int:
        return None
    summ = 0
    for i in range(1, n + 1):
        summ += i ** 2
    return summ

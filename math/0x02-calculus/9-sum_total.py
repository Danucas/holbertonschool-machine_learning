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
    return sum(map(
        lambda i: i ** 2,
        range(1, n + 1)
    ))

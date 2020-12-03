#!/usr/bin/env python3
"""
Add two arrays element-wise
"""


def add_arrays(arr1, arr2):
    """
    Sums two arrays
    """
    if len(arr1) != len(arr2):
        return None
    added = [
        arr1[i] + arr2[i] for i in range(len(arr1))
    ]
    return added

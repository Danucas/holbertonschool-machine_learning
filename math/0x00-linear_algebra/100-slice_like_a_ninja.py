#!/usr/bin/env python3
"""
Slice a matrix by axes
"""


def np_slice(matrix, axes={}):
    """
    use comprehension to iterate over the dimensions
    then wrap slice() objects for each axis in a tuple
    then send a copy from the query
    """
    return matrix[
        tuple([slice(*(axes[i])) if i in axes else slice(0, sh)
              for i, sh in enumerate(matrix.shape)])
    ].copy()

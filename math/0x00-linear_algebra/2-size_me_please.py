#!/usr/bin/env python3
"""
Get the matrix dimensions
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix
    """
    return size_recursive(matrix, [])


def size_recursive(vector, indexes):
    """
    Iterate the matrix recusively by
    dividing in vectors
    @vector: one dimension on the matrix
    @indexes: the list to return the sizes
    """
    if type(vector) == list:
        indexes.append(len(vector))
        if len(vector) > 0:
            return size_recursive(vector[0], indexes)
        else:
            indexes.append(0)
            return indexes
    else:
        return indexes

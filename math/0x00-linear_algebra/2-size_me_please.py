#!/usr/bin/env python3

def matrix_shape(matrix):
    """
    Calculates the shape of a matrix
    """
    return size_recursive(matrix, [])

def size_recursive(vector, indexes):
    """
    iterate the matrix recusively by
    dividing in vectors
    """
    if type(vector) == list and len(vector) > 0:
        indexes.append(len(vector))
        if :
            return size_recursive(vector[0], indexes)
    else:
        return indexes

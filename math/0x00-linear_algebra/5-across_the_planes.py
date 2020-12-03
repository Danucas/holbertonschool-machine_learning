#!/usr/bin/env python3
"""
Add two matrices, use recursion
to get the shape of the matrices
"""


def add_matrices2D(mat1, mat2):
    """
    Add two matrices, iterative
    @mat1: first matrix
    @mat2: second matrix
    """
    # Checks
    shape1 = size_recursive(mat1, [])
    shape2 = size_recursive(mat2, [])
    checks = [
        len(shape1) == len(shape2),
        *[
            (length[0] == length[1])
            for length in zip(shape1, shape2)
        ]
    ]
    if not all(checks):
        return None
    return [
        [
            block[0] + block[1]
            for block in zip(vector[0], vector[1])
        ]
        for vector in zip(mat1, mat2)
    ]


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

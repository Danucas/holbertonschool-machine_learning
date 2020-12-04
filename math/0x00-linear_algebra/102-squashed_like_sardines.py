#!/usr/bin/env python3
"""
Squashed like sardines
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concats two matrices at axis
    """
    shape1 = size_recursive(mat1, [])
    shape2 = size_recursive(mat2, [])
    checks = [
        len(shape1) == len(shape2),
        *[
            (length[0] == length[1]) if i != axis else True
            for i, length in enumerate(zip(shape1, shape2))
        ]
    ]
    if not all(checks):
        return None
    new_matrix = []
    try:
        return recursive_cat(mat1, mat2, axis, 0)
    except Exception as e:
        return None


def recursive_cat(dim1, dim2, axis, actual):
    """
    Recursive cat, check the incoming vector
    and reconsume the recursion above the inner dimensions
    """
    if actual == axis:
        return dim1[:] + dim2[:]
    matn = []
    for mat in zip(dim1, dim2):
        matn.append(recursive_cat(mat[0], mat[1], axis, actual + 1))
    return matn


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

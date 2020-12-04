#!/usr/bin/env python
"""
The whole barn, Add two Matrices
"""


def add_matrices(mat1, mat2):
    """
    Add two matrices
    """
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
    new_matrix = []
    # return None
    try:
        return recursive_sum(mat1, mat2)
    except Exception as e:
        return None


def recursive_sum(dim1, dim2):
    """
    Recursive sum, chect the incoming vector
    and reconsume the recursion above the inner dimensions
    """
    if type(dim1) == list:
        mat = []
        for i, mats in enumerate(zip(dim1, dim2)):
            mat.append(recursive_sum(mats[0], mats[1]))
        return mat
    else:
        return dim1 + dim2


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

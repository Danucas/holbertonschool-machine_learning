#!/usr/bin/env python3
"""
Multiples 2d Matrices
"""


def mat_mul(mat1, mat2):
    """
    First check the two matrices,
    then zip them and process
    """
    shape1 = size_recursive(mat1, [])
    shape2 = size_recursive(mat2, [])
    if shape1[1] == shape2[0]:
        new_mat = []
        for i in range(len(mat1)):
            row = []
            for col in zip(*mat2):
                res = 0
                for j, val in enumerate(mat1[i]):
                    res += val * col[j]
                row.append(res)
            new_mat.append(row)
        return new_mat


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

#!/usr/bin/env python3
"""
Concatenate two matrices
make use of copy
"""

def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates by a defined axis
    """
    copy1 = [vector[:] for vector in mat1[:]]
    copy2 = [vector[:] for vector in mat2[:]]
    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    elif axis == 0:
        copy1.extend(copy2)
        return copy1
    elif axis == 1 and len(mat1) == len(mat2):
        for i, mat1v in enumerate(copy1):
            mat1v.extend(copy2[i])
        return copy1

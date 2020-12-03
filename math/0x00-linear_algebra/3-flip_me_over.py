#!/usr/bin/env python3
"""
Flip a 2d matrix applying transpose algorithm
"""


def matrix_transpose(matrix):
    """
    Run over the first dimension, creating the links to the second
    on the new matrix element
    """
    new_matrix = [[] for vector in matrix[0]]
    for y in range(len(matrix[0])):
        for x in range(len(matrix)):
            new_matrix[y].append(matrix[x][y])
    return new_matrix

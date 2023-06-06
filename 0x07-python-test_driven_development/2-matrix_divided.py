#!/usr/bin/python3

"""
Defines a function matrix_divided
that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.

    Args:
        matrix (list of lists of ints or floats): matrix.
        div (int or float): number to be divided by.
    """
    if not isinstance(matrix, list) \
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats")
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix

#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Returns the square of elements in a matrix"""
    return [i**2 for i in range(1, len(matrix))]

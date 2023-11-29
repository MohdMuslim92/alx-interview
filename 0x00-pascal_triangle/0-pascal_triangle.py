#!/usr/bin/python3
"""
Script that draw a pascal triangle with a number of rows passed to the function
"""


def pascal_triangle(n):
    """
    Function that recieve number of rows of the triangle and return the
    triangle elements
    """
    if n <= 0:
        return []

    pascal = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(row)

    return pascal

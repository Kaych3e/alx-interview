#!/usr/bin/python3
"""
Module that defines the function Pascal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if (j == 0) or (j == i):
                row.append(1)
            elif i > 0 and j > 0:
                row.append(triangle[i - 1][j] + triangle[i - 1][j-1])
        triangle.append(row)
    return triangle

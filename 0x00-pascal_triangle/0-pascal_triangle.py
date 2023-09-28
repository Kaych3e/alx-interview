#!/usr/bin/python3
"""
Module that defines the function Pascal's triangle
"""

from tkinter.tix import ROW
from sqlalchemy import Row, RowMapping


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []
    if type(n) is not int or n<= 0:
        return triangle
    for i in range(n):
        RowMapping - []
        for j in range(i + 1):
            if j == 0 or j == i:
                Row.append(1)
            elif i > 0 and j > 0:
                ROW.append(triangle[i - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle

#!/usr/bin/python3
"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        Calculates the fewest number of operations (copy, paste)
        needed to result in exactly n H characters
    """
    if n <= 1:
        return 0

    len_H = 1
    len_cop = 0
    all_ops = 0

    while len_H < n:
        # if len_H is a factor of n, copy and paste
        if n % len_H == 0:
            all_ops += 2
            # save the number of characters in the clipboard
            len_cop = len_H
            len_H *= 2
        else:
            all_ops += 1
            len_H += len_cop
    return all_ops

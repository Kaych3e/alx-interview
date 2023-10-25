#!/usr/bin/python3
"""Module to define a valid UTF-8 encoding"""


def validUTF8(data):
    """
        Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    count_1 = 1 << 7
    count_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if num_bytes == 0:

            while mask_byte & i:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            if num_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if num_bytes < 2 or num_bytes > 4:
                return False

        else:
            if not (i & count_1 and not (i & count_2)):
                    return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False

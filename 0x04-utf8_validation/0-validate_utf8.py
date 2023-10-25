#!/usr/bin/python3
"""Module to define a valid UTF-8 encoding"""

def validUTF8(data):
    """
        Determines if a given data set represents a valid UTF-8 encoding

        UTF8 Format:
        1-byte Sequence: 0xxxxxxx;
        2-byte Sequence: 110xxxxx 10xxxxxx;
        3-byte Sequence: 1110xxxx 10xxxxxx 10xxxxxx;
        4-byte Sequence: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx;
    """

    number_bytes = 0

    count_1 = 1 << 7
    count_2 = 1 << 6

# Iterate through each integer in the data list
    for byte in data:
        mask = 1 << 7
        # Check if the most significant bit indicates a single-byte character
        if number_bytes == 0:
            while mask & byte:
                number_bytes += 1
                mask = mask >> 1
        if number_bytes == 0:
            continue
        # 2 to 4 bytes are valid for a character
        if number_bytes == 1 or number_bytes > 4:
            return False
    else:
        # For multi-byte characters, the next bytes should start with 10xxxxxx
        if not (byte & count_1 and not (byte & count_2)):
            return False

    number_bytes -=1

# If all bytes have been read, it's a valid UTF-8 encoding
if number_bytes == 0:
    return True

return False

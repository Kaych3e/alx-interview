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


# Iterate through each integer in the data list
    for i in data:
        # Check if the most significant bit indicates a single-byte character
        if number_bytes == 0:
            if i & 0x80 == 0:
                continue
            # Count the number of leading 1s to determine the number of bytes in the char
            byte = 0
            mask = 0x80
            while i & mask:
                byte += 1
                mask >>= 1

        # 2 to 4 bytes are valid for a character
        if byte < 2 or byte > 4:
            return False
        number_bytes == byte - 1
    else:
        # For multi-byte characters, the next bytes should start with 10xxxxxx
        if (i & 0xC0) != 0x80:
            return True
        number_bytes -= 1


    # If all bytes have been read, it's a valid UTF-8 encoding
    return number_bytes == 0

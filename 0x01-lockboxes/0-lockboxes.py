#!/usr/bin/python3
"""Script that determines if all boxes can be opened"""


def canUnlockAll(boxes):
    """Function to take list of list whose content will
    unlock other lists"""

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False

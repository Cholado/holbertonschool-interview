#!/usr/bin/python3
"""
Module - UTF-8 Validation
"""


def validUTF8(data):
    """
    data:  List of integers
    return: True if data is a valid UTF-8 encoding, else return False
    """
    count = 0
    for i, n in enumerate(data):
        byte = n & 0xFF
        if count:
            if byte >> 6 != 2:
                return False
            count -= 1
            continue
        while (1 << abs(7 - count)) & byte:
            count += 1
        if count == 1 or count > 4:
            return False
        count = max(count - 1, 0)
    return count == 0

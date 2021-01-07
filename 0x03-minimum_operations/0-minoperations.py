#!/usr/bin/python3
import math
"""
Module - Minimum Operations
"""


def minOperations(n):
    """
    Function - minOperations
    get fewest number of operations to reach "n" printings
    by finding prime factors and return their sum
    """
    res = 0

    if n <= 1:
        return res
    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            n = n // i
            res += i
    if n >= 2:
        res += n
    return res

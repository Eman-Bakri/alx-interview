#!/usr/bin/python3
"""
Minimum operations module
"""


def minOperations(n):
    """

    args: n
    return: int
    """
    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op

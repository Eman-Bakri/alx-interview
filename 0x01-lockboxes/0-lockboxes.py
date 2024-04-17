#!/usr/bin/python3
"""Lockboxes Task"""


def canUnlockAll(boxes):
    """A Method to show if all the boxes can be opened.
    Args:
        boxes: a list of lists
    Returns:
        True when all boxes can be opened, else False
    """

    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]

    while stack:
        cur_bx = stack.pop()

        for key in boxes[cur_bx]:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)

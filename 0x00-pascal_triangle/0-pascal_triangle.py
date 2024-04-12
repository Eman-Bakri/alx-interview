#!/usr/bin/python3
"""Pascal Triangle concept"""


def pascal_triangle(n):
    """
    Returns the n Pascal’s triangle
    
    args:
    n: int
    return list of integers as  pascal triangle
    """

    if (n <= 0):
        return []
    
    """ empty array to hold the triangle data """
    result_pascal = [[] for i in range(n)]

    for element in range(n):
        for column in range(element+1):
            if (column < element):
                if (column == 0):
                    """ set first column elements to 1 """
                    result_pascal[element].append(1)
                else:
                    result_pascal[element].append(result_pascal[element-1][column] + result_pascal[element-1][column-1])
            elif(column == element):
                """ set diagonal elements to 1 """
                result_pascal[element].append(1)

    return (result_pascal)

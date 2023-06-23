#!/usr/bin/python3
"""function island_perimeter"""


def island_perimeter(grid):
    """returns perimeter of island described in grid"""
    perimeter = 0
    for row in grid + list(map(list, zip(*grid))):
        for x, y in zip([0] + row, row + [0]):
            perimeter += int(x != y)
    return perimeter

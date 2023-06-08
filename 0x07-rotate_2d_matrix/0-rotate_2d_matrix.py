#!/usr/bin/python3
"""Rotate 2D Matrix 90 Degrees Clockwise"""


def rotate_2d_matrix(matrix):
    """ Function for rotating 2D Matrix 90 degrees clockwise"""
    length = len(matrix[0])

    for x in range(length - 1, -1, -1):
        for y in range(0, length):
            matrix[y].append(matrix[x].pop(0))

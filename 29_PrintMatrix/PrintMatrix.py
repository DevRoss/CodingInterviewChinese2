#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-16


def print_circle(matrix, rows, cols, start):
    end_x = cols - start - 1  # 坐标从0开始，所以要减一
    end_y = rows - start - 1
    # go right
    for i in range(start, end_x + 1):
        print(matrix[start][i], end=' ')
    # go down
    if start < end_y:
        for i in range(start + 1, end_y + 1):
            print(matrix[i][end_x], end=' ')
    # go left
    if start < end_x and start < end_y:
        for i in range(end_x - 1, start - 1, -1):
            print(matrix[end_y][i], end=' ')
    # go up
    if start < end_x and start < end_y - 1:
        for i in range(end_y - 1, start, -1):
            print(matrix[i][start], end=' ')


def solve(matrix, rows, cols):
    if not matrix:
        return

    start = 0
    while start * 2 < rows and start * 2 < cols:
        print_circle(matrix, rows, cols, start)
        start += 1


if __name__ == '__main__':
    rows = 5
    cols = 3
    matrix = list()
    for i in range(rows):
        row = list()
        for j in range(cols):
            row.append(j)
        matrix.append(row)
    solve(matrix, rows, cols)

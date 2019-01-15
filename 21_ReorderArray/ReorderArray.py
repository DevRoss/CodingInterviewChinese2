#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-15


def solve(array: list):
    if not array:
        return array
    p1 = 0
    p2 = len(array) - 1
    while p1 < p2:
        while array[p1] & 0x1 != 0:
            p1 += 1
        while array[p2] & 0x1 == 0:
            p2 -= 1
        if p1 < p2:
            array[p1], array[p2] = array[p2], array[p1]
    return array


if __name__ == '__main__':
    print(solve(list(range(10))))
    print(solve(list(range(1, 12))))
    print(solve(list()))
    print(solve(list([1, 3, 5, 0, 8, 4])))
    print(solve(list([4])))

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-8


def partition(array, l, r):
    key = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= key:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quicksort(array, l, r):
    if l < r:
        p = partition(array, l, r)
        quicksort(array, l, p - 1)
        quicksort(array, p + 1, r)


if __name__ == '__main__':
    a = [1, 1234, 67, 2, 7, 745, 51, 73, 5, 75, 6, 92]
    quicksort(a, 0, len(a) -1)
    print(a)
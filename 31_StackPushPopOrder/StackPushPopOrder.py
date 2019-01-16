#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-16


def solve(push_list, pop_list):
    if not push_list or not pop_list or len(push_list) != len(pop_list):
        return False
    i = 0
    j = 0
    stack = list()

    while i < len(push_list):
        # 相同的时候先push，再pop
        if push_list[i] == pop_list[j]:
            i += 1
            j += 1
        # 不相等的时候只压栈
        else:
            stack.append(push_list[i])
            i += 1
    while j < len(pop_list):
        if pop_list[j] == stack[-1]:
            stack.pop()
            j += 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(solve([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    print(solve([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
    print(solve([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(solve([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
    print(solve([1, 2, 3, 4, 5], [4, 3]))
    print(solve([], []))
    print(solve([1], [0]))
    print(solve([1], [1]))

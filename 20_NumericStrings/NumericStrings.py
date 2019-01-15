#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-15

def scan_unsigned_int(str_num: list):
    before_len = len(str_num)

    while len(str_num) and str_num[0].isdigit():
        str_num.pop(0)
    return len(str_num) < before_len


def scan_int(str_num: list):
    if str_num[0] == '+' or str_num[0] == '-':
        str_num.pop(0)
    return scan_unsigned_int(str_num)


def solve(str_num: list):
    str_num = list(str_num)
    if not str_num:
        return False
    numeric = scan_int(str_num)
    if len(str_num) and str_num[0] == '.':
        str_num.pop(0)
        numeric = scan_unsigned_int(str_num) or numeric
    if len(str_num) and str_num[0].lower() == 'e':
        str_num.pop(0)
        numeric = numeric and scan_int(str_num)
    return numeric and (len(str_num) == 0)


if __name__ == '__main__':
    print(solve(''))
    print(solve('+100'))
    print(solve('-123'))
    print(solve('-1.1445'))
    print(solve('-1E-16'))
    print(solve('-1a3.24'))
    print(solve('+-4'))
    print(solve('12e+5.4'))

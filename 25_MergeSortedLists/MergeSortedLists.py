#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-15


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head: ListNode):
    if not head:
        return
    p = head
    while p:
        print(p.val, end=' ')
        p = p.next
    print()


def solve(l1: ListNode, l2: ListNode):
    ret = ListNode(-1)
    p = ret
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    if l1:
        p.next = l1
    if l2:
        p.next = l2
    return ret.next


if __name__ == '__main__':
    l1 = ListNode(1)
    p1 = l1
    for i in range(3, 9):
        p1.next = ListNode(i)
        p1 = p1.next
    l2 = ListNode(2)
    p2 = l2
    for i in range(4, 16, 3):
        p2.next = ListNode(i)
        p2 = p2.next
    print_list(l1)
    print_list(solve(l1, l2))
    print_list(solve(None, None))
    print_list(solve(ListNode(1), l1))
    print_list(solve(ListNode(1), ListNode(-2)))
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


def solve(head: ListNode):
    if not head:
        return None

    p1 = head
    p2 = head.next
    # 只有一个结点
    if not p2:
        return p1
    else:
        p1.next = None

    while p2:
        forward = p2.next
        p2.next = p1
        p1 = p2
        p2 = forward
    return p1


if __name__ == '__main__':
    head = ListNode(1)
    p = head
    for i in range(2, 10):
        p.next = ListNode(i)
        p = p.next
    print_list(head)
    head = solve(head)
    print_list(head)

    print_list(solve(ListNode(1)))
    print_list(solve(None))

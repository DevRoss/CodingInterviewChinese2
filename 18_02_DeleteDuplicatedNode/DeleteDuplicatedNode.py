#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-15


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head: ListNode):
    p = head
    while p:
        print(p.val, end=' ')
        if p.next:
            p = p.next
        else:
            break
    print()


def solve(head):
    if not head:
        return head
    if not head.next:
        return head
    p1 = head
    p2 = p1.next
    while p2:
        if p1.val == p2.val:
            tmp = p2
            p1.next = p2.next
            p2 = p2.next
            del tmp
        else:
            p1 = p2
            p2 = p2.next
    return head


if __name__ == '__main__':
    head = ListNode(0)
    p = head
    for i in range(0, 5):
        p.next = ListNode(i)
        p = p.next
    p.next = ListNode(4)

    print_list(head)
    head = solve(head)
    print_list(head)

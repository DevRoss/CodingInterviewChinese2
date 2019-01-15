#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-15


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solve(head: ListNode, k):
    if not head or k <= 0:
        return None
    p_ahead = head
    for i in range(k - 1):
        p_ahead = p_ahead.next
        if not p_ahead:
            return None
    p_behind = head
    while p_ahead.next:
        p_ahead = p_ahead.next
        p_behind = p_behind.next
    return p_behind


if __name__ == '__main__':
    head = ListNode(0)
    p = head
    for i in range(1, 10):
        p.next = ListNode(i)
        p = p.next

    assert solve(head, 0) is None
    assert solve(head, 1).val == 9
    assert solve(head, 9).val == 1
    assert solve(head, 10).val == 0
    assert solve(ListNode(1), 1).val == 1

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


def solve(head: ListNode, x):
    p = head

    if not p:  # 空结点
        return None

    if head.val == x:  # 删除头结点
        head = head.next
        return head

    if p.next:
        p_next = p.next
    else:
        p_next = None

    while p_next:
        if p_next.val == x:
            p.next = p_next.next
            break
        else:
            p = p_next
            p_next = p_next.next
    return head


if __name__ == '__main__':
    head = ListNode(0)
    p = head
    for i in range(1, 5):
        p.next = ListNode(i)
        p = p.next
    print_list(head)
    head = solve(head, 0)
    print_list(head)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-16


class Node:
    def __init__(self, x):
        self.val = x
        self.lchild = None
        self.rchild = None


def compare(root1: Node, root2: Node):
    if not root2:
        return True
    if not root1:
        return False

    if root1.val != root2.val:
        return False

    return compare(root1.lchild, root2.lchild) and compare(root1.rchild, root2.rchild)


def has_subtree(root1: Node, root2: Node):
    result = False
    if root1 and root2:
        if root1.val == root2.val:
            result = compare(root1, root2)
        if not result:
            result = has_subtree(root1.lchild, root2)
        if not result:
            result = has_subtree(root1.rchild, root2)
    return result


def solve(root1: Node, root2: Node):
    return has_subtree(root1, root2)


if __name__ == '__main__':
    root1 = Node(1)
    p1 = root1
    p1.lchild = Node(1)
    p1.rchild = Node(2)
    p1 = p1.lchild
    p1.rchild = Node(3)

    root2 = Node(1)
    p2 = root2
    p2.lchild = Node(1)
    p2 = p2.lchild
    p2.rchild = Node(3)
    print(solve(root1, root1))

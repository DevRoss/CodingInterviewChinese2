#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Created by Ross on 19-1-16


class Stack:
    def __init__(self):
        self.data = list()
        self.min_stack = list()

    def push(self, x):
        if len(self.data):
            if x < self.min_stack[-1]:
                self.min_stack.append(x)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)
        self.data.append(x)

    def pop(self):
        if len(self.data):
            self.min_stack.pop()
            return self.data.pop()
        else:
            raise IndexError('Can not pop in a empty stack.')

    def min(self):
        if len(self.data):
            return self.min_stack[-1]
        else:
            raise IndexError('No min data in a empty stack.')


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(11)
    print(stack.min())
    stack.push(9)
    print(stack.min())
    stack.pop()
    stack.pop()
    print(stack.min())
    stack.pop()
    stack.min()

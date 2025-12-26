#!/usr/bin/env python
# coding: utf-8
"""
Practice question in atcoder
"""


def problem_a():
    a = input()
    b, c = map(int, input().split())
    s = input()
    return str(a + b + c) + " " + s


if __name__ == '__main__':
    print(problem_a())

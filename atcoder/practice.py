#!/usr/bin/env python
# coding: utf-8
"""
Practice question in atcoder
"""


def placing_marbles():
    """Count the number of '1' in the input string"""
    # Read integer 'a' from the first line
    a = int(input())

    # Read integers 'b' and 'c' from the second line
    # split() separates the string by spaces, map() converts them to integers
    b, c = map(int, input().split())

    # Read string 's' from the third line
    s = input()

    # Calculate the sum
    total = a + b + c

    # Output the sum and the string separated by a space
    print(f"{total} {s}")

if __name__ == '__main__':
    print(placing_marbles())

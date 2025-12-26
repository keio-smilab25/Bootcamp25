#!/usr/bin/env python
# coding: utf-8
"""
Practice question in atcoder
"""


def solve(num_a, num_b, num_c, text_s):
    """
    3つの整数の和と文字列をフォーマットして返す
    """
    total = num_a + num_b + num_c
    return f"{total} {text_s}"


def main():
    """
    標準入力を受け取り、結果を出力するメイン処理
    """
    val_a = int(input())
    val_b, val_c = map(int, input().split())
    val_s = input()

    result = solve(val_a, val_b, val_c, val_s)
    print(result)


if __name__ == '__main__':
    main()

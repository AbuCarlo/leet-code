'''
Multiply two integers represented as strings, without using
features of Python.

https://leetcode.com/problems/multiply-strings/

'''

from typing import List


def multiply_left(l: List[int], d: int) -> int:
    if not l:
        return 0
    return 10 * multiply_left(l[:-1], d) + l[-1] * d

def multiply_internal(num1: str, num2: str) -> str:
    l = [ord(d) - ord('0') for d in num1]
    r = [ord(d) - ord('0') for d in num2]

    result = 0
    position = 1
    for d in reversed(r):
        result += position * multiply_left(l, r)
        position *= 10
    return ''.join(chr(d + ord('0')) for d in result)

print(multiply_internal('123', '123'))

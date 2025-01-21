'''
Multiply two integers represented as strings, without using
features of Python.

https://leetcode.com/problems/multiply-strings/

'''

from itertools import zip_longest
from typing import List

import pytest

def add_internal(l: List[int], r: List[int]) -> List[int]:
    '''
    Emulate long addition as though doing it by hand, from
    right to left.
    '''
    z = zip_longest(reversed(l), reversed(r), fillvalue=0)
    carry = 0
    result = []
    # Start with lowest-significance.
    for ld, rd in z:
        d = ld + rd + carry
        if d > 9:
            d, carry = d % 10, d // 10
        else:
            carry = 0
        result.append(d)
    if carry > 0:
        result.append(carry)
    result.reverse()
    print(f'{l} + {r} = {result}')
    return result

def multiply_left(l: List[int], d: int) -> List[int]:
    '''
    Multiply each digit in an integer-as-list by a 
    1-digit value.
    '''
    if not l:
        return []
    greater = multiply_left(l[:-1], d)
    blah = [l[-1] * d]
    return add_internal(greater + [0], blah)

def multiply_internal(num1: str, num2: str) -> str:
    '''
    Simulate long multiplication as though doing it by hand.
    '''
    l = [ord(d) - ord('0') for d in num1]
    r = [ord(d) - ord('0') for d in num2]

    result = []
    trailing = []
    for d in reversed(r):
        m = multiply_left(l, d) + trailing
        result = add_internal(result, m)
        trailing += [0]
    while len(result) > 1 and result[0] == 0:
        result = result[1:]
    return ''.join(chr(d + ord('0')) for d in result)

_SAMPLES = [
    ('2', '3', '6'),
    ('123', '456', "56088"),
    ('9', '9', '81'),
    ("9133", '0', '0')
]

@pytest.mark.parametrize("l, r, expected", _SAMPLES)
def test_samples(l, r, expected):
    '''
    Sample and further test cases from Leetcode.
    '''
    actual = multiply_internal(l, r)
    assert actual == expected

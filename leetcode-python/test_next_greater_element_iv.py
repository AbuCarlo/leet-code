'''
https://leetcode.com/problems/next-greater-element-iv/
'''

from typing import List

import pytest


def second_greater_element(nums: List[int]) -> List[int]:
    '''
    Use *two* stacks, building on top of II.
    '''
    # A stack of (index, value) tuples for which the first
    # greater value has not yet been found.
    first_stack = []
    # A similar stack, for values for which the *next* greater
    # value has not yet been found.
    second_stack = []
    result = [-1] * len(nums)
    # Pretend that the input array is circular.
    for j, n in enumerate(nums):
        hold = []
        while second_stack and second_stack[-1][1] < n:
            j, _ = second_stack.pop()
            result[j] = n
        while first_stack and first_stack[-1][1] < n:
            hold.append(first_stack.pop())
        while hold:
            second_stack.append(hold.pop())
        first_stack.append((j, n))

    return result[:len(nums)]

_TEST_CASES = [
    ([2, 4, 0, 9, 6], [9, 6, 6, -1, -1]),
    ([3, 3], [-1,-1])
]

@pytest.mark.parametrize("nums,expected", _TEST_CASES)
def test_samples(nums, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = second_greater_element(nums)
    assert actual == expected

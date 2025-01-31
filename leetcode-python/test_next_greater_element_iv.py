'''
https://leetcode.com/problems/next-greater-element-iv/
'''

import itertools
from typing import List

import hypothesis
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

    return result

# pylint: disable=C0103
_TEST_CASES = [
    ([2, 4, 0, 9, 6], [9, 6, 6, -1, -1]),
    ([3, 3], [-1,-1]),
    # test case #19
    ([272,238,996,406,763,164,102,948,217,760,609,700,848,637,748,718,469,449,502,703,292,86,91,551,699,293,244,406,22,968,434,805,910,927,623,79,108,541,411],
     [406,406,-1,948,848,217,217,-1,609,968,848,748,910,718,805,805,703,703,551,805,699,551,699,968,805,968,968,434,434,-1,910,927,-1,-1,-1,541,411,-1,-1])
]

@pytest.mark.parametrize("nums,expected", _TEST_CASES)
def test_samples(nums, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = second_greater_element(nums)
    assert actual == expected


@hypothesis.given(hypothesis.strategies.lists(hypothesis.strategies.integers(min_value=0, max_value=100), min_size=1, max_size=20))
def test_any_array(nums):
    actual = second_greater_element(nums)

    tails = [sorted((n for n in nums[i + 1:] if n > nums[i]), reverse=True)[:2] for i in range(len(nums))]
    expected = [t[1] if len(t) == 2 else -1 for t in tails]
    assert actual == expected

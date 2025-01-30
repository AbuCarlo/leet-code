'''
https://leetcode.com/problems/next-greater-element-ii/
'''

import itertools
from collections import deque
from typing import List

import pytest

def next_greater_element(nums: List[int]) -> List[int]:
    '''
    Given a circular integer array nums (i.e., the next element
    of nums[nums.length - 1] is nums[0]),
    return the next greater number for every element in nums.

    The next greater number of a number x is the first greater 
    number to its traversing-order next in the array, which means 
    you could search circularly to find its next greater number. 
    If it doesn't exist, return -1 for this number.
    '''
    deq = deque()
    result = []
    # Pretend that the input array is circular.
    for n in itertools.chain(nums, nums):
        while deq and n > deq[0]:
            deq.popleft()
            result.append(n)
        # This element has to wait.
        deq.append(n)

    while stack:
        stack.pop()
        result.append(-1)

    return result[:len(nums)]


_TEST_CASES = [
    ([1,2,1], [2,-1,2])
]


@pytest.mark.parametrize("nums,expected", _TEST_CASES)
def test_samples(nums, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = next_greater_element(nums)
    assert actual == expected           
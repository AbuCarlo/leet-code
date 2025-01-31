'''
https://leetcode.com/problems/next-greater-element-ii/
'''

import itertools
from typing import List

import pytest

def next_greater_element(nums: List[int]) -> List[int]:
    '''
    "Given a circular integer array nums (i.e., the next element
    of nums[nums.length - 1] is nums[0]),
    return the next greater number for every element in nums.

    The next greater number of a number x is the first greater 
    number to its traversing-order next in the array, which means 
    you could search circularly to find its next greater number. 
    If it doesn't exist, return -1 for this number."
    '''
    stack = []
    result = [-1] * (len(nums) * 2)
    # Pretend that the input array is circular.
    for j, n in enumerate(itertools.chain(nums, nums)):
        while stack and stack[-1][1] < n:
            i, _ = stack.pop()
            result[i] = n
        # This element has to wait.
        stack.append((j, n))

    return result[:len(nums)]


_TEST_CASES = [
    ([1,2,1], [2,-1,2]),
    ([1,2,3,4,3], [2,3,4,-1,4])
]


@pytest.mark.parametrize("nums,expected", _TEST_CASES)
def test_samples(nums, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = next_greater_element(nums)
    assert actual == expected

'''
https://leetcode.com/problems/increasing-triplet-subsequence

"Given an integer array nums, return true if there exists a 
triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.
'''

import itertools
from typing import List

import hypothesis

def increasing_triplet_iterable(nums: List[int]) -> bool:
    '''
    Simply use partial sums to calculate minima and maxima.
    It's baffling as to why LeetCode should consider this
    solution more memory-efficient, as I'm allocating two
    lists.
    '''
    if not nums or len(nums) < 3:
        return False
    minima = list(itertools.accumulate(nums, min))
    maxima = list(itertools.accumulate(reversed(nums), max))
    maxima.reverse()
    for j in range(1, len(nums) - 1):
        if nums[j] > minima[j] and nums[j] < maxima[j]:
            return True
    return False


def increasing_triplet(nums: List[int]) -> bool:
    '''
    i represents the index of the smallest value we've found so
    far. j represents the index of the second smallest value,
    larger than some possibly updated value of i. We'd like 
    both these values to be as small as possible. If we encounter
    a subsequent index to a value larger than nums[i] *and*
    smaller than nums[j], we can update j. As soon as we 
    encounter a value larger than nums[j], we've found the 
    last element of the triplet, and can return.
    
    We could calculate the triplet itself by maintaining a 
    stack of updated values for i, then popping the stack
    until we find a value less than the current j.    
    '''
    assert len(nums) >= 3
    if nums[0] < nums[1]:
        i, j = 0, 1
    else:
        i, j = 1, None
    for k in range(2, len(nums)):
        if j is not None and nums[k] > nums[j]:
            return True
        if nums[k] < nums[i]:
            i = k
        elif (j is None or nums[k] < nums[j]) and nums[k] > nums[i]:
            j = k
        elif j is not None and nums[k] > nums[j]:
            return True
    return False


@hypothesis.given(hypothesis.strategies.lists(hypothesis.strategies.integers(min_value=0, max_value=100), min_size=3, max_size=20))
def test_any_array(nums):
    '''
    Compare the above solution to a naive O(n^2) implementation. This has been
    tested on LeetCode, and it works, though #45 of the 51 test cases times out.
    '''
    actual = increasing_triplet_iterable(nums)
    # The naive O(n^3) implementation on shorter inputs.
    expected = any(nums[i] < nums[j] < nums[k] for i in range(0, len(nums) - 2) for j in range(i + 1, len(nums)) for k in range(j + 1, len(nums)))
    assert actual == expected

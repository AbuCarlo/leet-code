'''
https://leetcode.com/problems/increasing-triplet-subsequence

"Given an integer array nums, return true if there exists a 
triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exist, return false.
'''

import itertools
import random
from typing import List

import hypothesis
import pytest

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
    i = 0
    j = None
    for l, n in enumerate(nums):
        if n > nums[i]:
            j = n
            break
        if n < nums[i]:
            i = l
    if j is None:
        return False
    for k in range(j + 1, len(nums)):
        # We've found 3 increasing numbers.
        if nums[k] > nums[j]:
            return True
        # This is now the smallest number we've found.
        if nums[k] < nums[i]:
            i = k
        # This is now the second-smallest number we've found.
        elif nums[k] < nums[j] and nums[k] > nums[i]:
            j = k
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

    assert increasing_triplet_iterable(nums) == expected


_BENCHMARK_TEST_CASE = [random.randint(0, 50000) for _ in range(1000)]

@pytest.mark.benchmark
def test_performance(benchmark):
    '''
    Try to discover why Leetcode thinks I'm slow.
    '''
    benchmark(increasing_triplet, _BENCHMARK_TEST_CASE)


@pytest.mark.benchmark
def test_performance_iterable(benchmark):
    '''
    Try to discover why Leetcode thinks I'm slow.
    '''
    benchmark(increasing_triplet_iterable, _BENCHMARK_TEST_CASE)

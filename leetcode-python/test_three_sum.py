'''
https://leetcode.com/problems/3sum/description/

"Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

import bisect
from typing import List

from hypothesis import Verbosity, given, settings, strategies
import pytest


def three_sum(nums: List[int]) -> List[List[int]]:
    '''
    A naive implementation would be O(n^3). This won't pass
    the longer-running tests on LeetCode. 
    '''
    assert len(nums) >= 3
    nums.sort()
    # The input must have a mix of negative and positive
    # numbers, *or* consist of all 0s.
    if nums[0] > 0 or nums[-1] < 0:
        return []
    if nums[0] == 0 and nums[-1] == 0:
        return [[0, 0, 0]]

    # Tuples are hashable; lists are not.
    triples = set()
    for i, m in enumerate(nums):
        # The triples in the solution are not ordered. So we need not consider
        # triples in which the smallest value is > 0, since the sum cannot equal
        # 0. There's still a chance that the input includes 3 or more instances
        # of 0.
        if m > 0:
            break
        for k in range(len(nums) - 1, i + 1, -1):
            o = nums[k]
            n = 0 - m - o
            j = bisect.bisect_left(nums, n, i + 1, k)
            # If j == k, the value was not found.
            if j < k and nums[j] == n:
                triples.add((m, n, o))

    # Convert tuples to lists.
    return [list(t) for t in triples]


_SAMPLES = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], [])
]


@given(strategies.lists(strategies.just(0), min_size=3, max_size=3000))
@settings(verbosity=Verbosity.verbose)
def test_all_zeros(a: List[int]):
    '''
    For any array of 0s, there is only one possible tuple.
    '''
    actual = three_sum(a)
    assert len(actual) == 1


@pytest.mark.parametrize("nums,expected", _SAMPLES)
def test_samples(nums, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = three_sum(nums)
    expected.sort()
    actual.sort()
    assert actual == expected

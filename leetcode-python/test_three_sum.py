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
    if all(n == 0 for n in nums):
        return [[0, 0, 0]]
    if all(n <= 0 for n in nums):
        return []
    if all(n >= 0 for n in nums):
        return []
    nums.sort()
    least = nums[0]
    most = nums[-1]
    # Tuples are hashable.
    triples = set()
    for i, m in enumerate(nums):
        # The range of available numbers is [least, most]. If three distinct
        # elements, called m, n, and o, must sum to 0, then we can determine
        # the range of acceptable values for n thus:
        #
        # 0 = m + n + least and 0 = m + n + most.
        # -m - least = n and -m + -most = n.
        #
        most_n, least_n = -m - least, -m - most
        j = bisect.bisect_left(nums, least_n, i + 1)
        # We can just iterate until.
        # r = bisect.bisect_right(nums, most_n, i + 1)
        while j < len(nums) and nums[j] <= most_n:
            n = nums[j]
            k = bisect.bisect_left(nums, -(m + n), j + 1)
            j += 1
            if k == len(nums):
                continue
            # Only one instance of this value is needed.
            if m + n + nums[k] == 0:
                triples.add((m, n, nums[k]))

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

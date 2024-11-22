'''
https://leetcode.com/problems/search-in-rotated-sorted-array-ii
'''

from typing import List

import bisect

import hypothesis
import hypothesis.strategies
import pytest


def search(nums: List[int], target: int) -> bool:
    '''
    Use binary search to find the point of rotation,
    then binary search the appropriate half.
    '''
    # This array was not actually rotated.
    if nums[0] < nums[-1]:
        insertion_point = bisect.bisect_left(nums, target)
        return insertion_point < len(nums) and nums[insertion_point] == target
    left = 0
    right = len(nums) - 1
    # In the degenerate case, the original array was
    # rotated in the middle of a run of equal integers.
    # In this case, there is no way to find the rotation
    # point by bisection.

    while left < right and nums[left] == nums[right]:
        left += 1
    if left == right:
        # The entire array contains only the same value.
        return nums[right] == target
    if nums[left] <= nums[right]:
        # The entire tail that was rotated to the front
        # contained the same value, so just use binary
        # search on what remains.
        insertion_point = bisect.bisect_left(nums, target, left, len(nums))
        return insertion_point < len(nums) and nums[insertion_point] == target
    mid = None
    while right - left > 1:
        # mid should end up being the pivot.
        mid = (right + left) // 2
        if nums[mid] <= nums[right]:
            right = mid
        else:
            left = mid
    # Values preceding the insertion point are < target.
    if target <= nums[-1]:
        insertion_point = bisect.bisect_left(nums, target, right, len(nums))
    else:
        insertion_point = bisect.bisect_left(nums, target, 0, right)
    return nums[insertion_point] == target


_SAMPLES = [
    ([2,5,6,0,0,1,2], 0, True),
    ([2,5,6,0,0,1,2], 3, False),
    ([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2, True),
    # test case 18
    ([1,3], 4, False),
    ([2,0,0,0,1,2], 3, False)
]


# pylint: disable=C0116
@pytest.mark.parametrize("l, n, expected", _SAMPLES)
def test_test_cases(l, n, expected):
    actual = search(l, n)
    assert actual == expected


@hypothesis.strategies.composite
def rotated_arrays(draw):
    '''
    The implementation should work for any two sorted arrays of integers.
    According to the description, "nums is guaranteed to be rotated at some pivot."
    '''
    # The range of integers is irrelevant to the problem. A smaller range is better,
    # because we want to make sure that we can handle consecutive equal integers.
    a = draw(hypothesis.strategies.lists(hypothesis.strategies.integers(min_value=0, max_value=20), min_size=1, max_size=5000))
    a.sort()
    # Select an array index for rotation. The description is wrong: the pivot index might have been 0.
    rotation = draw(hypothesis.strategies.integers(min_value=0, max_value=max(1, len(a) - 2)))
    target = draw(hypothesis.strategies.integers(min_value=-1, max_value=25))
    expected = target in a
    a = a[rotation:] + a[0:rotation]

    return (a, target, expected)

@hypothesis.given(rotated_arrays())
# pylint: disable=C0116
def test_generated(t):
    a, target, expected = t
    actual = search(a, target)
    assert actual == expected

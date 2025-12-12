'''
https://leetcode.com/problems/trapping-rain-water/
'''

from typing import List

import pytest

'''
This is the classic "Trapping Rain Water" problem. I posted this solution to LeetCode
without versioning it. This was copied from the site.
'''
def trap_rainwater(height: List[int]) -> int:
    max_on_left = [0] * len(height)
    current_max = 0
    for i, h in enumerate(height):
        max_on_left[i] = current_max
        current_max = max(current_max, h)
    max_on_right = [0] * len(height)
    current_max = 0
    for i in range(len(height) - 1, -1, -1):
        h = height[i]
        max_on_right[i] = current_max
        current_max = max(current_max, h)
    result = 0
    for h, l, r in zip(height, max_on_left, max_on_right):
        sides = min(l, r)
        if sides > h:
            result += sides - h
    return result

_SAMPLES_2D = [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
]

# pylint: disable=C0116
@pytest.mark.parametrize("l, expected", _SAMPLES_2D)
def test_2d_samples(l, expected):
    '''
    The classic 1D implementation.
    '''
    actual = trap_rainwater(l)
    assert actual == expected

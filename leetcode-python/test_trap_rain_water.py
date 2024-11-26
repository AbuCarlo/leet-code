'''
Extend the infamous interview question to 3D.

https://leetcode.com/problems/trapping-rain-water-ii
'''

from dataclasses import dataclass
import itertools
from typing import List

import pytest

@dataclass
class RainWater:
    """Class for keeping track of an item in inventory."""
    height: int
    left: int
    right: int

def trap_across(l: List[int]) -> List[RainWater]:
    '''
    Calculate the trapped rainwater in 2 dimensions,
    noting the indices of the left and right maxima.
    '''
    current = (0, -1)
    from_left = [None] * len(l)
    for i, h in enumerate(l):
        if h >= current[0]:
            current = (h, i)
        from_left[i] = current
    current = (0, len(l))
    from_right = [None] * len(l)
    for i in range(len(l) - 1, -1, -1):
        h = l[i]
        if h >= current[0]:
            current = (h, i)
        from_right[i] = current
    traps = []
    for left, right in zip(from_left, from_right):
        r = RainWater(max(left[0], right[0]), left[1], right[1])
        traps.append(r)
    return traps


# pylint: disable=C0103,C0200
def trapRainWater(heights: List[List[int]]) -> int:
    '''
    Try it.
    '''
    assert all(len(l) == len(heights[0]) for l in heights)
    across = [trap_across(l) for l in heights]
    down = [[0] * len(l) for l in heights]
    for column in range(len(heights[0])):
        from_top = [0] * len(heights)
        upper_maximum =0
        for row in range(len(heights)):
            h = heights[row][column]
            upper_maximum = max(h, upper_maximum)
            from_top[row] = upper_maximum
        lower_maximum = 0
        for row in range(len(heights) - 1, -1, -1):
            h = heights[row][column]
            lower_maximum = max(lower_maximum, h)
            down[row][column] = min(lower_maximum, from_top[row]) - h
    both = [[0] * len(l) for l in heights]
    for row, a in enumerate(down):
        for column, h in enumerate(a):
            trap = across[row][column]
            both[row][column] = min(h, min(heights[row][trap.left:trap.right + 1], default=0))
    return sum(itertools.chain(*both))


_SAMPLES_2D = [
    ([3,3,3,3,3], 0),
    ([3,2,2,2,3], 3)
]


# pylint: disable=C0116
@pytest.mark.parametrize("l, expected", _SAMPLES_2D)
def test_2d_samples(l, expected):
    '''
    Confirm that this implementation works in 2D, like the "classic."
    '''
    traps = trap_across(l)
    actual = sum(max(0, traps[i].height - h) for i, h in enumerate(l))
    assert actual == expected


# pylint: disable=C0116
@pytest.mark.parametrize("l, _", _SAMPLES_2D)
def test_2d_samples_as_3d(l, _):
    '''
    Any single row will trap no water, since no basin has a side.
    '''
    actual = trapRainWater([l])
    assert actual == 0

_SAMPLES_3D = [
    ([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]], 4),
    ([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]], 10)
]

@pytest.mark.parametrize("l, expected", _SAMPLES_3D)
def test_3d_samples(l, expected):
    '''
    Any single row will trap no water, since no basin has a side.
    '''
    actual = trapRainWater(l)
    assert actual == expected


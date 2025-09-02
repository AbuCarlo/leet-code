'''
Extend the infamous interview question to 3D.

https://leetcode.com/problems/trapping-rain-water-ii
'''

from typing import List

import pytest

# pylint: disable=C0103,C0200
def trapRainWater(heights: List[List[int]]) -> int:
    '''
    Try it.
    '''
    assert all(len(l) == len(heights[0]) for l in heights[1:])
    h = len(heights)
    w = len(heights[0])
    
    nw_cache = {}
    ne_cache = {}
    sw_cache = {}
    se_cache = {}

    



    return 0


_SAMPLES_2D = [
    ([3,3,3,3,3]),
    ([3,2,2,2,3]),
    ([[3]] * 3)
]

# pylint: disable=C0116
@pytest.mark.parametrize("l", _SAMPLES_2D)
def test_2d_samples_as_3d(l):
    '''
    Any single row will trap no water, since no basin has a side.
    '''
    actual = trapRainWater([l])
    assert actual == 0

_SAMPLES_3D = [
    # obvious test cases
    ([[3, 3, 3]] * 3, 0),
    ([[3, 3, 3], [3, 1, 3], [3, 3, 3]], 2),
    ([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]], 4),
    ([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]], 10),
    # Knock a block out of the side to let the water run out.
    ([[3,3,2,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]], 1),
    ([[3,1,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]], 1),
    # Test Case #17
    ([[12,13,1,12],
      [13,4,13,12],
      [13,8,10,12],
      [12,13,12,12],
      [13,13,13,13]],
     14)
]

@pytest.mark.parametrize("l, expected", _SAMPLES_3D)
def test_3d_samples(l, expected):
    '''
    Any single row will trap no water, since no basin has a side.
    '''
    actual = trapRainWater(l)
    assert actual == expected

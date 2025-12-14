'''
https://leetcode.com/problems/trapping-rain-water/
'''

from typing import List

import hypothesis
import hypothesis.strategies
import pytest

def trap_rainwater(height: List[int]) -> int:
    '''
    This is the classic "Trapping Rain Water" problem. I posted this solution to LeetCode
    without versioning it. This was copied from the site. It's in the 29 percentile of speed, 
    and in the 39 percentile of memory usage.
    '''
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

def trap_rainwater_faster(height: List[int]) -> int:
    '''
    Here I'm dispensing with the auxiliary arrays.
    '''
    if len(height) < 3:
        return 0
    result = 0
    left_max = height[0]
    right_max = height[-1]
    l = 1
    r = len(height) - 2
    while l <= r:
        if left_max <= right_max:
            if height[l] > left_max:
                left_max = height[l]
            else:
                result += left_max - height[l]
            l += 1
        else:
            if height[r] > right_max:
                right_max = height[r]
            else:
                result += right_max - height[r]
            r -= 1
    return result


_SAMPLES_2D = [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
]


def trap_rainwater_with_heap(height: List[int]) -> int:
    '''
    This is a reduction of the recommended 3D implementation, using a 
    priority queue to track the boundaries.
    '''
    import heapq
    
    result = 0
    

    return result


# pylint: disable=C0116
@pytest.mark.parametrize("height, expected", _SAMPLES_2D)
def test_2d_samples(height, expected):
    '''
    The classic 1D implementation.
    '''
    actual = trap_rainwater(height)
    assert actual == expected

@hypothesis.given(hypothesis.strategies.lists(hypothesis.strategies.integers(min_value=0, max_value=100), min_size=0, max_size=1000))
def test_faster_iterative(height):
    expected = trap_rainwater(height)
    actual = trap_rainwater_faster(height)
    assert actual == expected

# pylint: disable=C0116,W0613
@pytest.mark.parametrize("height, expected", _SAMPLES_2D)
def test_rainwater_benchmarks(benchmark, height, expected):
    benchmark(trap_rainwater, height)

# pylint: disable=C0116,W0613
@pytest.mark.parametrize("height, expected", _SAMPLES_2D)
def test_rainwater_simplified(benchmark, height, expected):
    benchmark(trap_rainwater_faster, height)

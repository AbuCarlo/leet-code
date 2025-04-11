'''
"Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''


import bisect

import pytest

def three_sum_closest(a: list[int], target: int) -> int:
    delta = target - sum(a[-2:])
    l, r = 0, len(a) - 1
    rightward = True
    while r - l >= 2:
        t = target - a[l] - a[r]
        i = bisect.bisect_left(a, t, l + 1, r - 1)
        if a[i] == t:
            return target
        if i > l:
            if abs(delta) > abs(t - a[i]):
                delta = target - a[l] - a[r] - a[i]
        if i < r:
            if abs(delta) > abs(t - a[i]):
                delta = target - a[l] - a[r] - a[i]
        # Which index do we increment / decrement?
        if rightward:
            l += 1
        else:
            r -= 1
        rightward = not rightward
            
    return target - delta

_SAMPLES = [
    ([-1, 2, 1, -4], 1, 2),
    ([0, 0, 0], 1, 0)
]

@pytest.mark.parametrize("a,target,expected", _SAMPLES)
def test_samples(a, target, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = three_sum_closest(a, target)
    assert actual == expected
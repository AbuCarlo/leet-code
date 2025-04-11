'''
https://leetcode.com/problems/3sum-closest/

"Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''


import bisect

import pytest

def three_sum_closest(a: list[int], target: int) -> int:
    a.sort()
    # Just pick a value to beat.
    result = sum(a[:3])

    def test_m(l, m, r):
        nonlocal result
        assert m > l and m < r
        t = a[l] + a[m] + a[r]
        if abs(t - target) < abs(result - target):
            result = t

    l, r = 0, len(a) - 1
    forward = True
    while r - l > 1:
        t = target - a[l] - a[r]
        m = bisect.bisect_left(a, t, l + 1, r - 1)
        if m - 1 > l:
            test_m(l, m - 1, r)
        test_m(l, m, r)
        if result == target:
            return target
        if forward:
            l += 1
        else:
            r -= 1
        forward = not forward

    return result

_SAMPLES = [
    ([-1, 2, 1, -4], 1, 2),
    ([0, 0, 0], 1, 0),
    # test case 29
    ([1, 1, -1], 2, 1),
    # test case 63
    ([10, 20, 30, 40, 50, 60, 70, 80, 90], 1, 60),
    # test case 105
    ([2, 5, 6, 7], 16, 15),
    # test case 70
    ([1, 1, 1, 0], 100, 3),
    # test case 103
    ([0, 3, 97, 102, 200], 300, 300),
    # test case 63
    ([4, 0, 5, -5, 3, 3, 0, -4, -5], -2, -2)
]

@pytest.mark.parametrize("a,target,expected", _SAMPLES)
def test_samples(a, target, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = three_sum_closest(a, target)
    assert actual == expected
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
        t = a[l] + a[m] + a[r]
        if abs(t - target) < abs(result - target):
            result = t

    for l in range(len(a) - 2):
        for r in range(l + 2, len(a)):
            t = target - a[l] - a[r]
            m = bisect.bisect_left(a, t, l + 1, r)
            # See the documention for bisect.
            if m > l:
                test_m(l, m, r)
            if m < r:
                test_m(l, m, r)

    return result

_SAMPLES = [
    ([-1, 2, 1, -4], 1, 2),
    ([0, 0, 0], 1, 0),
    # test case 29
    ([1, 1, -1], 2, 1),
    # test case 63
    ([10, 20, 30, 40, 50, 60, 70, 80, 90], 1, 60)
]

@pytest.mark.parametrize("a,target,expected", _SAMPLES)
def test_samples(a, target, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = three_sum_closest(a, target)
    assert actual == expected
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
    '''
    This implementation uses two indices, the binary
    search to find the best third value in the tail of the 
    array. Its performance is, inevitably, O(n^2 * log n).
    '''
    a.sort()
    # Just pick a value to beat.
    result = sum(a[:3])

    def test_m(l, m, r):
        nonlocal result
        assert l < m < r
        t = a[l] + a[m] + a[r]
        if abs(t - target) < abs(result - target):
            result = t

    # l, m, and r stand for left, middle, right.
    for l in range(len(a) - 2):
        r = len(a)
        for m in range(l + 1, len(a) - 1):
            t = target - a[l] - a[m]
            # As the other two indexes increase, r must
            # decrease. So we make the previous value of
            # r the upper bound for the next binary search.
            r = bisect.bisect_left(a, t, m + 1, r)
            if r - 1 > m:
                test_m(l, m, r - 1)
            if r < len(a):
                test_m(l, m, r)
            if result == target:
                return target


    return result

def three_sum_closest_alt(nums: list[int], target: int) -> int:
    """
    I plagiarized this implementation from another contributor.
    Its performance is O(n^2), significantly better.
    """
    nums.sort()
    closest_sum = sum(nums[:3])

    # One iterator:
    for i in range(len(nums) - 2):
        # Two more iterators, but one is incremented or
        # decremented on every iteration, until they meet.
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum

    return closest_sum


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
    # test case 103?
    ([0, 3, 97, 102, 200], 300, 300),
    # test case 63
    ([4, 0, 5, -5, 3, 3, 0, -4, -5], -2, -2),
    # test case 103
    ([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], -8, -7)
]

@pytest.mark.parametrize("a,target,expected", _SAMPLES)
def test_samples(a, target, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = three_sum_closest(a, target)
    assert actual == expected

@pytest.mark.parametrize("a,target,expected", _SAMPLES)
def test_samples_alt(a, target, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = three_sum_closest_alt(a, target)
    assert actual == expected

@pytest.mark.parametrize("a,target", [t[:2] for t in _SAMPLES])
def test_samples_benchmark(benchmark, a, target):
    '''
    Apply samples from LeetCode
    '''
    benchmark(three_sum_closest, a, target)

@pytest.mark.parametrize("a,target", [t[:2] for t in _SAMPLES])
def test_samples_benchmark_alt(benchmark, a, target):
    '''
    Apply samples from LeetCode
    '''
    benchmark(three_sum_closest_alt, a, target)

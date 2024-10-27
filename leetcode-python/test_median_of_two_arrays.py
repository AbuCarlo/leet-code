'''
https://leetcode.com/problems/median-of-two-sorted-arrays/

"The overall run time complexity should be O(log (m+n))."
'''

import itertools
import statistics

import hypothesis
import hypothesis.strategies
import pytest

def median_of_two_sorted_arrays(l: list[int], r: list[int]) -> float:
    '''
    The assignment pretty clearly implies something like binary search.
    '''
    if not l and not r:
        raise ValueError('There is no median for empty data.')

    # Initially, the window onto each array extends across the array. We need
    # to shrink each window so that this many values are excluded on either
    # side of the windows.
    target = (len(l) + len(r) - 1) // 2
    odd_median = (len(l) + len(r)) % 2 == 1

    left = 0

    while left < target:
        left_midpoint = min(target - left, len(l)) // 2
        right_midpoint = min(target - left, len(r)) // 2
        if len(r) == 0 or l[left_midpoint] <= r[right_midpoint]:
            left += left_midpoint + 1
            l = l[left_midpoint + 1:]
        else:
            left += right_midpoint + 1
            r = r[right_midpoint + 1:]

    if odd_median:
        return min(l[:1] + r[:1])
    smallest_values = l[:2] + r[:2]
    smallest_values.sort()
    return sum(smallest_values[:2]) / 2.0


# pylint: disable=C0301
@hypothesis.strategies.composite
def sorted_arrays(draw):
    '''
    The implementation should work for any two sorted arrays of integers.
    '''
    l = draw(hypothesis.strategies.lists(hypothesis.strategies.integers(min_value=-1000000, max_value=1000000), min_size=0, max_size=1000))
    r = draw(hypothesis.strategies.lists(hypothesis.strategies.integers(min_value=-1000000, max_value=1000000), min_size=0, max_size=1000))
    hypothesis.assume(l or r)
    l.sort()
    r.sort()
    return (l, r)


@hypothesis.given(sorted_arrays())
def test_any_array(lr):
    '''
    Hypothesis will begin with [0], which is exactly the edge case we want.
    '''
    l, r = lr
    expected = statistics.median(itertools.chain(l, r))
    actual = median_of_two_sorted_arrays(l, r)
    assert actual == expected

samples = [
    ([1, 3], [2], 2),
    ([0, 1], [0], 0),
    ([0, 1], [1], 1),
    ([1, 1], [0], 1)
]

@pytest.mark.parametrize("l, r, expected", samples)
def test_samples(l, r, expected):
    '''
    Sample and further test cases from Leetcode.
    '''
    actual = median_of_two_sorted_arrays(l, r)
    assert actual == expected

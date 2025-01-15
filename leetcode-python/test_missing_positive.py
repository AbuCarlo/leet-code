'''
https://leetcode.com/problems/first-missing-positive/

1 <= nums.length <= 10^5
'''

from typing import List

from hypothesis import given, settings, strategies, Verbosity
import pytest


# pylint: disable=C0103
def firstMissingPositive(a: List[int])->int:
    '''
    We use the partioning algorithm from Quicksort in order
    to find a subarray between two values that's too short.
    We continue partioning, not sorting, to home in on this
    value.
    '''
    i = 0
    swaps = 0
    while i < len(a) and swaps < len(a):
        while True:
            n = a[i]
            if n < 1 or n > len(a):
                break
            if n == i + 1:
                break
            if a[n - 1] == n:
                break
            a[i], a[n - 1] = a[n -1], n
            swaps += 1
            if a[i] == i + 1:
                swaps += 1
        i += 1

    for i, n in enumerate(a):
        if n != i + 1:
            return i + 1
    return len(a) + 1


_TEST_CASES = [
    # my own test cases, to observe behavior of partitioning algorithm
    ([1], 2),
    ([1, 2], 3),
    (list(range(2, 5)), 1),
    (list(range(9)), 9),
    (list(range(1, 9)), 9),
    ([1, 3, 3, 4, 6, 6], 2),
    # test cases from description
    ([1,2,0], 3),
    ([3,4,-1,1], 2),
    ([7,8,9,11,12], 1),
    # test case #118: yes, duplicates may appear in the array!
    ([1, 3, 3], 2)
]


@pytest.mark.parametrize("a, expected", _TEST_CASES)
def test_samples(a: List[int], expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    actual = firstMissingPositive(a)
    assert actual == expected

# pylint: disable=C0301
@given(strategies.lists(strategies.integers(min_value=-5, max_value=50), min_size=1, max_size=10000))
@settings(verbosity=Verbosity.verbose)
def test_any_array(a: List[int]):
    '''
    Test for any array of integers. We constrain the range of integers so that the arrays
    are more likely to contain a 1, and thus circumvent the implementation.
    '''
    actual = firstMissingPositive(a)
    positives = set(n for n in a if n > 0)
    expected = 1
    while True:
        if expected not in positives:
            break
        expected += 1

    assert actual == expected

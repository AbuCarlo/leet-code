'''
https://leetcode.com/problems/first-missing-positive/

1 <= nums.length <= 10^5
'''

from typing import List

import pytest

def _partition(a: List[int], low: int, high: int, pivot_index: int) -> int:
    # See https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme.
    # I modified the partitioning to be able to return the known
    # location of the pivot value, based on
    # https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/Quicksort.html

    pivot = a[pivot_index]
    a[high], a[pivot_index] = a[pivot_index], a[high]

    i = low - 1
    # Leave the pivot value alone.
    j = high

    while True:

        i += 1
        while a[i] < pivot:
            i += 1

        j -= 1
        while a[j] > pivot:
            j -= 1

        if i >= j:
            # Swap the pivot value into its final location.
            a[i], a[high] = a[high], a[i]
            # Return the location of the pivot value,
            # unlike Hoare.
            return i

        # Swap values across the partition.
        a[i], a[j] = a[j], a[i]

# pylint: disable=C0103
def firstMissingPositive(a: List[int])->int:
    '''
    We use the partioning algorithm from Quicksort in order
    to find a subarray between two values that's too short.
    We continue partioning, not sorting, to home in on this
    value.
    '''
    try:
        midpoint = a.index(1)
    except ValueError:
        return 1

    # Start with positive integers.
    start = _partition(a, 0, len(a) -1, midpoint)
    end = len(a) - 1

    while True:
        # Keep selecting pivots. If a partition is the right size,
        # based on the pivot value, it's not missing anything.
        # Try the other one.
        if a[midpoint] - a[start] > midpoint - start:
            print(f'Missing value between a[{start}] = {a[start]} and a[{midpoint}] = {a[midpoint]}')
            end = midpoint - 1
        elif a[end] - a[midpoint] > end - midpoint:
            print(f'Missing value between a[{midpoint}] = {a[midpoint]} and a[{end}] = {a[end]}')
            start = midpoint + 1
        else:
            # Both partitions are the right size: no value is missing.
            return max(a) + 1
        if end - start == 1:
            return a[start] + 1
        midpoint = _partition(a, start, end, (start + end) // 2)


_TEST_CASES = [
    # my own test cases, to observe behavior of partitioning algorithm
    # TODO Shuffle these.
    ([1], 2),
    ([1, 2], 3),
    (list(range(2, 5)), 1),
    (list(range(9)), 9),
    (list(range(1, 9)), 9),
    # test cases from description
    ([1,2,0], 3),
    ([3,4,-1,1], 2),
    ([7,8,9,11,12], 1)
]


@pytest.mark.parametrize("a, expected", _TEST_CASES)
def test_samples(a: List[int], expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    actual = firstMissingPositive(a)
    assert actual == expected

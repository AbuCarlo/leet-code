'''
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description

"Given an integer array arr, remove a subarray (can be empty) from arr
such that the remaining elements in arr are non-decreasing."

'''

import sys
from typing import List, Tuple

import pytest

def find_shifted(arr: List[int]) -> Tuple[int, int]:
    '''
    Find the indices of elements that would have to be
    moved as part of a non-destructive sort.
    '''
    annotated = [(n, i) for i, n in enumerate(arr)]
    indices = [t[1] for t in sorted(annotated)]
    shifted = [ix for i, ix in enumerate(indices[:-1]) if ix > indices[i + 1]]
    return shifted


# pylint: disable=C0103
def findLengthOfShortestSubarray(arr: List[int]) -> int:
    '''
    Find the indices of elements that would have to be moved as 
    part of a sort. The minimum and maximum such indices 
    are the first and last indices of the subarray to be removed.
    '''
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    if arr[0] > arr[-1]:
        # The subarray to be deleted must start at 0, or end at -1.
        max_left = 1
        for n in arr[1:]:
            if n < arr[0]:
                break
            max_left += 1
        max_right = 1
        for n in reversed(arr[:-1]):
            if n > arr[-1]:
                break
            max_right += 1
        return min(len(arr) - max_left, len(arr) - max_right)
    shifted = find_shifted([-sys.maxsize] + arr + [sys.maxsize])
    if not shifted:
        return 0
    return max(shifted) - min(shifted) + 1


_SAMPLES =[
    # sample test cases
    ([1,2,3,10,4,2,3,5], 3),
    ([5,4,3,2,1], 4),
    ([1, 2, 3], 0),
    # special cases
    ([7, 8, 9, 4, 5, 6, 0, 1, 2, 3], 6),
    ([5, 1, 2, 3, 4, 5], 1),
    ([0, 1, 2, 3, 4, 0], 1),
    # test case #20
    ([2,2,2,1,1,1], 3),
    # variations of test case #20
    ([2,2,1,1,1], 2),
    ([2,2,2,1,1], 2),
    # test case #58
    ([1,2,3,10,0,7,8,9], 2),
]
 
# pylint: disable=C0116
@pytest.mark.parametrize("a, expected", _SAMPLES)
def test_samples(a, expected):
    actual = findLengthOfShortestSubarray(a)
    assert actual == expected

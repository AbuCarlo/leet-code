'''
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description

"Given an integer array arr, remove a subarray (can be empty) from arr
such that the remaining elements in arr are non-decreasing."

'''

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
    shifted = find_shifted(arr)
    if not shifted:
        return 0
    return max(shifted) - min(shifted) + 1


_SAMPLES =[
    # sample test cases
    ([1,2,3,10,4,2,3,5], 3),
    ([5,4,3,2,1], 4),
    ([1, 2, 3], 0),
    # test case 20
    ([2,2,2,1,1,1], 3)
]

# pylint: disable=C0116
@pytest.mark.parametrize("a, expected", _SAMPLES)
def test_samples(a, expected):
    actual = findLengthOfShortestSubarray(a)
    assert actual == expected

'''
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description

"Given an integer array arr, remove a subarray (can be empty) from arr
such that the remaining elements in arr are non-decreasing."

'''

from typing import List

import pytest

# pylint: disable=C0103
def findLengthOfShortestSubarray(arr: List[int]) -> int:
    '''
    Find the indices of elements that would have to be moved as 
    part of a sort. The minimum and maximum such indices 
    are the first and last indices of the subarray to be removed.
    '''
    if not arr:
        return 0
    # If the first element is > than the last,
    # one of these elements must be removed to
    # achieve a sorted array. The subarray to
    # removed must therefore be either the prefix
    # or the suffix of the array.
    max_left = len(arr) - 1
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            max_left = i
            break
    # Is the array already sorted? The edge cases
    # of a 0- or 1-length array are taken care of here.
    if max_left == len(arr) - 1:
        return 0

    max_right = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < arr[i - 1]:
            max_right = i
            break
    if max_right == 0:
        return len(arr) - 1
    
    memos = {}

    def trim_internal(l: int, r: int) -> int:
        key = (l, r)
        if key in memos:
            return memos[key]
        if l < 0:
            # Discard the prefix.
            return r
        if r == len(arr):
            # Discard the entire suffix.
            return len(arr) - l - 1
        if arr[l] <= arr[r]:
            # How many elements between these two?
            return r - l - 1
        leftward = trim_internal(l - 1, r)
        rightward = trim_internal(l, r + 1)
        result = min(leftward, rightward)
        memos[key] = result
        return result

    return trim_internal(max_left, max_right)


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

'''
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description
'''

from typing import List

import pytest

# pylint: disable=C0103
def findLengthOfShortestSubarray(arr: List[int]) -> int:
    if len(arr) < 2:
        return 0
    start = None
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            start = i
            break
    i = start - 1
    j = start + 1
    # while arr[i] > 
        


_SAMPLES =[
    ([1,2,3,10,4,2,3,5], 3)
]

# pylint: disable=C0116
@pytest.mark.parametrize("a, expected", _SAMPLES)
def test_samples(a, expected):
    actual = findLengthOfShortestSubarray(a)
    assert actual == expected

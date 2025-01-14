'''
https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

'''

from typing import List

import pytest


def find_score(nums: List[int]) -> int:
    '''
    See above. |nums| <= 10^5, nums[i] < 10^6. 
    Time: O(n log n) to sort the values. A heap
    would have been appropriate.
    '''
    marked_locations = set()
    values_with_locations = [(v, l) for l, v in enumerate(nums)]
    values_with_locations.sort()
    score = 0
    for v, l in values_with_locations:
        if l in marked_locations:
            continue
        score += v
        marked_locations.add(l)
        marked_locations.add(l - 1)
        marked_locations.add(l + 1)
    return score


_TEST_CASES = [
    ([2,1,3,4,5,2], 7)
]

# pylint: disable=C0116
@pytest.mark.parametrize("nums, expected", _TEST_CASES)
def test_find_score(nums, expected):
    actual = find_score(nums)
    assert actual == expected

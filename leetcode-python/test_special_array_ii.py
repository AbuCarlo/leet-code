'''
https://leetcode.com/problems/special-array-ii
'''

import bisect
from typing import List

import pytest

def is_array_special(nums: List[int], queries: List[List[int]]) -> List[bool]:
    '''
    Find adjacent pairs with the same parity. Then use binary search
    to determine if such a pair is within a "query."
    '''
    same_parity = []
    for i in range(1, len(nums)):
        if nums[i - 1] & 0x1 == nums[i] & 0x1:
            same_parity.append(i - 1)

    def is_subarray_special(l, r) -> bool:
        if l == r:
            return True
        if not same_parity:
            return True
        insertion = bisect.bisect_right(same_parity, l)
        # bisect_right() tells us where the last instance
        # of l should be inserted. If l is present in the
        # array, we have an edge case.
        if insertion > 0 and same_parity[insertion - 1] == l:
            return False
        if insertion == len(same_parity):
            # Apparent nums[l:] is completely special.
            return True
        return not(same_parity[insertion] >= l and same_parity[insertion] < r)

    return [is_subarray_special(l, r) for l, r in queries]

_TEST_CASES = [
    ([3,4,1,2,6],[[0,4]], [False]),
    ([4,3,1,6], [[0,2],[2,3]], [False, True]),
    # test case # 427
    ([1,1], [[0,1]], [False]),
    # test case # 496
    ([2,2], [[0,0]], [True])
]

@pytest.mark.parametrize("nums,queries,expected", _TEST_CASES)
def test_shortest_distance(nums, queries, expected):
    '''
    Apply samples from LeetCode
    '''
    actual = is_array_special(nums, queries)
    assert actual == expected

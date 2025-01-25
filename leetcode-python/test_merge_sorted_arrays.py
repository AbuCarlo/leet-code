'''
https://leetcode.com/problems/merge-sorted-array/
'''

from typing import List

import pytest


class Solution:
    '''
    LeetCode's usual framework.
    '''
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify a in-place instead.
        """
        i = m - 1
        j = n - 1
        for k in range(m + n - 1, -1, -1):
            if j < 0 or i >= 0 and a[i] > b[j]:
                a[k] = a[i]
                i -= 1
            else:
                a[k] = b[j]
                j -= 1

_SAMPLES = [
    ([1,2,3,0,0,0], [2, 5, 6]),
    ([], []),
    ([1], []),
    ([2, 0], [1]),
    ([1,2,4,5,6,0], [3]),
    ([4,5,6,0,0,0], [1, 2, 3]),
    ([0,0,3,0,0,0,0,0,0], [-1,1,1,1,2,3]),
    ([-1,0,0,0,3,0,0,0,0,0,0], [-1,-1,0,0,1,2])
]

@pytest.mark.parametrize("l, r", _SAMPLES)
def test_test_cases(l, r):
    '''
    Stress tests from LeetCode
    '''
    n = len(r)
    m = len(l) - n

    expected = list(sorted(l[:m] + r))

    solution = Solution()
    solution.merge(l, m, r, n)
    assert l == expected

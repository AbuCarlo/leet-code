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
        # Store excess values from the first array in the second. We'll have to
        # do this at most n times, because there can only be n values too large
        # to insert before b[0]
        i = 0
        j = 0
        retrieve_at = 0
        store_at = 0
        for i in range(m):
            if j < n and a[i] <= b[j]:
                continue
            if j == n:
                break
            t = b[j]
            j += 1
            b[store_at] = a[i]
            store_at += 1
            a[i] = t
        i = m
        while i < m + n:
            if j == n:
                a[i] = b[retrieve_at]
                retrieve_at += 1
                if retrieve_at == store_at:
                    retrieve_at = store_at = 0
            elif retrieve_at == store_at or b[j] < b[retrieve_at]:
                a[i] = b[j]
                j += 1
            else:
                a[i] = b[retrieve_at]
                retrieve_at += 1
                if retrieve_at == store_at:
                    retrieve_at = store_at = 0
            i += 1
            



_SAMPLES = [
    ([1,2,3,0,0,0], [2, 5, 6]),
    ([], []),
    ([1], []),
    ([2, 0], [1]),
    ([1,2,4,5,6,0], [3])
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








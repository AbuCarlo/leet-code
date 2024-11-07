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
        if not b:
            return
        j = 0
        retrieve_at = 0
        store_at = 0
        for i in range(m + n):
            # Something's in the buffer.
            if retrieve_at != store_at:
                if j < n:
                    if b[retrieve_at] <= b[j]:
                        if i < m:
                            t = a[i]
                        a[i] = b[retrieve_at]
                        retrieve_at += 1
                        if retrieve_at == store_at:
                            retrieve_at = store_at = 0
                        if i < m:
                            b[store_at] = t
                            store_at += 1
                    elif i < m and a[i] <= b[j]:
                        pass
                    else:
                        if i < m:
                            t = a[i]
                        a[i] = b[j]
                        j += 1
                        if i < m:
                            b[store_at] = t
                            store_at += 1
            else:
                # Values here can be overwritten.
                if i >= m:
                    a[i] = b[j]
                    j += 1
                # The buffer must be empty.
                elif j >= n or a[i] <= b[j]:
                    pass
                else:
                    t = a[i]
                    a[i] = b[j]
                    b[store_at] = t
                    store_at += 1
                    
                



_SAMPLES = [
    ([1,2,3,0,0,0], [2, 5, 6]),
    ([], []),
    ([1], []),
    ([2, 0], [1]),
    ([1,2,4,5,6,0], [3]),
    ([4,5,6,0,0,0], [1, 2, 3]),
    ([0,0,3,0,0,0,0,0,0], [-1,1,1,1,2,3])
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








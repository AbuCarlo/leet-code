'''
https://leetcode.com/problems/merge-sorted-array/
'''

from typing import List

import pytest


class Solution:
    '''
    LeetCode's usual framework.
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        # Store excess values from the first array in the second. We'll have to 
        # do this at most n times, because there can only be n values too large
        # to insert before nums1[0]
        retrieve_at = 0
        store_at = 0
        # Store excess values in the *second* array.
        while i < m + n:
            # If we've stored a smaller value, fetch it. If we've used up
            # the second array, prioritize the cache.
            if retrieve_at < store_at and (j == n or nums2[retrieve_at] < nums2[j]):
                if j == n:
                    t = nums2[retrieve_at]
                    nums2[retrieve_at] = nums1[i]
                    nums1[i] = t
                elif i < m:
                    nums2[store_at] = nums1[i]
                    store_at += 1
                    nums1[i] = nums2[retrieve_at]
                    retrieve_at += 1
            elif i >= m:
                nums1[i] = nums2[j]
                j += 1
            elif j == n or nums1[i] <= nums2[j]:
                pass
            else:
                t = nums1[i]
                nums1[i] = nums2[j]
                j += 1
                nums2[store_at] = t
                store_at += 1
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








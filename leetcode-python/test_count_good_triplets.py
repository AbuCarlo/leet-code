'''
https://leetcode.com/problems/count-good-triplets-in-an-array
'''

from typing import List

def good_triplets(l: List[int], r: List[int]) -> int:
    '''
    A "good" triplet is a triplet (a[i], a[j], a[k])
    such that a[i] < a[j] < a[k] and i < j < k. 
    For a sorted array of length n, the number of such 
    triplets is (n - 2) * (n - 1) * (n - 2). We can 
    count by iterating over the array, and adding each
    value to a min-heap. Whenever a new value a[i] becomes
    the new min (i.e. there are no preceding smaller values),
    a[i] can only be the first value of a good triplet.
    a[1] is an edge case: it clearly cannot be the last
    value in a good triplet. By similar reasoning, whenever
    a value a[i] becomes the new maximum in a max-heap,
    it can be only the last value in a good triplet.
    '''
    assert len(l) == len(r)
    if len(l) < 3:
        return 0
    
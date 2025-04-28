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
    a[i] can only be the _first_ value of a good triplet.

    '''
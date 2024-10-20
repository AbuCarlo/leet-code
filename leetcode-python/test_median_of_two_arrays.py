'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

import hypothesis

@hypothesis.strategies.composite
def sorted_arrays(draw):
    '''
    The implementation should work for any two sorted arrays of integers.
    '''
    a = draw(hypothesis.strategies.lists(hypothesis.strategies.integers(), min_size=1))
    split_at = draw(hypothesis.strategies.integers(min_value=1, max_value=len(a)))
    l = a[:split_at]
    r = a[split_at:]
    l.sort()
    r.sort()
    return (l, r)
 

@hypothesis.given(sorted_arrays())
def test_any_array(lr):
    l, r = lr
    print(l, r)
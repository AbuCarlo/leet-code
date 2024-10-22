'''
https://leetcode.com/problems/median-of-two-sorted-arrays/

"The overall run time complexity should be O(log (m+n))."
'''

import itertools
import statistics

import hypothesis
import hypothesis.strategies

def median_of_two_sorted_arrays(l: list[int], r: list[int]) -> float:
    '''
    The assignment pretty clearly implies something like binary search.
    '''
    odd_median = (len(l) + len(r)) % 2 == 1
    # There *is* a median if 1 list is empty.
    if not l:
        if not r:
            # Python's statistics.median() raises a similar error.
            raise ValueError('There is no median for empty data.')
        return r[len(r) // 2] if odd_median else sum(r[len(r) // 2:][:2]) / 2.0
    if not r:
        return [len(l) // 2] if odd_median else sum(l[len(l) // 2:][:2]) / 2.0

    # This many value need to be on either side of the median.
    target = (len(l) + len(r) - 1) // 2

    l_left_limit = 0
    r_left_limit = 0

    l_index = len(l) // 2
    r_index = len(r) // 2

    while l_index + r_index < target:
        if l[l_index] < r[r_index]:
            l_left_limit, l_index = l_index, (l_index + l_left_limit) // 2
            assert l_index >= l_left_limit
        else:
            r_left_limit, r_index = r_index, (r_index + r_left_limit) // 2
            assert r_index >= r_left_limit
    # All the value to the left of the indices would be in the first half
    # of the merged array. If the total length is odd, the median has to
    # be the lower value at the two indices. If even, the median is the
    # average of the two lowest values still available.
    print(f'l = {l}: {l_index}; r = {r}: {r_index}')
    if (len(l) + len(r)) % 2 == 1:
        # *All* values in l were eliminated.
        if l_index == 0:
            return r[r_index]
        if r_index == 0:
            return l[l_index]
        # Those were the edge cases.
        return min(l[l_index], r[r_index])
    # Let's say that l[l_index] < r[r_index]. Then l[l_index] is 
    # one value that's averaged into the median, and the other is
    # either r[r_index] or, if lower, l[l_index + 1]. And so on.
    # Let's just take advantage of the fact that Python will *not*
    # give us an IndexError if we use the range accessors.
    values_for_median = l[l_index:l_index + 2] + r[r_index:r_index + 2]
    values_for_median.sort()
    return sum(values_for_median[0:2]) / 2

# pylint: disable=C0301
@hypothesis.strategies.composite
def sorted_arrays(draw):
    '''
    The implementation should work for any two sorted arrays of integers.
    '''
    l = draw(hypothesis.strategies.lists(hypothesis.strategies.integers(min_value=-1000000, max_value=1000000), min_size=0, max_size=1000))
    r = draw(hypothesis.strategies.lists(hypothesis.strategies.integers(min_value=-1000000, max_value=1000000), min_size=0, max_size=1000))
    hypothesis.assume(l or r)
    l.sort()
    r.sort()
    return (l, r)


@hypothesis.given(sorted_arrays())
def test_any_array(lr):
    '''
    Hypothesis will begin with [0], which is exactly the edge case we want.
    '''
    l, r = lr
    expected = statistics.median(itertools.chain(l, r))
    actual = median_of_two_sorted_arrays(l, r)
    assert actual == expected

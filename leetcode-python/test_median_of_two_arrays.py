'''
https://leetcode.com/problems/median-of-two-sorted-arrays/

"The overall run time complexity should be O(log (m+n))."
'''

import itertools
import statistics

import hypothesis
import hypothesis.strategies
import pytest

def median_of_two_sorted_arrays(l: list[int], r: list[int]) -> float:
    '''
    The assignment pretty clearly implies something like binary search.
    '''
    if not l and not r:
        raise ValueError('There is no median for empty data.')

    # Once we've eliminated this many elements, the values
    # for the median will be in the prefix of either or
    # both array.
    target = (len(l) + len(r) - 1) // 2
    is_median_odd = (len(l) + len(r)) % 2 == 1

    eliminated = 0

    while eliminated < target:
        if len(l) == 0:
            r = r[target - eliminated:]
            break
        if len(r) == 0:
            l = l[target - eliminated:]
            break

        # This the edge case: we can only consider the first elements
        # of the two arrays.
        if target - eliminated == 1:
            if l[0] <= r[0]:
                l = l[1:]
            else:
                r = r[1:]
            break

        left_selection = min((target - eliminated) // 2 - 1, len(l) - 1)
        right_selection = min((target - eliminated) // 2 - 1, len(r) - 1)

        assert left_selection + 1 + right_selection + 1 <= target - eliminated

        if l[left_selection] <= r[right_selection]:
            # 0-based Python indexing
            eliminated += left_selection + 1
            # The assertion above ensures that we can do this:
            # we can eliminate both prefixes here.
            if l[left_selection] == r[right_selection]:
                eliminated += right_selection + 1
                r = r[right_selection + 1:]
            l = l[left_selection + 1:]
        elif l[left_selection] > r[right_selection]:
            eliminated += right_selection + 1
            r = r[right_selection + 1:]

    if is_median_odd:
        return min(l[:1] + r[:1])
    smallest_values = l[:2] + r[:2]
    smallest_values.sort()
    return sum(smallest_values[:2]) / 2.0


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

samples = [
    ([1, 3], [2], 2),
    ([0, 1], [0], 0),
    ([0, 1], [1], 1),
    ([1, 1], [0], 1),
    # edge cases I've found
    ([1, 2, 3], [1, 2, 3, 4], 2),
    ([1, 2, 3], [1, 2, 3], 2)
]

@pytest.mark.parametrize("l, r, expected", samples)
def test_samples(l, r, expected):
    '''
    Sample and further test cases from Leetcode.
    '''
    actual = median_of_two_sorted_arrays(l, r)
    assert actual == expected

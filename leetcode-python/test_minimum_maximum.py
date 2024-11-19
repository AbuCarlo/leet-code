'''
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
'''

import math
from typing import List

import pytest

def minimized_maximum(n: int, quantities: List[int]) -> int:
    '''
    Use binary search to find the optimal result, i.e.,
    Where q = |quantities|, O(q * log q) implementation.

    :param n: number of buckets to put goods in
    :param quantities: quantity of each item, which can't be mixed
    '''
    if len(quantities) > n:
        raise ValueError('There are more quantities than buckets to put them in.')
    # "upper" is the upper bound on a solution. In the worst case, we just
    # keep all the quantities together, and leave some buckets empty.
    # "lower" is the total of quantities, distributed evenly to the buckets.
    # This solution isn't possible, since we can't mix products.
    upper = max(quantities)
    lower = math.ceil(sum(quantities) / n)
    while upper - lower > 1:
        mid = (upper + lower) // 2
        if sum(math.ceil(q / mid) for q in quantities) > n:
            lower = mid
        else:
            upper = mid

    if sum(math.ceil(q / lower) for q in quantities) <= n:
        return lower
    return upper


_SAMPLES = [
    # edge cases
    (3, [1, 100], 50),
    (4, [2, 4], 2),
    (3, [11, 17], 11),
    (3, [2, 10], 5),
    # samples
    (6, [11,6], 3),
    (7, [15,10,10], 5),
    (1, [10000], 10000),
    # test cases
    (22, [25,11,29,6,24,4,29,18,6,13,25,30], 13)
]


# pylint: disable=C0116
@pytest.mark.parametrize("n,quantities,expected", _SAMPLES)
def test_known_solutions(n: int, quantities: List[int], expected: int):
    actual = minimized_maximum(n, quantities)
    assert actual == expected

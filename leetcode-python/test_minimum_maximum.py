'''
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
'''

import math
from typing import List

import pytest

_SAMPLES = [
    # samples
    (6, [11,6], 3),
    (7, [15,10,10], 5),
    (1, [10000], 10000),
    # test cases
    (22, [25,11,29,6,24,4,29,18,6,13,25,30], 13)
]

def minimized_maximum(n: int, quantities: List[int]) -> int:
    '''
    O(|quantities|) implementation.
    '''
    quantity_ix = 0
    bucket_index = 0
    result = 0
    quantities.sort()
    current_sum = sum(quantities)
    while bucket_index < n:
        current_avg = math.ceil(current_sum / (n - bucket_index))
        while quantities[quantity_ix] < current_avg:
            result = max(result, quantities[quantity_ix])
            current_sum -= quantities[quantity_ix]
            bucket_index += 1
            quantity_ix += 1
        current_avg = math.ceil(current_sum / (n - bucket_index))
        # Split up the next quantity.
        buckets = math.ceil(quantities[quantity_ix] / (current_avg))
        sizes = math.ceil(quantities[quantity_ix] / buckets)
        result = max(result, sizes)

        current_sum -= quantities[quantity_ix]
        bucket_index += buckets
        quantity_ix += 1

    assert quantity_ix == len(quantities)
    return result


# pylint: disable=C0116
@pytest.mark.parametrize("n,quantities,expected", _SAMPLES)
def test_known_solutions(n: int, quantities: List[int], expected: int):
    actual = minimized_maximum(n, quantities)
    assert actual == expected

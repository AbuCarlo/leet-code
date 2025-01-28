'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
'''

import itertools
import operator

import pytest

VOWELS = set('aeiou')

def max_vowels(s: str, k: int) -> int:
    '''
    O(n) solution using partial sums.
    '''
    singles = (e in VOWELS for e in s)
    # "If an initial value is provided, the accumulation will start
    # with that value and the output will have one more element than the input iterable."
    # The value of "initial" will be prepended to the result.
    accumulation = list(itertools.accumulate(singles, func=operator.add, initial=0))
    k_sums = [accumulation[i] - accumulation[i - k] for i in range(k - 1, len(accumulation))]
    return max(k_sums)


_TEST_CASES = [
    ("abciiidef", 3, 3),
    ("aeiou", 2, 2),
    ('weallloveyou', 7, 4)
]


@pytest.mark.parametrize("s,k,expected", _TEST_CASES)
def test_samples(s: str, k: int, expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    actual = max_vowels(s, k)
    assert actual == expected

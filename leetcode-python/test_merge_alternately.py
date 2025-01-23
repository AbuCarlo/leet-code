'''
https://leetcode.com/problems/merge-strings-alternately
'''

import pytest


def merge_alternately(word1: str, word2: str) -> str:
    '''
    Just use Python's zip(), then append the leftover
    from the longer string.
    '''
    z = zip(list(word1), list(word2))
    if len(word1) > len(word2):
        tail = word1[len(word2):]
    else:
        # Possibly a 0-length string.
        tail = word2[len(word1):]
    return ''.join(t[0] + t[1] for t in z) + tail

_SAMPLES = [
    ("ab", "pqrs", "apbqrs")
]

@pytest.mark.parametrize("l,r,expected", _SAMPLES)
def test_known_solutions(l: str, r: str, expected: str):
    actual = merge_alternately(l, r)
    assert actual == expected
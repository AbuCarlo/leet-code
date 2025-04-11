'''
https://leetcode.com/problems/minimum-window-substring/

"Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string.

'''

import collections

import pytest

# pylint: disable=W0223
class ZeroingCounter(collections.Counter):
    '''
    This class encapsulates the logic of a sliding count. If any count
    becomes 0, the key is deleted.
    '''

    # We don't need to override the constructor since the initial
    # values will not include 0s. update() should be overriden, but
    # we never invoke it.

    def __setitem__(self, key, value):
        if value == 0:
            self.pop(key)
        else:
            super().__setitem__(key, value)


def minimum_window_substring(s: str, t: str) -> str:
    '''
    Put something here.
    '''
    allowable = set(t)
    counts = ZeroingCounter(t)
    overflow = ZeroingCounter()
    results = []
    l = 0
    for r, c in enumerate(s):
        if c not in allowable:
            continue
        if c in counts:
            counts[c] -= 1
        else:
            overflow[c] += 1
        while s[l] in overflow or s[l] not in allowable:
            overflow[s[l]] -= 1
            l += 1
        if len(counts) == 0:
            results.append((l, r + 1))
            counts[s[l]] += 1
            l += 1

    if not results:
        return ''
    ll, rr = min(results, key=lambda t: t[1] - t[0])
    return s[ll:rr]

_SAMPLES = [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", "")
]

@pytest.mark.parametrize("s,t,expected", _SAMPLES)
def test_samples(s: str, t: list[str], expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    actual = minimum_window_substring(s, t)
    assert actual == expected
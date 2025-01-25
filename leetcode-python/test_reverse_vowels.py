'''
https://leetcode.com/problems/reverse-vowels-of-a-string
'''

import pytest


class Solution:
    '''
    LeetCode's boilerplate, which lets us initialize the set of vowels.
    '''

    def __init__(self):
        vowels = 'aeiou'
        self._vowels = set(vowels + vowels.upper())

    # pylint: disable=C0103,C0116
    def reverseVowels(self, s: str) -> str:
        vowel_indices = [i for i, c in enumerate(s) if c in self._vowels]
        a = list(s)
        for i, ix in enumerate(vowel_indices[:len(vowel_indices) // 2]):
            jx = vowel_indices[len(vowel_indices) - i - 1]
            a[ix], a[jx] = a[jx], a[ix]
        return ''.join(a)


_SAMPLES = [
    ("leetcode", "leotcede")
]


@pytest.mark.parametrize("s,expected", _SAMPLES)
def test_reverse_vowels(s: str, expected: str):
    '''
    Apply samples from LeetCode
    '''
    solution = Solution()
    actual = solution.reverseVowels(s)
    assert actual == expected
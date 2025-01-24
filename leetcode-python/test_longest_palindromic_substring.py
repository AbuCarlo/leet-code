'''
https://leetcode.com/problems/longest-palindromic-substring/
'''

import collections
import pytest


def longest_palindrome(s: str) -> str:
    index = collections.defaultdict(list)
    for i, c in enumerate(s):
        index[c].append(i)
    palindromes = []
    longest = 1
    for i, c in enumerate(s):
        for j in [j for j in reversed(index[c]) if j > i]:

            if j - i + 1 < longest:
                continue
            # If i and j are the endpoints of a palindrome,
            # let's check the center:
            # if (j - i) // 2 in palindromes:
            #     continue
            k = i + 1
            l = j - 1
            
            middle = 1 if (j - i) % 2 == 0 else 0
            
            while l > k + middle and s[k] == s[l]:
                k += 1
                l -= 1
            # The indices have crossed, i.e. we've found a palindrome.
            if l <= k:
                length = j - i + 1
                print(f'Found palindrome from {i} to {j} inclusive: {s[i:j + 1]}')
                longest = max(longest, length)
                # palindromes[k] = length
                palindromes.append((i, j))

    if longest == 1:
        assert not palindromes
        return s[:1]
    for key, value in palindromes:
        if value - key + 1 == longest:
            return s[key:value + 1]
        # if value == longest:
        #     l, r = key - longest // 2, key + longest // 2 + (longest % 2)
        #     return s[l:r]

_SAMPLES = [
    ("babad", "bab"),
    ("cbbd", "bb"),
    # test case # 77
    ("aacabdkacaa", "aca")
]

@pytest.mark.parametrize("s, expected", _SAMPLES)
def test_samples(s, expected):
    '''
    Sample and further test cases from Leetcode.
    '''
    actual = longest_palindrome(s)
    assert actual == expected
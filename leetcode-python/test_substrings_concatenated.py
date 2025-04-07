'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words
'''

import collections
import itertools
import random
import typing

import pytest
import hypothesis
from hypothesis import strategies

class ZeroingCounter(collections.Counter):
    '''
    This class encapsulates the logic of a sliding count. If any count
    becomes 0, the key is deleted. We initialize the counter from a list 
    of search tokens. If all values (counts) become 0, the current window
    contains a permutation of the input tokens (i.e.). A negative value
    means that the current keyb (token) appears too many times in the 
    current window.
    '''

    # We don't need to override the constructor since the initial
    # values will not include 0s. update() should be overriden, but
    # we never invoke it.

    def __setitem__(self, key, value):
        if value == 0:
            self.pop(key)
        else:
            super().__setitem__(key, value)


def find_concatenations(s: str, tokens: list[str]) -> int:
    '''
    :param s: a string to search
    :param tokens: tokens, not necessarily unique
    :returns: the starting indices of every substring that is the
    concatenation of all the tokens
    '''

    def find_all_overlapping(token: str) -> typing.Iterator[int]:
        '''
        Find all over instances of a token in the input string,
        possibly overlapping.
        '''
        start = 0
        while True:
            start = s.find(token, start)
            if start == -1:
                break
            yield start
            start += 1

    token_set = set(tokens)
    # Several test cases time out when there's only 1 token value, 
    # esp. a very short one.
    if len(token_set) == 1:
        token = tokens[0] * len(tokens)
        return list(find_all_overlapping(token))

    # All the tokens are the same length.
    token_length = len(tokens[0])
    # We may be given only two tokens, and they might be equal.
    # So there's not much point in looking for the best token.
    anchor = random.choice(tokens)
    anchor_positions = list(find_all_overlapping(anchor))

    all_results = []

    # Matches may start at any index. A match at i will be a concatenation
    # tokens, all the same length.  
    for remainder in set(p % token_length for p in anchor_positions):

        results = []
        # Slicing up the input is easier than lots of finicky substring matching, and in 
        # any case, we have to create substrings as keys, so let's just slice up the input.
        sliced = [s[i:i + token_length] for i in range(remainder, len(s), token_length)]

        # the index of the slice representing the (possible) rightmost slice of a match
        r = 0

        counts = ZeroingCounter(tokens)
        # the left of a potential match, and the current token
        for l, sl in enumerate(sliced):
            if sl not in token_set:
                # Advance the right index past the current token.
                r = l + 1
                # Reset the counts.
                counts = ZeroingCounter(tokens)
                continue
            # Check off this token.
            counts[sl] -= 1
            # Discard the rightmost token if we have too many.
            if l - r == len(tokens):
                counts[sliced[r]] += 1
                r += 1
            if not counts:
                results.append(r)

        # Translate these again.
        all_results += [remainder + r * token_length for r in results]

    all_results.sort()
    return all_results


_SAMPLES = [
    ('barfoothefoobarman', ["foo", "bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ['bar', 'foo', 'the'], [6, 9, 12]),
    # test case #168
    ('a', ["a","a"], []),
    # test case #170
    ("aaaaaaaaaaaaaa", ["aa","aa"], list(range(11))),
    # test case #177
    ("abbaccaaabcabbbccbabbccabbacabcacbbaabbbbbaaabaccaacbccabcbababbbabccabacbbcabbaacaccccbaabcabaabaaaabcaabcacabaa", ["cac","aaa","aba","aab","abc"]
, [97]),
    # test case #179
    ("bcabbcaabbccacacbabccacaababcbb", ["c","b","a","c","a","a","a","b","c"], [6,16,17,18,19,20]),
    # test case #181
    ("acccaccaa", ["aa","cc","ca"], [3])
]


@pytest.mark.parametrize("s,tokens,expected", _SAMPLES)
def test_samples(s: str, tokens: list[str], expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    actual = find_concatenations(s, tokens)
    assert actual == expected

@strategies.composite
def permute_tokens(draw):
    '''
    A match should be able to begin anywhere in the input string.
    '''
    _, tokens, _ = draw(strategies.sampled_from(_SAMPLES))
    permutation = draw(strategies.permutations(tokens))
    return (''.join(permutation), tokens)

@hypothesis.given(permute_tokens())
# pylint: disable=C0116
def test_permuted_tokens(t):
    s, tokens = t
    actual = find_concatenations(s, tokens)
    assert len(actual) == 1

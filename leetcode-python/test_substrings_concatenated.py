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

class ZeroingCount(collections.Counter):
    '''
    This class encapsulates the logic of a sliding count. If any count
    becomes 0, the key is deleted. An empty counter means that the current
    window contains a permutation of the input tokens.
    '''

    # We don't need to override the constructor, since the initial
    # values will not include 0s.

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
        start = 0
        while True:
            start = s.find(token, start)
            if start == -1:
                break
            yield start
            start += 1

    # All the tokens are the same length.
    token_set = set(tokens)
    # Several test cases time out when there's only 1 token value, 
    # esp. a very short one.
    if len(token_set) == 1:
        token = tokens[0] * len(tokens)
        return list(find_all_overlapping(token))
    token_length = len(tokens[0])
    # We may be given only two tokens, and they might be equal.
    # So there's not much point in looking for the best token.
    anchor = random.choice(tokens)
    anchor_positions = list(find_all_overlapping(anchor))

    all_results = []

    for remainder in set(p % token_length for p in anchor_positions):

        results = []
        # Slicing up the input is easier than lots of finicky substring matching. Get rid
        # of terminal tokens that are too short to match anyway.
        sliced = [s[i:i + token_length] for i in range(remainder, len(s), token_length) if len(s) - i >= token_length]

        r = 0

        counts = ZeroingCount(tokens)

        for l, sl in enumerate(sliced):
            if sl not in token_set:
                r = l + 1
                counts = ZeroingCount(tokens)
                continue

            counts[sl] -= 1
            if l - r + 1 == len(tokens):
                counts[sliced[r]] -= 1
            if not counts:
                results.append(r)
            r += 1

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
def add_whitespace(draw):
    '''
    A match should be able to begin anywhere in the input string.
    '''
    s, tokens, expected = draw(strategies.sampled_from(_SAMPLES))
    prefix_length = draw(strategies.integers(min_value=0, max_value=len(tokens[0])))
    suffix_length = draw(strategies.integers(min_value=0, max_value=len(tokens[0])))
    s = (' ' * prefix_length) + s + (' ' * suffix_length)
    return (s, tokens, expected)


@strategies.composite
def permute_tokens(draw):
    '''
    A match should be able to begin anywhere in the input string.
    '''
    _, tokens, _ = draw(strategies.sampled_from(_SAMPLES))
    permutation = draw(strategies.permutations(tokens))
    return (''.join(permutation), tokens)


@hypothesis.given(add_whitespace())
# pylint: disable=C0116
def test_with_whitespace(t):
    s, tokens, expected = t
    actual = find_concatenations(s, tokens)
    assert actual == expected

# TODO: Modify to just take whitespace as argument.

@hypothesis.given(permute_tokens())
# pylint: disable=C0116
def test_permuted_tokens(t):
    s, tokens = t
    actual = find_concatenations(s, tokens)
    assert len(actual) == 1

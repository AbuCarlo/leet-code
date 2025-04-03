'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words
'''

import collections
import random
import typing

import pytest
import hypothesis
from hypothesis import strategies


def find_concatenations(s: str, tokens: typing.List[str]) -> int:
    '''
    :param s: a string to search
    :param tokens: tokens, not necessarily unique
    :returns: the starting indices of every substring that is the
    concatenation of all the tokens
    '''

    def find_all_overlapping(token: str) -> typing.Iterator[int]:
        start = 0
        while True:
            i = s.find(token, start)
            if i == -1:
                break
            yield i
            start = i + 1

    anchor = random.choice(tokens)
    anchor_positions = list(find_all_overlapping(anchor))
    # All the tokens are the same length.
    token_counter = collections.Counter(tokens)
    token_length = len(tokens[0])
    # Group them by starting position % the token length.
    token_shifts = list(set(p % token_length for p in anchor_positions))
    all_results = []

    for shift in token_shifts:
        results = []
        # Slicing up the input is easier than lots of finicky substring matching.
        sliced = [s[i:i + token_length] for i in range(shift, len(s), token_length) if len(s) - i >= token_length]
        counter = collections.Counter(token_counter)
        match_size = 0
        for i, sl in enumerate(sliced):
            if sl not in token_counter:
                # Start again after this token.
                counter = collections.Counter(token_counter)
                match_size = 0
                continue
            if i - len(tokens) >= 0 and match_size == len(tokens):
                discard = sliced[i - len(tokens)]
                counter[discard] += 1
                match_size -= 1
            # If a count becomes negative, we have too many of this token.
            # The only to fix that is to go back and eliminate the first
            # one in the current match we're working on.
            counter[sl] -= 1
            match_size += 1
            if counter[sl] == 0:
                counter.pop(sl)
                if not counter:
                    results.append(i - len(tokens) + 1)
        all_results += [i * token_length + shift for i in results]



    return all_results


_SAMPLES = [
    ('barfoothefoobarman', ["foo", "bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ['bar', 'foo', 'the'], [6, 9, 12]),
    # test case #170
    ("aaaaaaaaaaaaaa", ["aa","aa"], 11),
    # test case #179
    ("bcabbcaabbccacacbabccacaababcbb", ["c","b","a","c","a","a","a","b","c"], len([6,16,17,18,19,20]))
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

@hypothesis.given(permute_tokens())
# pylint: disable=C0116
def test_permuted_tokens(t):
    s, tokens = t
    actual = find_concatenations(s, tokens)
    assert actual == 1

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
    token_length = len(tokens[0])
    # We may be given only two tokens, and they might be equal.
    # So there's not much point in looking for the best token.
    anchor = random.choice(tokens)
    anchor_positions = list(find_all_overlapping(anchor))
    # Group them by starting position % the token length.
    all_results = []
    # Read: https://docs.python.org/3/library/itertools.html#itertools.groupby
    anchor_positions.sort(key=lambda p: p % token_length)
    for remainder, positions in itertools.groupby(anchor_positions, lambda i: i % token_length):
        blah = list(positions)
        results = []
        # Slicing up the input is easier than lots of finicky substring matching. Get rid
        # of terminal tokens that are too short to match anyway.
        sliced = [s[i:i + token_length] for i in range(remainder, len(s), token_length) if len(s) - i >= token_length]

        for middle in (p // token_length for p in blah):
            counts = collections.Counter(tokens)
            # By definition, we've matched this token, so decrement the count.
            counts[anchor] -= 1
            if counts[anchor] == 0:
                counts.pop(anchor)
            last_match = -1 if not results else results[-1]
            # This will happen in the event of two equal tokens.
            if middle <= last_match:
                continue
            # Don't go any farther back than the highest solution so far.
            lower_limit = max(last_match, middle - len(tokens))
            i = middle
            for j in range(middle - 1, lower_limit, -1):
                if sliced[j] not in counts:
                    break
                i = j
                counts[sliced[j]] -= 1
                if counts[sliced[j]] == 0:
                    counts.pop(sliced[j])
            # This will only happen if we match every token.
            if len(counts) == 0:
                results.append(i)
                last_match = i
            # Now extend the window forward.
            upper_limit = min(len(sliced), middle + len(tokens))
            for k in range(middle + 1, upper_limit, 1):
                if sliced[k] not in token_set:
                    break
                # Move the lower edge of the window.
                if k - i == len(tokens):
                    counts[sliced[i]] += 1
                    if counts[sliced[i]] == 0:
                        counts.pop(sliced[i])
                    i += 1
                # This is wrong, but it's part of the way there.
                if sliced[k] not in counts:
                    break
                counts[sliced[k]] -= 1
                if counts[sliced[k]] == 0:
                    counts.pop(sliced[k])
                if len(counts) == 0:
                    results.append(i)
                    last_match = i
        # Translate these again.
        all_results += [remainder + r * token_length for r in results]

    all_results.sort()
    return all_results


_SAMPLES = [
    ('barfoothefoobarman', ["foo", "bar"], [0, 9]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], []),
    ("barfoofoobarthefoobarman", ['bar', 'foo', 'the'], [6, 9, 12]),
    # test case #170
    ("aaaaaaaaaaaaaa", ["aa","aa"], list(range(11))),
    # test case #179
    ("bcabbcaabbccacacbabccacaababcbb", ["c","b","a","c","a","a","a","b","c"], [6,16,17,18,19,20])
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
    assert actual == 1

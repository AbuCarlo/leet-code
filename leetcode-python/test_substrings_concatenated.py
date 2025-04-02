'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words
'''

import collections
import itertools
import random
import re

import pytest
import hypothesis
from hypothesis import strategies
from hypothesis import given


def find_concatenations(s: str, tokens: list[str]) -> int:
    # This is allowed by the problem definition.
    # TODO: Let the rest of the code handle this edge case.
    if len(tokens) == 1:
        positions = [m.start() for m in re.finditer(f"(?={tokens[0]})", s)]
        return len(positions)
    # All the tokens are the same length.
    token_set = set(tokens)
    token_length = len(tokens[0])
    # We may be given only two tokens, and they might be equal.
    # So there's not much point in looking for the best token.
    anchor = random.choice(tokens)
    # Hat-tip to https://stackoverflow.com/a/4664889/476942
    anchor_positions = [m.start() for m in re.finditer(f"(?={anchor})", s)]
    # Group them by starting position % the token length.
    anchor_positions = itertools.groupby(anchor_positions, lambda i: i % token_length)
    all_results = []
    # Todo go back and forth on either end.
    for remainder, positions in anchor_positions:
        results = []
        # Slicing up the input is easier than lots of finicky substring matching. Get rid
        # of terminal tokens that are too short to match anyway.
        sliced = [s[i:i + token_length] for i in range(remainder, len(s), token_length) if len(s) - i >= token_length]

        for middle in (p // token_length for p in positions):
            counts = collections.Counter(tokens)
            # By definition, we've matched this token, so decrement the count.
            counts[anchor] -= 1
            if counts[anchor] == 0:
                counts.pop(anchor)
            last_match = -1 if not results else results[-1]
            # This will happen in the event of two equal tokens.
            if middle < last_match:
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
            # Now extend the window forward.
            upper_limit = min(len(sliced), middle + len(tokens))
            for k in range(middle + 1, upper_limit, 1):
                if sliced[k] not in token_set:
                    break
                # Move the lower edge of the window.
                if k - i == len(tokens):
                    counts[sliced[i]] += 1
                    i += 1
                counts[sliced[k]] -= 1
                if counts[sliced[k]] == 0:
                    counts.pop(sliced[k])
                if len(counts) == 0:
                    results.append(i)
        # Translate these again.
        all_results += [remainder + r * token_length for r in results]

    return len(all_results)
    

_SAMPLES = [
    ('barfoothefoobarman', ["foo", "bar"], 2),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], 0),
    ("barfoofoobarthefoobarman", ['bar', 'foo', 'the'], 3),
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
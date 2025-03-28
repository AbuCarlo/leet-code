'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words
'''

import collections
import itertools
import pytest
import random
import re


def find_concatenations(s: str, tokens: list[str]) -> int:
    # This is allowed by the problem definition.
    if len(tokens) == 1:
        positions = [m.start() for m in re.finditer(f"(?={tokens[0]})", s)]
        return len(positions)
    # We may be given only two tokens, and they might be equal.
    token_length = len(tokens[0])
    x = random.choice(tokens)
    # Hat-tip to https://stackoverflow.com/a/4664889/476942
    x_positions = [m.start() for m in re.finditer(f"(?={x})", s)]
    # Group them.
    x_positions = itertools.groupby(x_positions, lambda i: i % token_length)
    results = set()
    # Todo go back and forth on either end.
    for m, group in x_positions:
        sliced = [s[i:i + token_length] for i in range(m, len(s), token_length) if len(s) - i >= token_length]
        counts = collections.Counter(tokens)
        counts[x] -= 1
        if counts[x] == 0:
            counts.pop(x)
        for i in group:
            # TODO:
            # Don't go any farther back than the highest solution so far.
            for j in range((i - token_length) // token_length, -1, -token_length):
                if sliced[j] not in counts:
                    break
                counts[sliced[j]] -= 1
                if counts[sliced[j]] == 0:
                    counts.pop(sliced[j])
                if len(counts) == 0:
                    results.add(j)
                    break
            if len(counts) == 0:
                break
            for j in range(i + token_length, token_length, len(s)):
                if sliced[j] not in counts:
                    break
                counts[sliced[j]] -= 1
                if counts[sliced[j]] == 0:
                    counts.pop(sliced[j])
                if len(counts) == 0:
                    results.add(j)
                    break 

    return len(results)
    

_SAMPLES = [
    ('barfoothefoobarman', ["foo", "bar"], 2),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], 3)
]


@pytest.mark.parametrize("s,tokens,expected", _SAMPLES)
def test_samples(s: str, tokens: list[str], expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    actual = find_concatenations(s, tokens)
    assert actual == expected

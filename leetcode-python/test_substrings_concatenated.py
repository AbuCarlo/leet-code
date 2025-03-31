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
    # TODO: Let the rest of the code handle this edge case.
    if len(tokens) == 1:
        positions = [m.start() for m in re.finditer(f"(?={tokens[0]})", s)]
        return len(positions)
    # All the tokens are the same length.
    token_length = len(tokens[0])
    # We may be given only two tokens, and they might be equal.
    # So there's not much point in looking for the best token.
    x = random.choice(tokens)
    # Hat-tip to https://stackoverflow.com/a/4664889/476942
    x_positions = [m.start() for m in re.finditer(f"(?={x})", s)]
    # Group them by starting position % the token length.
    x_positions = itertools.groupby(x_positions, lambda i: i % token_length)
    # This can simply be a list, right? 
    results = set()
    # Todo go back and forth on either end.
    for remainder, group in x_positions:
        # Slicing up the input is easier than lots of finicky substring matching. Get rid of the possible
        # initial token that's too short.
        sliced = [s[i:i + token_length] for i in range(remainder, len(s), token_length) if len(s) - i >= token_length]
        counts = collections.Counter(tokens)
        # By definition, we've matched this token, so decrement the count.
        counts[x] -= 1
        if counts[x] == 0:
            counts.pop(x)
        for i in (start // token_length for start in group):
            # TODO:
            # Don't go any farther back than the highest solution so far.
            for j in range(i - 1, max(results, default=0) // token_length, -1):
                if sliced[j] not in counts:
                    break
                counts[sliced[j]] -= 1
                if counts[sliced[j]] == 0:
                    counts.pop(sliced[j])
                if len(counts) == 0:
                    results.add(j * token_length + remainder)
                    break
            if len(counts) == 0:
                break
            for j in range(i + i, 1, len(sliced)):
                if sliced[j] not in counts:
                    break
                counts[sliced[j]] -= 1
                if counts[sliced[j]] == 0:
                    counts.pop(sliced[j])
                if len(counts) == 0:
                    results.add(j * token_length + remainder)
                    break
            # TODO Add a third loop to subtract and tokens.
            if len(counts) > 0:
                continue
            for j in range(max(results) // token_length + 1, i, 1):
                counts[sliced[j]] += 1
                if sliced[j + len(tokens) - 1] in counts:
                    counts[sliced[j]] -= 1
                    if counts[sliced[j]] == 0:
                        counts.pop(sliced[j])
                    if len(counts) == 0:
                        results.add(j * token_length + remainder)
                else:
                    continue
                    

    return len(results)
    

_SAMPLES = [
    ('barfoothefoobarman', ["foo", "bar"], 2),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"], 0),
    ("barfoofoobarthefoobarman", ['bar', 'foo', 'the'], 3)
]


@pytest.mark.parametrize("s,tokens,expected", _SAMPLES)
def test_samples(s: str, tokens: list[str], expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    actual = find_concatenations(s, tokens)
    assert actual == expected

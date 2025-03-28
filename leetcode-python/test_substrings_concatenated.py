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
    x, y = random.sample(tokens, 2)
    # Hat-tip to https://stackoverflow.com/a/4664889/476942
    left_positions = [m.start() for m in re.finditer(f"(?={left})", s)]
    right_positions = [m.start() for m in re.finditer(f"(?={right})", s)]
    if not left_positions or not right_positions:
        return 0
    # Group them.
    left_positions = itertools.groupby(left_positions, lambda i: i % token_length)
    right_positions = itertoos.groupby(right_positions, lambda i: i % token_length)
    result = 0
    # Todo go back and forth on either end.
    for m in range(token_length):
        sliced = [s[i:i + token_length] for i in range(m, len(s)) if len(s) - i >= token_length]
        for l in left_positions[m]:
            for r in right_positions[m]:
                # This will only happen if the tokens are equal. 
                if r != l:
                    continue
                # The matches are too far apart.
                if abs(r - l) // token_length > len(tokens) - 2:
                    continue
            

    return result
    

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

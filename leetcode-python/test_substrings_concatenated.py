'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words
'''

import itertools
import pytest
import re


def find_concatenations(s: str, tokens: list[str]) -> int:
    # I want two tokens with no letters in common.
    token_length = len(tokens[0])
    # I'd prefer to have tokens with no repeated letters.
    tokens.sort(key=lambda s: len(set(s)), reverse=True)
    left = tokens[0]
    left_set = set(left)
    # I'd prefer the next token to share no letters with the first. 
    right = next((t for t in itertools.islice(tokens, 1, None) if len(set(t) & left_set) == 0), tokens[1])
    # Hat-tip to https://stackoverflow.com/a/4664889/476942
    left_positions = [m.start() for m in re.finditer(f"(?={left})", s)]
    right_positions = [m.start() for m in re.finditer(f"(?={right})", s)]
    return 0
    

_SAMPLES = [
    ('barfoothefoobarman', ["foo", "bar"], 2)
]


@pytest.mark.parametrize("s,tokens,expected", _SAMPLES)
def test_samples(s: str, tokens: list[str], expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    actual = find_concatenations(s, tokens)
    assert actual == expected

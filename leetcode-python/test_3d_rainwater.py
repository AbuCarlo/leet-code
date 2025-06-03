'''
TODO: Put link to problem.
'''

from typing import List

import pytest

def get_standing_water(blah: List[List[int]]) -> int:
    ''' 
    How much water would be left standing here?
    '''
    height = len(blah)
    width = len(blah[0])

    ne = [[0 for _ in blah[0]] for _ in blah]
    sw = [[0 for _ in blah[0]] for _ in blah]

    def get_northeast_max(x, y) -> int:
        if x < 0 or x == width:
            return 0
        if y < 0 or y == height:
            return 0
        if ne[y][x] is not None:
            return ne[y][x]
        result = max(blah[y][x], get_northeast_max(y + 1, x), get_northeast_max(y, x + 1))
        ne[y][x] = result
        return result

    return 0

_SAMPLES = [
    # Any 1 x 1 of 2 x 2 problem will produce an answer of 0.
    ([[0]], 0),
    ([[1, 1], [1, 1]], 0),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1),
]


# pylint: disable=C0116
@pytest.mark.parametrize("blah, expected", _SAMPLES)
def test_test_cases(blah, expected):
    actual = get_standing_water(blah)
    assert actual == expected

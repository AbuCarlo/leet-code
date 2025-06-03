'''
TODO: Put link to problem.
'''

from typing import List

import pytest

def get_standing_water(heights: List[List[int]]) -> int:
    ''' 
    How much water would be left standing here?
    '''
    height = len(heights)
    width = len(heights[0])

    ne = [[0 for _ in heights[0]] for _ in heights]
    sw = [[0 for _ in heights[0]] for _ in heights]

    def get_northeast_max(column, row) -> int:
        if column < 0 or column == width:
            return 0
        if row < 0 or row == height:
            return 0
        if ne[row][column] is not None:
            return ne[row][column]
        result = max(
            heights[row][column],
            min(
                get_northeast_max(row + 1, column),
                get_northeast_max(row, column + 1)
            )
        )
        ne[row][column] = result
        return result

    def get_southwest_max(column, row) -> int:
        if column < 0 or column == width:
            return 0
        if row < 0 or row == height:
            return 0
        if sw[row][column] is not None:
            return sw[row][column]
        result = max(
            heights[row][column],
            get_southwest_max(row - 1, column),
            get_southwest_max(row, column - 1)
        )
        ne[row][column] = result
        return result

    get_northeast_max(0, 0)
    get_southwest_max(height - 1, width - 1)

    result = sum(min(ne[c][r], sw[c][r]) for c in range(height) for r in range(width))

    return result

_SAMPLES = [
    # Any 1 x 1 or 2 x 2 problem will produce an answer of 0.
    ([[0]], 0),
    ([[1, 1], [1, 1]], 0),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1),
]


# pylint: disable=C0116
@pytest.mark.parametrize("blah, expected", _SAMPLES)
def test_test_cases(blah, expected):
    actual = get_standing_water(blah)
    assert actual == expected

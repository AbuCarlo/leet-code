'''

'''

from dataclasses import dataclass
from typing import List

import pytest

@dataclass
class RainWater:
    """Class for keeping track of an item in inventory."""
    height: int
    left: int
    right: int

def trap_one(l: List[int]) -> List[RainWater]:
    current = (0, -1)
    from_left = [None] * len(l)
    for i, h in enumerate(l):
        if h >= current[0]:
            current = (h, i)
        from_left[i] = current
    current = (0, len(l))
    from_right = [None] * len(l)
    for i in range(len(l) - 1, -1, -1):
        h = l[i]
        if h >= current[0]:
            current = (h, i)
        from_right[i] = current
    blah = []
    for left, right in zip(from_left, from_right):
        r = RainWater(max(left[0], right[0]), left[1], right[1])
        blah.append(r)
    return blah

def trapRainWater(heightMap: List[List[int]]) -> int:
    return 0

_SAMPLES_2D = [
    ([3,3,3,3,3], 0),
    ([3,2,2,2,3], 3)
]

# pylint: disable=C0116
@pytest.mark.parametrize("l, expected", _SAMPLES_2D)
def test_samples(l, expected):
    traps = trap_one(l)
    actual = sum(t.height for t in traps)
    assert actual == expected

sample01 = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]

print(trapRainWater(sample01))

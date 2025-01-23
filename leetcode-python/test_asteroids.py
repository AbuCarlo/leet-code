'''
https://leetcode.com/problems/asteroid-collision
'''

from typing import List

import pytest


def asteroid_collision(asteroids: List[int]) -> List[int]:
    '''
    Iterate pairwise over the asteroids.
    '''
    result = []
    for a in asteroids:
        # Until we've dealt with a...
        while a is not None:
            # Both asteroids are moving in the same direction, or further apart.
            if not result or result[-1] < 0 or a > 0:
                result.append(a)
                a = None
            # Both asteroids explode.
            elif a == -result[-1]:
                result.pop()
                a = None
            # The current asteroid is larger.
            elif a < -result[-1]:
                # Continue iterating.
                result.pop()
            # The current asteroid explodes.
            else:
                a = None
    return result

_SAMPLES = [
    ([5, 10, -5], [5, 10]),
    ([8, -8], []),
    ([10, 2, -5], [10])
]


# pylint: disable=C0116
@pytest.mark.parametrize("asteroids, expected", _SAMPLES)
def test_test_cases(asteroids, expected):
    actual = asteroid_collision(asteroids)
    assert actual == expected

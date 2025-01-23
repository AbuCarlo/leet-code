'''
https://leetcode.com/problems/asteroid-collision
'''

from math import copysign
from typing import List

import pytest


def asteroid_collision(asteroids: List[int]) -> List[int]:
    '''
    Iterate pairwise over the asteroids.
    '''
    if not asteroids:
        return []
    while len(set(copysign(1, a) for a in asteroids)) > 1:
        i = 0
        l = []
        while i < len(asteroids):
            if i == len(asteroids) - 1:
                l.append(asteroids[i])
                break
            # If this asteroid is moving leftward, there can't be a collision.
            if copysign(1, asteroids[i]) < 0:
                l.append(asteroids[i])
                i += 1
            # Is the next asteroid moving leftward?
            elif copysign(1, asteroids[i + 1]) < 0:
                if abs(asteroids[i]) >= abs(asteroids[i + 1]):
                    # Both asteroids explode.
                    if abs(asteroids[i]) == abs(asteroids[i + 1]):
                        i += 2
                    # The next asteroid explodes.
                    else:
                        l.append(asteroids[i])
                        i += 2
                # This asteroid explodes.
                else:
                    l.append(asteroids[i + 1])
                    i += 2
            # These two asteroids are both moving rightward.
            else:
                l.append(asteroids[i])
                i += 1
        # No asteroids blew up.
        if len(asteroids) == len(l):
            break
        asteroids = l

    return asteroids


_SAMPLES = [
    ([5, 10, -5], [5, 10]),
    ( [8, -8], []),
    ([10, 2, -5], [10])
]


# pylint: disable=C0116
@pytest.mark.parametrize("asteroids, expected", _SAMPLES)
def test_test_cases(asteroids, expected):
    actual = asteroid_collision(asteroids)
    assert actual == expected

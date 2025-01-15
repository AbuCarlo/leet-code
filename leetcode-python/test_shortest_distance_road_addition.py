'''
https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i

There will be at most 500 nodes, and at most 500 roads.
'''

import collections
import bisect
import sys
from typing import List

import pytest

class Solution:
    '''
    LeetCode's usual structure.
    '''
    def __init__(self) -> None:
        self.n = sys.maxsize
        self.forward_distances = []

    def add_road(self, u, v):
        '''
        Add a road from u to v, recalculating the necessary shortest distances.
        '''
        # We've recalculated all the shortest distances from u back to the beginning,
        # so don't do it again until a road is added somewhere between 0 and u.
        # Mutatis mutandis for v.
        self.forward_distances[u][v] = 1
        for t in range(0, u + 1):
            for w in range(v, self.n):
                possible = self.forward_distances[t][u] + 1 + self.forward_distances[v][w]
                self.forward_distances[t][w] = min(self.forward_distances[t][w], possible)

    # pylint: disable=C0103
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        '''
        For every road in queries, recalculate the shortest distance from 0 to n - 1.
        Return a list of all recalculations.
        '''
        self.n = n
        self.forward_distances = []
        for i in range(n):
            self.forward_distances.append([0] * i + list(range(n - i)))

        results = []

        for u, v in queries:
            self.add_road(u, v)
            results.append(self.forward_distances[0][-1])

        return results

_SAMPLES = [
    (5, [[2,4],[0,2],[0,4]], [3,2,1]),
    # test case 400: roads join
    (6, [[1, 3],[3, 5]], [4, 3]),
    # test case 634: non-overlapping
    (7, [[4,6],[0,3]], [5,3]),
    # test case 696: non-overlapping
    (12, [[8,11],[0,2]], [9,8]),
    # test case #751
    (17, [[3, 12], [11, 16], [0, 4], [3, 9], [9, 12], [9, 13], [10, 16], [3, 10]], [8, 8, 8, 7, 7, 7, 6, 5]),
    # test case #876
    (47, [[2, 38], [9, 39], [41, 43]], [11, 11, 10]),
    # reduction of test case #876
    (12, [[2, 5], [4, 6], [8, 10]], [9, 9, 8])
]

@pytest.mark.parametrize("n,queries,expected", _SAMPLES)
def test_shortest_distance(n, queries, expected):
    '''
    Apply samples from LeetCode
    '''
    solution = Solution()
    actual = solution.shortestDistanceAfterQueries(n, queries)
    assert actual == expected

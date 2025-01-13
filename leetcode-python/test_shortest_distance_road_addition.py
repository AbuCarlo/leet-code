'''
https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i
'''

import collections
from typing import List
import sys

import pytest

class Solution:
    '''
    LeetCode's usual structure.
    '''
    def __init__(self) -> None:
        self.n = sys.maxsize
        self.result = sys.maxsize
        self.distance_forward = []
        self.distance_backward = []
        self.roads_forward = collections.defaultdict(set)
        self.roads_backward = collections.defaultdict(set)
        self.last_u = -1
        self.last_v = sys.maxsize

    def find_length_to_end(self, v) -> int:
        '''
        Recalculate the shortest distances for nodes between v and
        the end where roads have been added since the last call.
        '''
        if v < self.last_v:
            return self.distance_forward[v]
        current_min = min((1 + self.find_length_to_end(w)) for w in self.roads_forward[v])
        current_min = min(current_min, 1 + self.find_length_to_end(v + 1))
        self.distance_forward[v] = current_min
        return current_min

    def find_length_to_beginning(self, u):
        '''
        See above. Recalculate shortest distances back to the beginning.
        '''
        if u > self.last_u:
            return self.distance_backward[u]
        current_min = min((1 + self.find_length_to_beginning(w)) for w in self.roads_backward[w])
        current_min = min(current_min, 1 + self.find_length_to_beginning(u + 1))
        self.distance_backward[u] = current_min
        return current_min

    def add_road(self, u, v):
        '''
        Add a road from u to v, recalculating the necessary shortest distances.
        '''
        self.distance_forward[u] = 1 + self.find_length_to_end(v)
        self.distance_backward[v] = 1 + self.find_length_to_beginning(u)

        self.result = self.distance_backward[u] + 1 + self.distance_forward[v]

        self.roads_backward[v].add(u)
        self.roads_forward[u].add(v)
        # We've recalculated all the shortest distances from u back to the beginning,
        # so don't do it again until a road is added somewhere between 0 and u.
        # Mutatis mutandis for v.
        self.last_u = u
        self.last_v = v

    # pylint: disable=C0103
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        '''
        For every road in queries, recalculate the shortest distance from 0 to n - 1.
        Return a list of all recalculations.
        '''
        self.n = n
        self.result = n - 1
        self.distance_forward = list(range(n))
        self.distance_backward = reversed(list(range(n)))
        self.roads_backward.clear()
        self.roads_forward.clear()

        results = []

        for u, v in queries:
            self.add_road(u, v)
            results.append(self.result)

        return results

_SAMPLES = [
    (5, [[2,4],[0,2],[0,4]], [3,2,1]),
    # test case 400: roads join
    (6, [[1,3],[3,5]], [4,3]),
    # test case 634: non-overlapping
    (7, [[4,6],[0,3]], [5,3]),
    # test case 696: non-overlapping
    (12, [[8,11],[0,2]], [9,8])
]

@pytest.mark.parametrize("n,queries,expected", _SAMPLES)
def test_shortest_distance(n, queries, expected):
    '''
    Apply samples from LeetCode
    '''
    solution = Solution()
    actual = solution.shortestDistanceAfterQueries(n, queries)
    assert actual == expected

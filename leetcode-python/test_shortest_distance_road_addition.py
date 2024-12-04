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
        self.length_to_end = {}
        self.length_from_beginning = {}
        self.roads_to = collections.defaultdict(set)

    def find_length_to_end(self, u):
        return self.length_to_end.get(u, self.n - u - 1)

    def find_length_from_beginning(self, u):
        return self.length_from_beginning.get(u, u)

    def add_road(self, u, v):
        self.length_to_end[u] = min(self.find_length_to_end(u), 1 + self.find_length_to_end(v))
        self.result = min(self.result, u + self.length_to_end[u])
        for w in self.roads_to[u]:
            self.length_to_end[w] = min(self.find_length_to_end(w), 1 + self.length_to_end[u])
            self.result = min(self.result, self.find_length_from_beginning(w) + self.length_to_end[u])
        self.roads_to[v].add(u)

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        self.n = n
        self.result = n
        self.length_to_end.clear()
        self.length_from_beginning.clear()
        self.roads_to.clear()

        results = []

        for u, v in queries:
            self.add_road(u, v)
            results.append(self.result)

        return results

_SAMPLES = [
    (5, [[2,4],[0,2],[0,4]], [3,2,1])
]

@pytest.mark.parametrize("n,queries,expected", _SAMPLES)
def test_shortest_distance(n, queries, expected):
    '''
    Apply samples from LeetCode
    '''
    solution = Solution()
    actual = solution.shortestDistanceAfterQueries(n, queries)
    assert actual == expected

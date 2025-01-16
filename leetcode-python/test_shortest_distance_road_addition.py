'''
https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i

There will be at most 500 nodes, and at most 500 roads.
'''

from collections import deque
from typing import List

import pytest

class Solution:
    '''
    LeetCode's usual structure.
    '''

    # pylint: disable=C0103
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        '''
        For every road in queries, recalculate the shortest distance from 0 to n - 1 using
        breadth-first search. Nodes between u and v (exclusive) can be excluded.
        '''
        adjacency = [{v + 1: 1} for v in range(0, n - 1)]

        def bfs() -> int:
            '''
            https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
            '''
            q = deque([0])
            visited = set()
            path = {}
            while q:
                w = q.pop()
                # All paths have a length of 1. As soon as we encounter
                # the target in the queue, we've perforce found the
                # shortest path to it.
                if w == n - 1:
                    break
                for t in adjacency[w]:
                    if t in visited:
                        continue
                    visited.add(t)
                    path[t] = w
                    q.appendleft(t)

            result = 0
            t = n - 1
            # Trace the path from 0 simply to determine
            # it's length.
            while t > 0:
                result += 1
                t = path[t]
            return result

        results = []

        for u, v in queries:
            adjacency[u][v] = 1
            result = bfs()
            results.append(result)

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
def test_shortest_distance(n: tuple[int, list[list[int]], list[int]], queries: tuple[int, list[list[int]], list[int]], expected: tuple[int, list[list[int]], list[int]]):
    '''
    Apply samples from LeetCode
    '''
    solution = Solution()
    actual = solution.shortestDistanceAfterQueries(n, queries)
    assert actual == expected

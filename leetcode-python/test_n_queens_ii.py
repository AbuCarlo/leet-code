'''
https://leetcode.com/problems/n-queens-ii/
'''

import pytest

# pylint: disable=C0103
def totalNQueens(n: int) -> int:
    '''
    Recursive implementation using set()
    '''
    def internal_queens(row, columns, lefts, rights):
        if row == n:
            return 1
        result = 0
        for column in range(n):
            if column in columns or row + column in lefts or row - column in rights:
                continue
            result += internal_queens(row + 1, columns | set([column]), lefts | set([row + column]), rights | set([row - column]))
        return result
    return internal_queens(0, set(), set(), set())

print(totalNQueens(4))

_KNOWN_SOLUTIONS = [
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (5, 10),
    (6, 4),
    (7, 40),
    (8, 92),
    (9, 352),
    (10, 724)
]

@pytest.mark.parametrize("n,solutions", _KNOWN_SOLUTIONS)
def test_known_solutions(n: int, solutions: int):
    '''
    Test against known solutions. Cf. # See https://en.wikipedia.org/wiki/Eight_queens_puzzle
    '''
    actual = totalNQueens(n)
    assert actual == solutions

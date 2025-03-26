'''
https://leetcode.com/problems/n-queens-ii/
'''

import pytest

# pylint: disable=C0103
def totalNQueens(n: int) -> int:
    '''
    Recursive implementation using set()
    
    :param row: the row in which we're trying to place a queen
    :param columns: the set of columns already having a queeen
    '''
    def internal_queens(row, columns, lefts, rights):
        # The preceding iteration found a position
        # in the last row, i.e. n - 1. So we have
        # found another solution.
        if row == n:
            return 1
        result = 0
        for column in range(n):
            # Number the leftward diagonals by the sum of the coordinates.
            # There will be 2n -1 diagonals.
            left = row + column
            # Number the rightward diagonals similarly, but prevent negative values.
            right = row - column + n
            if 1 << column & columns or 1 << left & lefts or 1 << right & rights:
                continue
            result += internal_queens(row + 1, columns | 1 << column, lefts | 1 << left, rights | 1 << right)
        return result
    return internal_queens(0, 0, 0, 0)

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

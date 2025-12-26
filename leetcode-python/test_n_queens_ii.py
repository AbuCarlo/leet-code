'''
https://leetcode.com/problems/n-queens-ii/
'''

import pytest

# pylint: disable=C0103
def totalNQueensBitmasks(n: int) -> int:
    '''
    Recursive implementation using bitsets to represent 
    already occupied positions.

    :param n: the size of the board, i.e. n * n
    '''
    def internal_queens(row: int, columns: int, lefts: int, rights: int) -> int:
        '''
        :param row: the row in which we're trying to place a queen
        :param columns: the set of columns already having a queen
        :param rows: the set of rows etc.
        :param lefts: the set of leftward diagonals etc.
        :param rights: the set of rightward diagonals etc.
        '''
        # If we've placed a queen in every row up to now, we've 
        # found a solution.
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

# pylint: disable=C0103
def totalNQueensMemoized(n: int) -> int:
    '''
    Variant of the above, adding memoization to prevent O(n!) performance.
    '''

    memos = {}

    def internal_queens(row: int, columns: int, lefts: int, rights: int) -> int:
        if row == n:
            return 1

        key = (columns, lefts, rights)
        # The row doesn't have to form part of the key. 
        # For any value of row, all the bitsets will have
        # the same size (row).
        if key in memos:
            return memos[key]
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
        memos[key] = result
        return result

    return internal_queens(0, 0, 0, 0)


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

# It turns out that memoization does not improve the performance, most likely because the 
# dictionary grows very large. When n = 8, there are 1818 memos, but only 95 cache hits.
# Without memoization, the internal function is called 2057 times. Without, it's called
# 1999 times, making the memoization not worth the effort.
#
# Leetcode insists that actual sets use less memory than bitmasks, which baffles me.

@pytest.mark.parametrize("n,solutions", _KNOWN_SOLUTIONS)
def test_known_solutions(n: int, solutions: int):
    '''
    Test against known solutions. Cf. # See https://en.wikipedia.org/wiki/Eight_queens_puzzle
    '''
    actual = totalNQueensMemoized(n)
    assert actual == solutions

    actual = totalNQueensBitmasks(n)
    assert actual == solutions

# pylint: disable=C0116,W0613
@pytest.mark.parametrize("n,solutions", _KNOWN_SOLUTIONS[-3:])
def test_known_solutions_recursive(benchmark, n: int, solutions: int):
    benchmark(totalNQueensBitmasks, n)

# pylint: disable=C0116,W0613
@pytest.mark.parametrize("n,solutions", _KNOWN_SOLUTIONS[-3:])
def test_known_solutions_memoized(benchmark, n: int, solutions: int):
    benchmark(totalNQueensMemoized, n)

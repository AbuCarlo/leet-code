'''
https://leetcode.com/problems/n-queens
'''

import pytest

def solveNQueens(n: int):
    '''
    Recursive implementation using bitsets to represent 
    already occupied positions.

    :param n: the size of the board, i.e. n * n
    '''
    def print_solution(solution):
        # We know that no positions share a row.
        board = [None] * n
        for (row, column) in solution:
            s = ('.' * (column)) + 'Q' + ('.' * (n - column - 1))
            board[row] = s
        return board

    def internal_queens(row: int, columns: int, lefts: int, rights: int) -> int:
        for column in range(n):
            left, right = row + column, row - column + n - 1
            if 1 << column & columns or 1 << left & lefts or 1 << right & rights:
                continue
            position = (row, column)
            if row == n - 1:
                yield [position]
            subsolutions = internal_queens(row + 1, columns | 1 << column, lefts | 1 << left, rights | 1 << right)
            for s in subsolutions:
                yield [position] + s

    solutions = internal_queens(0, 0, 0, 0)

    return [print_solution(s) for s in solutions]

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
    actual = list(solveNQueens(n))
    assert len(actual) == solutions

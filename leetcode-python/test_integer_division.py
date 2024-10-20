import pytest

def integer_division(dividend, divisor):
    # TODO Add checks for 0, negative numbers.
    # TODO Write two functions, one that calls
    # the recursive workhorse.
    # These two conditions stop recursion.
    if dividend < divisor:
        return (0, dividend)
    if dividend < divisor + divisor:
        return (1, dividend - divisor)
    # TODO Rename these variables.    
    # The quotient must be at least 1.
    quotient, remainder = integer_division(dividend, divisor << 1)
    # The remainder must be somewhere from [0, divisor * 2]
    a, b = integer_division(remainder, divisor)
    return (quotient + quotient + a, b)

samples = [
    (0, 1, (0, 0)),
    (1, 1, (1, 0)),
    (2, 1, (2, 0)),
    (2, 2, (1, 0)),
    (8, 3, (2, 2)),
    (8, 5, (1, 3)),
    (1000, 33, (30, 10)),
    (44444444440, 2, (22222222220, 0))
]

@pytest.mark.parametrize('dividend, divisor, expected', samples)
def test_integer_division(dividend, divisor, expected):
    actual = integer_division(dividend, divisor)
    assert actual == expected

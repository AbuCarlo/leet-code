'''
https://leetcode.com/problems/divide-two-integers/description

The problem has some additional requirements at the extremes
of the range. These are not included here.
'''

import math

import hypothesis
import hypothesis.strategies

def internal_integer_division(dividend, divisor):
    # These two conditions stop recursion.
    if dividend < divisor:
        return (0, dividend)
    if dividend < (divisor << 1):
        return (1, dividend - divisor)
    quotient, remainder = internal_integer_division(dividend, divisor << 1)
    assert quotient >= 1
    # The remainder must be somewhere from [0, divisor * 2]
    a, b = internal_integer_division(remainder, divisor)
    return (quotient + quotient + a, b)

def integer_division(dividend: int, divisor: int):
    # The problem disallows 0.
    assert divisor != 0
    sign = int(math.copysign(1, dividend) * math.copysign(1, divisor))
    dividend = abs(dividend)
    divisor = abs(divisor)
    # The assignment doesn't include the remainder, and the
    # modulus operator with negatives is tricky anyway.
    quotient, _ = internal_integer_division(dividend, divisor)
    return sign * quotient


LIMIT = (1 << 31) - 1

@hypothesis.strategies.composite
def valid_arguments(draw):
    '''
    These are the bounds in the problem description.
    '''
    valid_range = hypothesis.strategies.integers(min_value=-LIMIT, max_value=LIMIT).filter(lambda x: x != 0)
    dividend = draw(valid_range)
    divisor = draw(valid_range)
    return (dividend, divisor)

@hypothesis.given(valid_arguments())
# pylint: disable=C0116
def test_integer_division(t):
    dividend, divisor = t
    actual = integer_division(dividend, divisor)
    # Python's // uses "floor division, so...
    quotient, remainder = divmod(dividend, divisor)
    if quotient < 0 and remainder != 0:
        # The quotient was rounded *down* in floor division.
        quotient += 1
    assert actual == quotient

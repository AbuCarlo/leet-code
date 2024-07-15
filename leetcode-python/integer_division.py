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

assert(integer_division(0, 1) == (0, 0))
assert(integer_division(1, 1) == (1, 0))
assert(integer_division(2, 1) == (2, 0))
assert(integer_division(2, 2) == (1, 0))
assert(integer_division(8, 3) == (2, 2))
assert(integer_division(8, 5) == (1, 3))



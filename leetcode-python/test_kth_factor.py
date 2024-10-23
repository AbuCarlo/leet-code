'''
https://leetcode.com/problems/the-kth-factor-of-n/
'''

import pytest
import sympy

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # A previous implementation found the prime factors,
        # then the powerset of the multiset of prime factors,
        # then the sum over multiplication of each set in the
        # powerset, which were then sorted...you get the idea.
        # This was all that Leetcode wanted.
        factors = [1]
        f = 2
        while f <= n // 2:
            if n % f == 0:
                factors.append(f)
            f += 1
        factors.append(n)
        return factors[k - 1] if k <= len(factors) else -1

samples = [
    (12, 3, 3),
    (7, 2, 7),
    (4, 4, -1)
]

@pytest.mark.parametrize("n, k, expected", samples)
def test_samples(n: int, k: int, expected: int):
    '''
    Test samples and test cases from Leetcode.
    '''
    solution = Solution()
    actual = solution.kthFactor(n, k)
    assert actual == expected
    # Create a property-based test.
    print(sympy.ntheory.factor_.divisors(n))
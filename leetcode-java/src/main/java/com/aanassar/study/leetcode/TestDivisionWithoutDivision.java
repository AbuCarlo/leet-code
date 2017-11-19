package com.aanassar.study.leetcode;

import org.junit.Test;

public class TestDivisionWithoutDivision {

	public int divide(int dividend, int divisor) {
		final boolean positive = (dividend & 0x8000000) == (divisor & 0x8000000);
		if (dividend < 0)
			dividend = -dividend;
		if (divisor < 0)
			divisor = -divisor;
		int result = 0;
		while (dividend >= divisor) {
			int shift = Integer.numberOfLeadingZeros(divisor) - Integer.numberOfLeadingZeros(dividend);
			int subtrahend = 
			dividend -= (divisor << shift);
		}
		return positive ? result : -result;
	}

	@Test
	public void testZero() {
		// assert divide(7, 1) == 7;
		// assert divide(7, 2) == 3;
		assert divide(7, -2) == -3;
		assert divide(7, 8) == 0;
		assert divide(10, 3) == 3;
	}
}

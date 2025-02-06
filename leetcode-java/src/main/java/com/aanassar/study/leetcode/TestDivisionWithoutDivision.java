package com.aanassar.study.leetcode;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.MatcherAssert.assertThat;

public class TestDivisionWithoutDivision {

	public int divide(int dividend, int divisor) {
		final boolean positive = (dividend & 0x8000000) == (divisor & 0x8000000);
		if (dividend < 0)
			dividend = -dividend;
		if (divisor < 0)
			divisor = -divisor;
		int result = 0;
		while (dividend >= divisor) {
			int shift = 0;
			while (dividend << shift < dividend) {
				++shift;
			}
			dividend -= (divisor << shift);
			result += 1 << shift;
		}
		return positive ? result : -result;
	}

	@Test
	public void testZero() {
		assert divide(7, 1) == 7;
		assert divide(7, 2) == 3;
		assert divide(7, 8) == 0;
		assert divide(10, 3) == 3;
	}

	@Test
	public void testPositiveNegative() {
		assert divide(7, -2) == -3;
	}

	@Test
	public void testNegativePositive() {
		assert divide(7, -2) == -3;
	}

	@Test
	public void testNegativeNegative() {
		assert divide(-7, -2) == 3;
	}

	@Test
	public void testFromSite() {
		int actual = divide(Integer.MIN_VALUE, -1);
		assertThat(actual, equalTo(2147483647));
	}
}

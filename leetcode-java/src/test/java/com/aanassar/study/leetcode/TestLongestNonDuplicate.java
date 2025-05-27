package com.aanassar.study.leetcode;

import org.junit.Before;
import org.junit.Test;

public class TestLongestNonDuplicate {

	static class Solution {
		public int lengthOfLongestSubstring(String s) {
			if (s.isEmpty())
				return 0;
			// As it happens, the inputs are all ASCII, so a small array here
			// would have been optimal. However, a map allows us to distinguish
			// between 0 and "not found."
			int[] seen = new int[Character.MAX_VALUE + 1];
			seen[s.charAt(0)] = 0;
			int result = 1;
			int start = 0;
			for (int i = 1; i < s.length(); ++i) {
				char c = s.charAt(i);
				if (seen[c] > 0) {
					start = Math.max(seen[c] + 1, start);
				}
				if (result < i - start + 1) {
					result = i - start + 1;
				}

				seen[c] = i;
			}
			return result;
		}
	}

	private Solution solution;

	@Before
	public void setUp() {
		this.solution = new Solution();
	}

	@Test
	public void testEmptyString() {
		assert solution.lengthOfLongestSubstring("") == 0;
	}

	@Test
	public void testStringWithNoRepetition() {
		assert solution.lengthOfLongestSubstring("abcdefg") == 7;
	}

	@Test
	public void abba() {
		assert solution.lengthOfLongestSubstring("abba") == 2;
	}

	@Test
	public void crap() {
		assert solution.lengthOfLongestSubstring("abcabcdabcde") == 5;
	}

}

package com.aanassar.study.leetcode;


import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

import java.util.*;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.MatcherAssert.assertThat;

@RunWith(Parameterized.class)
public class TestLongestIncreasingSubsequence {

    public static int longestIncreasingSubsequence(int[] a) {
        SortedMap<Integer, Integer> map = new TreeMap<>();
        for (int n : a) {
            var head = map.headMap(n);
            if (head.isEmpty()) {
                // There is no smaller value.
                map.put(n, 1);
                continue;
            }
            Map.Entry<Integer, Integer> e = head.lastEntry();
            int m = Math.max(e.getValue() + 1, map.getOrDefault(n, 0));
            map.put(n, m);
        }
        return map.values().stream().max(Integer::compareTo).orElse(0);
    }

    @Parameters
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][]{
                {new int[]{10, 9, 2, 5, 3, 7, 101, 18}, 4},
        });
    }

    @Parameterized.Parameter
    public int[] a;

    @Parameterized.Parameter(1)
    public int expected;

    @Test
    public void testSamples() {
        var actual = longestIncreasingSubsequence(a);
        assertThat(actual, equalTo(expected));
    }
}
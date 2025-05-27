package com.aanassar.study.leetcode;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.*;
import java.util.stream.IntStream;

/**
 * See <a href="https://leetcode.com/problems/count-good-triplets-in-an-array/description/">...</a>
 * <p>
 * The inputs are two arrays of the same length, containing the same values in different order.
 * Each array is just a permutation of the values [1, |a|]. A "good" triplet is a triple of
 * which the values are present in increasing order by position in both arrays. If the arrays
 * were identical, the number of good triplets would be (n - 2) * (n - 1) * (n - 2).
 * <p>
 * The problem becomes easy in a language that provides a binary search tree.
 */
@RunWith(Parameterized.class)
public class TestCountGoodTriplets {

    /**
     * The only purpose of this tree is to count the values less than,
     * and the values greater than, a given value. This is a trivial
     * case of a "range sum": a value can only occur once, so is added
     * to the tree only once. The sum of the values for nodes [0, n)
     * is simply the number of values < n that have been added to the
     * tree so far.
     */

    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return List.of(
                new Object[]{new int[]{2, 0, 1, 3}, new int[]{0, 1, 2, 3}, 1L},
                new Object[]{new int[]{4, 0, 1, 3, 2}, new int[]{4, 1, 0, 2, 3}, 4L}
        );
    }

    private final int[] l;

    private final int[] r;

    private final long expected;

    public TestCountGoodTriplets(int[] l, int[] r, long expected) {
        this.l = l;
        this.r = r;
        this.expected = expected;
    }

    @Test
    public void testCountGoodTriplets() {
        long actual = CountGoodTriplets.goodTriplets(l, r);
        Assert.assertEquals(expected, actual);
    }
}

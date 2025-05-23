package com.aanassar.study.leetcode;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Collection;
import java.util.List;

/**
 * See <a href="https://leetcode.com/problems/count-good-triplets-in-an-array/description/">...</a>
 */
@RunWith(Parameterized.class)
public class TestCountGoodTriplets {
    public int countGoodTriplets(int[] l, int[] r) {
        return 0;
    }

    @Parameterized.Parameters
    public static Collection<Object[]> data() {
        return List.of(
                new Object[]{new int[]{2, 0, 1, 3}, new int[]{0, 1, 2, 3}, 1},
                new Object[]{new int[]{4, 0, 1, 3, 2}, new int[]{4, 1, 0, 2, 3}, 4}
        );
    }

    private final int[] l;

    private final int[] r;

    private final int expected;

    public TestCountGoodTriplets(int[] l, int[] r, int expected) {
        this.l = l;
        this.r = r;
        this.expected = expected;
    }

    @Test
    public void testCountGoodTriplets() {
        int actual = countGoodTriplets(l, r);
        Assert.assertEquals(expected, actual);
    }
}

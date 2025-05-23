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

    record LesserGreater(int lesser, int greater) {}
    
    static class CustomTree {
        private final int[] lessers;
        private final int[] greaters;
        private final int root;

        CustomTree(int size) {
            // The index to these arrays is the actual value.
            // We are not implementing a binary tree, but only
            // simulating the descent in order to update these
            // values.
            this.lessers = new int[size];
            this.greaters = new int[size];
            int powerOfTwo = 1;
            do {
                powerOfTwo <<= 1;
            } while (powerOfTwo - 1 < size);
            this.root = (powerOfTwo >> 1) - 1;
        }
        
        void add(int n) {
            assert n < lessers.length;
            int r = this.root;
            int width = (this.root + 1) / 2;
            while (n != r) {
                if (n < r) {
                    ++this.lessers[r];
                    r -= width;
                } else {
                    ++this.greaters[r];
                    r += width;
                }
                width /= 2;
            }
        }

        LesserGreater find(int n) {
            assert n < lessers.length;
            return new LesserGreater(this.lessers[n], this.greaters[n]);
        }
    }
    
    public long goodTriplets(int[] l, int[] r) {
        // There is no neat way to do this without Guava 21.
        // To give credit where credit is due: https://stackoverflow.com/a/18552071/476942
        var withIndices = IntStream.range(0, l.length)
                .mapToObj(i -> new int[] { l[i], i })
                // Sort by the values.
                .sorted(Comparator.comparingInt(t -> t[0]))
                // Now extract the index of the value t[0].
                .mapToInt(t -> t[1])
                .toArray();
        // We know have an array mapping the values in l to their positions.
        var tree = new CustomTree(l.length);
        long result = 0L;
        // Now for each value in r, determine how many values preceding it *also*
        // preceded it in l.
        for (int j : r) {
            // Where was this value in l?
            int indexInLeft = withIndices[j];
            var tuple = tree.find(indexInLeft);
            // How many smaller indices into l are already in the tree?
            // How many larger indices are already in the tree? These cannot
            // be the third element of a good triplet. How many larger indices
            // are left over?
            long tripletsWithThisValue = (long) tuple.lesser * (r.length - indexInLeft - 1 - tuple.greater);
            result += tripletsWithThisValue;
            tree.add(indexInLeft);
        }
        return result;
    }

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
        long actual = goodTriplets(l, r);
        Assert.assertEquals(expected, actual);
    }
}

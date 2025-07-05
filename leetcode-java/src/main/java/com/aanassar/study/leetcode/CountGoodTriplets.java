package com.aanassar.study.leetcode;

import java.util.Comparator;
import java.util.stream.IntStream;

public class CountGoodTriplets {

    /**
     * This is an extremely simplified Fenwick tree. It can compute
     * the number of known values <= some value in O(log n) time.
     * No value should be added twice, but the implementation does
     * not bother checking.
     */
    static class FenwickTree {
        private final int[] tree;
        private int size;

        /**
         *
         * @param n the tree can accept values [0, n)
         */
        public FenwickTree(int n) {
            this.tree = new int[n];
            this.size = 0;
        }

        /**
         *
         * @param i this value is added to the tree, i.e. the value at the leaf node for this value
         *          is changed from 0 to 1.
         */
        public void add(int i) {
            for (; i < this.tree.length; i = i | (i + 1))
                ++this.tree[i];
            ++this.size;
        }

        public int getSize() {
            return this.size;
        }

        /**
         *
         * @param i a value in the input array
         * @return the number of values <= i
         */
        public int getPrefixSum(int i) {
            int result = 0;
            for (; i >= 0; i = (i & (i + 1)) - 1)
                result += this.tree[i];
            return result;
        }
    }

    static long goodTriplets(int[] l, int[] r) {
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
        var tree = new FenwickTree(l.length);
        long result = 0L;
        // Now for each value in r, find out its index in l. Any smaller indices
        // in the Fenwick tree represent smaller values that preceded j in both
        // arrays. Larger indices represent larger values that preceded it, and
        // can therefore not be part of a "good triplet" with j as the middle value.
        for (int j : r) {
            // Where was this value in l?
            int indexInLeft = withIndices[j];
            // How many smaller indices into l are already in the tree? The
            // prefix sum is inclusive, but since "indexInLeft" is making its
            // first appearance here, we don't have to subtract 1 from its prefix sum.
            long smaller = tree.getPrefixSum(indexInLeft);
            // How many larger indices are already in the tree? These cannot
            // be the third element of a good triplet. How many larger indices
            // are left over? "indexInLeft" has not yet been added to the tree,
            // so we don't need to add 1 for getPrefixSum().
            long larger = tree.getSize() - tree.getPrefixSum(indexInLeft);
            long tripletsWithThisValue = smaller * (r.length - indexInLeft - 1 - larger);
            result += tripletsWithThisValue;
            tree.add(indexInLeft);
        }
        return result;
    }

}

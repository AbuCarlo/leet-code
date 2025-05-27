package com.aanassar.study.leetcode;

import java.util.Comparator;
import java.util.stream.IntStream;

public class CountGoodTriplets {

    static class FenwickTree {
        private final int[] tree;
        private int size;

        public FenwickTree(int n) {
            this.tree = new int[n + 1];
            this.size = 0;
        }

        public void add(int i) {
            for (; i < this.tree.length; i = i | (i + 1))
                ++this.tree[i];
            ++this.size;
        }

        public int getSize() {
            return this.size;
        }

        public int countLesser(int i) {
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
            // How many smaller indices into l are already in the tree?
            long smaller = tree.countLesser(indexInLeft);
            // How many larger indices are already in the tree? These cannot
            // be the third element of a good triplet. How many larger indices
            // are left over? "indexInLeft" has not yet been added to the tree.
            long larger = tree.getSize() - tree.countLesser(indexInLeft);
            long tripletsWithThisValue = smaller * (r.length - indexInLeft - 1 - larger);
            result += tripletsWithThisValue;
            tree.add(indexInLeft);
        }
        return result;
    }

}

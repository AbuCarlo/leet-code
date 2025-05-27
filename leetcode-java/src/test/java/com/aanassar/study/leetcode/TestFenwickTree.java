package com.aanassar.study.leetcode;

//

import net.jqwik.api.*;

import java.util.stream.IntStream;

public class TestFenwickTree
{
    @Property
    boolean prefix_sum_equals_value(@ForAll("consecutiveIntegersShuffled") int[] values) {
        var tree = new CountGoodTriplets.FenwickTree(values.length);
        for (int v: values) {
            tree.add(v);
        }

        for (int v: values) {
            int prefix = tree.countLesser(v) - 1;
            if (prefix != v) {
                return false;
            }
        }
        return true;
    }

    @Provide
    Arbitrary<int[]> consecutiveIntegersShuffled() {
        int n = Arbitraries.integers().between(1, 5000).sample();
        var values = IntStream.range(0, n).boxed().toList();
        Arbitraries.shuffle(values);
        return Arbitraries.just(values.stream().mapToInt(Integer::valueOf).toArray());
    }
}

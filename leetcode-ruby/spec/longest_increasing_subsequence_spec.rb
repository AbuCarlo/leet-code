# frozen_string_literal: true

# https://leetcode.com/problems/longest-increasing-subsequence/description/
# https://ruby-doc.org/3.4.1/bsearch_rdoc.html
# https://github.com/tomykaira/rspec-parameterized
# https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeSet.html

require 'rspec-parameterized'
require 'rspec'

def longest_increasing_subsequence(a)
  if a.length == 0
    return 0
  end
  # Sort the array indices by the values!
  sorted_indices = (0...a.count).sort { |l, r|
    if a[l] == a[r]
      l <=> r
    else
      a[l] <=> a[r]
    end }
  found = [a[sorted_indices[0]]]
  prefix_lengths = { found[0] => 1 }
  sorted_indices[1..].map { |i| [i, a[i]] }.each do |i, n|
    insertion = found.bsearch_index { |e| e >= i }
    if insertion.nil?
      prefix_lengths[i] = prefix_lengths[found.last] + 1
      found.push(i)
    elsif n == a[found[insertion]]
      if n == 0
        next
      else

      end
    else
      prefix_lengths[i] = (prefix_lengths[found[insertion - 1]] || 0) + 1
      found.insert(insertion, i)
    end
  end
  prefix_lengths.values.max
end

describe "longest_increasing_subsequence" do
  where(:a, :expected) do
    [
      [[10, 9, 2, 5, 3, 7, 101, 18], 4],
      [[0, 1, 0, 3, 2, 3], 4],
      [[7, 7, 7, 7, 7, 7, 7], 1]
    ]
  end

  with_them do
    it "should produce expected answer" do
      actual = longest_increasing_subsequence(a)
      expect(actual).to eq(expected)
    end
  end
end
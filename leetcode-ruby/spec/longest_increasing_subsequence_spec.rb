# frozen_string_literal: true

# https://leetcode.com/problems/longest-increasing-subsequence/description/
# https://ruby-doc.org/3.4.1/bsearch_rdoc.html
# https://github.com/tomykaira/rspec-parameterized
# https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeSet.html

require 'rspec-parameterized'
require 'rspec'

def longest_increasing_subsequence(a)
  return 0 if a.empty?

  # Sort the array indices by the values, non-destructively,
  # i.e. if the values are equal, the higher index comes after.
  sorted_indices = (0...a.count).sort do |l, r|
    if a[l] == a[r]
      l <=> r
    else
      a[l] <=> a[r]
    end
  end
  # This should be a binary tree.
  found = [sorted_indices[0]]
  inserted_values = Set.new
  inserted_values.add(a[sorted_indices[0]])
  result = 1
  sorted_indices[1..].map { |i| [i, a[i]] }.each do |i, n|
    insertion = found.bsearch_index { |e| e > i }
    if insertion.nil?
      # We are appending to a run.
      result += 1 unless inserted_values.include?(n)
      found.push(i)
    else
      found.insert(insertion, i)
    end
    inserted_values.add(n)
  end
  result
end

describe 'longest_increasing_subsequence' do
  where(:a, :expected) do
    [
      [[10, 9, 2, 5, 3, 7, 101, 18], 4],
      [[0, 1, 0, 3, 2, 3], 4],
      [[7, 7, 7, 7, 7, 7, 7], 1]
    ]
  end

  with_them do
    it 'should produce expected answer' do
      actual = longest_increasing_subsequence(a)
      expect(actual).to eq(expected)
    end
  end
end

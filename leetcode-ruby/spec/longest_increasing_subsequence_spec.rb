# frozen_string_literal: true

# https://leetcode.com/problems/longest-increasing-subsequence/description/
# https://ruby-doc.org/3.4.1/bsearch_rdoc.html
# https://github.com/tomykaira/rspec-parameterized
# https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeSet.html

require 'prop_check'
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
  result = 1
  sorted_indices[1..].map { |i| [i, a[i]] }.each do |i, n|
    insertion = found.bsearch_index { |e| e > i }
    if insertion.nil?
      # We are appending to a run.
      result += 1 unless a[found.last] == n
      found.push(i) unless a[found.last] == n
    else
      found.insert(insertion, i) unless a[i] == n
    end
  end
  found.count
end

describe 'known test cases' do
  where(:a, :expected) do
    [
      [[10, 9, 2, 5, 3, 7, 101, 18], 4],
      [[0, 1, 0, 3, 2, 3], 4],
      [[7, 7, 7, 7, 7, 7, 7], 1],
      # test case 30
      [[1, 3, 6, 7, 9, 4, 10, 5, 6], 6]
    ]
  end

  with_them do
    it 'should produce expected answer' do
      actual = longest_increasing_subsequence(a)
      expect(actual).to eq(expected)
    end
  end
end

G = PropCheck::Generators

RSpec.describe 'generated arrays' do

  it 'returns an integer for any input' do
    PropCheck.forall(G.array(G.integer)) do |numbers|
      result = longest_increasing_subsequence(numbers)

      expect(result).to be_a(Integer)
    end
  end
end

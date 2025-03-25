# frozen_string_literal: true

# https://leetcode.com/problems/longest-increasing-subsequence/description/

require 'rspec-parameterized'
require 'rspec'

def longest_increasing_subsequence(numbers)
  return 0 if numbers.empty?

  lengths = { numbers.last => 1 }
  starting_values = [numbers.last]

  # In Python, use reverse iterator.
  numbers[0..-2].reverse.each do |number|
    tail_start = starting_values.bsearch_index { |i| i >= number }
    if tail_start.nil?
      # There is no larger value.
      lengths[number] = 1
      starting_values.push(number)
    elsif starting_values[tail_start] > number
      # What is the longest run to which we could prepend this value?
      lengths[number] = lengths.slice(*starting_values[tail_start..]).values.max + 1
      # Here's where a tree would be useful.
      starting_values.insert(tail_start, number)
    elsif tail_start < starting_values.count - 1
      # This value has already been encountered. If it's also the largest,
      # there's nothing to do, since this value is already at the end of a run.
      new_length = lengths.slice(*starting_values[tail_start + 1..]).values.max + 1
      lengths[number] = new_length if lengths[number] < new_length
    end
  end
  lengths.values.max
end

describe 'known test cases' do
  where(:numbers, :expected) do
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
      actual = longest_increasing_subsequence(numbers)
      expect(actual).to eq(expected)
    end
  end
end

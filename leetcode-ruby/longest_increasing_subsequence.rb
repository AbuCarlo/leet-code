# frozen_string_literal: true

# https://leetcode.com/problems/longest-increasing-subsequence/description/

Tuple = Struct.new(:value, :index)

def longest_subsequence(a)
  # TODO: Values first; if ==, then index.
  sorted_indices = (0...a.count).sort { |l, r| if a[l] == a[r] then l <=> r else a[l] <=> a[r] end }
  found = []
  prefix_lengths = {}
  sorted_indices.map { |i| [i, a[i] ]}.each do |i, n|
    # What is the largest value less than t.value?
    insertion = found.bsearch_index { |e| e >= n }
    if insertion.nil?
      found.unshift(n)
      prefix_lengths[n] = 1
    elsif found[insertion] == n
      prefix_lengths[n] = [(prefix_lengths[found[insertion - 1]] + 1), prefix_lengths[n]].max
    else
      prefix_lengths[n] = (prefix_lengths[found[insertion - 1]] || 0) + 1
      found.insert(insertion + 1, n)
    end
  end
  prefix_lengths.values.max
end

test_cases = {
  [10, 9, 2, 5, 3, 7, 101, 18] => 4
}

test_cases.each do |a, _b|
  actual = longest_subsequence(a)
  print actual
end
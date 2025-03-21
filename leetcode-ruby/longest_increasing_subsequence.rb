# frozen_string_literal: true

# https://leetcode.com/problems/longest-increasing-subsequence/description/
# https://ruby-doc.org/3.4.1/bsearch_rdoc.html
# https://github.com/tomykaira/rspec-parameterized
# https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/TreeSet.html

Tuple = Struct.new(:value, :index)

def longest_subsequence(a)
  if a.length == 0
    return 0
  end
  # Sort the array indices by the values!
  sorted_indices = (0...a.count).sort { |l, r| if a[l] == a[r] then l <=> r else a[l] <=> a[r] end }
  found = [a[sorted_indices[0]]]
  prefix_lengths = { found[0] => 1 }
  sorted_indices[1..].map { |i| [i, a[i]] }.each do |i, n|
    insertion = found.bsearch_index { |e| e >= n - 1 }
    if insertion.nil?
      prefix_lengths[i] = prefix_lengths[found.last] + 1
      found.push(i)
    elsif a[found[insertion]] == n
      prefix_lengths[i] = [(prefix_lengths[found[insertion - 1]] + 1), prefix_lengths[n]].max
    else
      prefix_lengths[i] = (prefix_lengths[found[insertion - 1]] || 0) + 1
      found.insert(insertion + 1, i)
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
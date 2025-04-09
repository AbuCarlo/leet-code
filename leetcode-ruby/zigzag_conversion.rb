# frozen_string_literal: true

def convert(s, num_rows)
  if num_rows == 1
    return s
  end
  modulus = 2 * num_rows - 2
  result = [''] * num_rows
  s.each_char.with_index do |c, i|
    if i % modulus < num_rows
      result[i % modulus] += c
    else
      result[num_rows - 1 - (i % modulus) - 1] += c
    end

  end
  result.join('')
end

actual = convert('PAYPALISHIRING', 3)
puts actual
# Output: "PAHNAPLSIIGYIR"

puts convert('PAYPALISHIRING', 4)
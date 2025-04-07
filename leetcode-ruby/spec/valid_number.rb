# https://leetcode.com/problems/valid-number

# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.
#
# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
#
# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.

def is_number(s)
  exponent = s =~ /e\d+\z/i
  if exponent
    s = s[0...exponent]
  end

  is_integer(s) || is_decimal(s)

end

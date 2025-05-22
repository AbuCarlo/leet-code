# frozen_string_literal: true

# https://leetcode.com/problems/valid-number
#
# Given a string s, return whether s is a valid number.
#
# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14",
# "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789",
# while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5",
# "--6", "-+3", "95a54e53".
# Formally, a valid number is defined using one of the following definitions:
#
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
  # Can an exponent have leading 0s?
  exponent = s =~ /e[+-]?\d+\z/i
  s = s[0...exponent] if exponent
  # It turns out that nothing is faster than just using a regex.
  !(s =~ /^[+-]?((\d+)(\.\d*)?|(\.\d+))$/).nil?
end

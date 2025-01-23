'''
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
'''

from collections import Counter
from typing import List


def count_k_sum_pairs(nums: List[int], k: int) -> int:
    c = Counter(nums)
    result = 0
    # Copy the counts.
    for n, count in c.items():
        if n > k // 2:
            continue
        if k % 2 == 0 and n == k // 2:
            result += count // 2
        else:
            result += min(count, c[k - n])
    return result

# assert count_k_sum_pairs([1,2,3,4], 5) == 2
assert count_k_sum_pairs([3,1,3,4,3], 6) == 1

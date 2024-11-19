'''
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
'''
import collections
from typing import List

# pylint: disable=C0103
def maximumSubarraySum(nums: List[int], k: int) -> int:
    if k > len(nums):
        raise ValueError()
    # Are there negative numbers?
    result = 0
    #
    counts = collections.Counter(nums[:k])
    current_sum = sum(nums[:k])
    if len(counts) == k:
        result = current_sum
    for i in range(k, len(nums)):
        counts[nums[i - k]] -= 1
        current_sum -= nums[i - k]
        current_sum += nums[i]
        if counts[nums[i - k]] == 0:
            del counts[i - k]
        counts[nums[i]] += 1
        if len(counts) == k:
            result = max(result, current_sum)
    return result

print(maximumSubarraySum([9,9,9,1,2,3], 3))

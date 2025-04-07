## Problem

https://leetcode.com/problems/largest-divisible-subset

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

## Solution

First we should realize that if `nums[i] % nums[j] == 0`, then `nums[i] > nums[j]`. So we can sort the array and process the numbers in increasing order.

The next key fact is that if `nums[i] % nums[j] == 0` and `nums[j] % nums[k] == 0` where `nums[i] > nums[j] > nums[k]`, then `nums[i] % nums[k] == 0`. (`nums[i]` is a multiple of `nums[j]` and `nums[j]` is a multiple of `nums[k]`, so `nums[i]` is a multiple of `nums[k]`.)

So if `nums[i] % nums[j] == 0` then we can add `nums[i]` to any subset answer where `nums[j]` is the maximum, since all other numbers in that subset are divisible by `nums[j]`, and hence by `nums[i]`.

This gives us a DP solution we can use to find the length of the maximum subset answer where `nums[i]` is the maximum for each `i`. Once we know which number the maximum subset answer ends in we can retrace our steps to construct the subset.

## Code
```
from collections import deque

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [0] * len(nums)
        prev = [-1] * len(nums)
        nums.sort()
        for i in range(len(nums)):
            maxSequenceLength = 1
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > maxSequenceLength:
                    maxSequenceLength = dp[j] + 1
                    prev[i] = j
            dp[i] = maxSequenceLength
        maxLength = 0
        currIndex = -1
        for i, length in enumerate(dp):
            if length > maxLength:
                currIndex = i
                maxLength = length
        res = deque()
        while currIndex != -1:
            res.appendleft(nums[currIndex])
            currIndex = prev[currIndex]
        return list(res)
```
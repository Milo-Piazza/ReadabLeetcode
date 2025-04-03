## Problem

https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii

You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

Note: this is identical to https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i but with larger test cases.

## Solution

We can solve this in one pass in O(n): 
For each number `num` at index k assume we've tracked the maximum value of `(nums[i] - nums[j])` in `maxDiff` for all `i < j < k`. Then we can easily update the result using `num` and `maxDiff`. The only thing we need to do afterwards is update `maxDiff`. To do this, we need to keep track of the maximum element we've seen so far in `currMax`, in which case `maxDiff` is at least `currMax - num`.

## Code
```
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        currMax = 0
        maxDiff = 0
        res = 0
        for num in nums:
            res = max(res, num * maxDiff)
            currMax = max(num, currMax)
            maxDiff = max(currMax - num, maxDiff)
        return res
```
## Notes

See also the series of stock sale problems, since tracking `maxDiff` is equivalent to 121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/.
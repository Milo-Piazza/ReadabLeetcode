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
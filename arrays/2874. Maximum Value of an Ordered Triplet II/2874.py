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
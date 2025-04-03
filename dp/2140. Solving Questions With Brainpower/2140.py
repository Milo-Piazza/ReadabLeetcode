class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions)+1)
        for i in range(len(questions)-1, -1, -1):
            points, brainpower = questions[i]
            resumeAt = min(i + brainpower + 1, len(questions))
            dp[i] = max(dp[i+1], points + dp[resumeAt])
        return dp[0]
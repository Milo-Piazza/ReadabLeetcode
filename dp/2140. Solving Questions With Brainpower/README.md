## Problem

https://leetcode.com/problems/solving-questions-with-brainpower/

You are given a 0-indexed 2D integer array questions where questions[i] = [points<sub>i</sub>, brainpower<sub>i</sub>].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you points<sub>i</sub> points but you will be unable to solve each of the next brainpower<sub>i</sub> questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = \[\[3, 2\], \[4, 3\], \[4, 4\], \[2, 5\]\]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

## Solution

This is pretty straightforward DP.

Define $dp[i]$ to be the maximum number of points for the subarray starting at index i.

The base case is $dp[N] = 0$ where $N$ is greater than or equal to the length of `questions`, since the sum for an empty array is 0.

For each question at index $i$, we have two options:
- skip question $i$, in which case $dp[i] = dp[i+1]$.
- solve question $i$, in which case we have to skip brainpower~i~ problems, so $dp[i] = points_i + dp[i + brainpower_i + 1]$.



## Code
```
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions)+1)
        for i in range(len(questions)-1, -1, -1):
            points, brainpower = questions[i]
            resumeAt = min(i + brainpower + 1, len(questions))
            dp[i] = max(dp[i+1], points + dp[resumeAt])
        return dp[0]
```
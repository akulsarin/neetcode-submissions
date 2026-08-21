class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        currSum = sum(cardPoints[:k])
        currMax = currSum
        for i in range(1, k + 1):
            currSum -= cardPoints[k - i]
            currSum += cardPoints[-i]
            currMax = max(currSum, currMax)
        return currMax



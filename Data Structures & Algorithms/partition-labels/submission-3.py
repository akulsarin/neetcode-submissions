class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndices = {}
        for i, char in enumerate(s):
            lastIndices[char] = i

        N = len(s)
        ans = []        
        l = 0
        currMax = lastIndices[s[0]]
        for r in range(N):
            currMax = max(currMax, lastIndices[s[r]])
            if r == currMax:
                ans.append(r - l + 1)
                l = r + 1
                continue

        return ans



        
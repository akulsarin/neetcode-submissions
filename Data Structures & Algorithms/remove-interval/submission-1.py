class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        for interval in intervals:
            if toBeRemoved[0] > interval[1] or toBeRemoved[1] < interval[0]:
                ans.append(interval)
                continue

            if interval[0] < toBeRemoved[0] < interval[1]:
                ans.append([interval[0], toBeRemoved[0]])
            
            if interval[0] < toBeRemoved[1] < interval[1]:
                ans.append([toBeRemoved[1], interval[1]])

        return ans


            
        
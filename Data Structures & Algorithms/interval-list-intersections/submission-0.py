class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        M, N = len(firstList), len(secondList)
        i = j = 0
        ans = []
        while i < M and j < N:
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            if end1 < start2:
                i += 1
            elif end2 < start1:
                j += 1
            else:
                intersection = [max(start1, start2), min(end1, end2)]
                ans.append(intersection)
                if end2 >= end1:
                    i += 1
                if end1 >= end2:
                    j += 1
        
        return ans
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]

        idx = bisect.bisect(arr, x)
        l, r = idx - 1, idx
        res = deque([])
        while len(res) < k:
            lNum = arr[l] if l >= 0 else float('inf')
            rNum = arr[r] if r < N else float('inf')
            if abs(lNum - x) <= abs(rNum - x):
                res.appendleft(lNum)
                l -= 1
            else:
                res.append(rNum)
                r += 1
        
        return [i for i in res]
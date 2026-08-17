class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        res = 1
        l = 0
        
        mult = 1
        for r in range(1, N):
            if (mult * arr[r - 1]) < (mult * arr[r]):
                mult *= -1
            else:
                if arr[r - 1] == arr[r]:
                    l = r
                else:
                    l = r - 1
                mult = -1 if arr[r - 1] < arr[r] else 1
            res = max(res, r - l + 1)
        return res
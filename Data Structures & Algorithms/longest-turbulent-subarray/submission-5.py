class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 1

        l = 0
        mul = 1 if arr[1] > arr[0] else -1
        res = 1

        for r in range(1, len(arr)):
            if (mul * arr[r]) > (mul * arr[r - 1]):
                res = max(res, r - l + 1)
                mul *= -1
            else:
                if r == len(arr) - 1:
                    break
                elif arr[r] == arr[r - 1]:
                    l = r
                    mul = 1 if arr[r + 1] > arr[r] else -1 
                else:
                    l = r - 1

        return res




        
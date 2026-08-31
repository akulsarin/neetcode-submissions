class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 1:
            return 1
        
        l = 0
        max_len = 1
        prev_comp = "="
        for r in range(len(arr) - 1):
            if prev_comp in {"<", "="} and arr[r] > arr[r + 1]:
                prev_comp = ">"
            elif prev_comp in {">", "="} and arr[r] < arr[r + 1]:
                prev_comp = "<"
            elif arr[r] != arr[r + 1]:
                l = r
                prev_comp = ">" if arr[r] > arr[r + 1] else "<"
            else:
                l = r + 1
                prev_comp = "="
            max_len = max(max_len, r - l + 2)
        
        return max_len
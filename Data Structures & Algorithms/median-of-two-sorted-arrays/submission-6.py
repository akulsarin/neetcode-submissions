class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        M, N = len(nums1), len(nums2)
        TOTAL = M + N
        HALF = TOTAL // 2
        
        l, r = 0, M
        while l <= r:
            mid1 = (l + r) // 2
            mid2 = HALF - mid1

            maxLeft1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            minRight1 = nums1[mid1] if mid1 < M else float('inf')

            maxLeft2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            minRight2 = nums2[mid2] if mid2 < N else float('inf')

            if minRight1 >= maxLeft2 and minRight2 >= maxLeft1:
                if TOTAL % 2:
                    return min(minRight1, minRight2)
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif minRight1 < maxLeft2:
                l = mid1 + 1
            elif minRight2 < maxLeft1:
                r = mid1 - 1
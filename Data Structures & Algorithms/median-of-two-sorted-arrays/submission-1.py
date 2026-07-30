class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsCombined = []
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] <= nums2[i2]:
                numsCombined.append(nums1[i1])
                i1 += 1
            else:
                numsCombined.append(nums2[i2])
                i2 += 1

        if i1 < len(nums1):
            numsCombined += nums1[i1:]
        elif i2 < len(nums2):
            numsCombined += nums2[i2:]

        i = len(numsCombined) // 2
        if len(numsCombined) % 2 == 0:
            return (numsCombined[i] + numsCombined[i - 1]) / 2
        else:
            return numsCombined[i]
        
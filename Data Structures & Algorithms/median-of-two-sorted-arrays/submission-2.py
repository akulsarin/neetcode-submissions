class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smaller, longer = nums1, nums2
        if len(nums2) < len(nums1):
            smaller, longer = longer, smaller
        
        totalLength = len(smaller) + len(longer)
        isEven = totalLength % 2 == 0
        halfLength = (totalLength + 1) // 2

        l, r = 0, len(smaller)

        while l <= r:
            smallerCut = (l + r) // 2
            longerCut = halfLength - smallerCut

            smallerLeft = smaller[smallerCut - 1] if smallerCut > 0 else float('-inf')
            smallerRight = smaller[smallerCut] if smallerCut < len(smaller) else float('inf')
            
            longerLeft = longer[longerCut - 1] if longerCut > 0 else float('-inf')
            longerRight = longer[longerCut] if longerCut < len(longer) else float('inf')

            if smallerLeft <= longerRight and longerLeft <= smallerRight:
                if isEven:
                    return (max(smallerLeft, longerLeft) + min(smallerRight, longerRight)) / 2
                else:
                    return max(smallerLeft, longerLeft)
            elif smallerLeft > longerRight:
                r = smallerCut - 1
            else:
                l = smallerCut + 1

        return smaller[l]


"""
    t    |    l    |    r    |    sCut    |    lCut    |
    1         0         0           0            0
"""
  
        
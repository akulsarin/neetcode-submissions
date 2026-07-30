class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m, n
        while p1 > 0 and p2 > 0:
            num1, num2 = nums1[p1 - 1], nums2[p2 - 1]
            if num1 >= num2:
                nums1[p1 + p2 - 1] = num1
                p1 -= 1
            else:
                nums1[p1 + p2 - 1] = num2
                p2 -= 1
            
        if p1 > 0:
            nums1[:p1 + p2] = nums1[:p1]
        elif p2 > 0:
            nums1[:p1 + p2] = nums2[:p2]
            
        
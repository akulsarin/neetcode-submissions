class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_temp = [nums1[i] for i in range(m)]
        p1 = p2 = 0
        while p1 < m and p2 < n:
            num1, num2 = nums1_temp[p1], nums2[p2]
            if num1 <= num2:
                nums1[p1 + p2] = num1
                p1 += 1
            else:
                nums1[p1 + p2] = num2
                p2 += 1
            
        if p1 < m:
            nums1[p1 + p2:] = nums1_temp[p1:]
        elif p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
            
        
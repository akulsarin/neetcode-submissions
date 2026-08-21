class SparseVector:
    def __init__(self, nums: List[int]):
        self.indicesToVals = {}
        for i, num in enumerate(nums):
            self.indicesToVals[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for idx in (self.indicesToVals.keys() & vec.indicesToVals.keys()):
            ans += (self.indicesToVals[idx] * vec.indicesToVals[idx])
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

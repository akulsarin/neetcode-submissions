class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        for i, num in enumerate(nums):
            prevPrefix = 0 if i == 0 else self.prefix[i - 1]
            self.prefix.append(prevPrefix + num)

        
    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = 0 if left == 0 else self.prefix[left - 1]
        return rightSum - leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
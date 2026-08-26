class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        slow_2 = 0
        while slow != slow_2:
            slow = nums[slow]
            slow_2 = nums[slow_2]
        
        return slow
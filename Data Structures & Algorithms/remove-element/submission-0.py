class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        num_found = 0
        for i in range(len_nums - 1, -1, -1):
            curr_num = nums[i]
            if curr_num == val:
                nums[-1 - num_found], nums[i] = nums[i], nums[-1 - num_found]
                num_found += 1
        nums = nums[num_found:]
        return len_nums - num_found
        
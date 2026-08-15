class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        target = N - 1
        queue = deque([0])
        while queue:
            for _ in range(len(queue)):
                currIdx = queue.popleft()
                maxJump = nums[currIdx]
                if maxJump >= target - currIdx:
                    return True
                nums[currIdx] = 0
                for i in range(currIdx + 1, min(target, currIdx + maxJump + 1)):
                    queue.append(i)
                print(queue)
        return False
                    


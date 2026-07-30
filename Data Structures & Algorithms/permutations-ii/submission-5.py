class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        counts = {n: 0 for n in nums}
        for n in nums:
            counts[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in counts:
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1

                    dfs()

                    counts[n] += 1
                    perm.pop()

        dfs()
        return res
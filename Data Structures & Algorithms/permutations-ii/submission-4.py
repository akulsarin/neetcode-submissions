class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            nextPerms = set()
            for perm in perms:
                for i in range(len(perm) + 1):
                    permCopy = list(perm)
                    permCopy.insert(i, num)
                    nextPerms.add(tuple(permCopy))
            perms = list(nextPerms)

        return perms
        
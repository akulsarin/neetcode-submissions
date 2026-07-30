class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms =[[]]

        for num in nums:
            nextPerms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    permCopy = perm.copy()
                    permCopy.insert(i, num)
                    nextPerms.append(permCopy)
            perms = nextPerms

        return perms
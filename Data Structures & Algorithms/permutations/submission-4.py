class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[nums[0]]]

        for num in nums[1:]:
            new_perms = []
            for perm in permutations:
                for i in range(0, len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, num)
                    new_perms.append(perm_copy)
            permutations = new_perms
        
        return permutations
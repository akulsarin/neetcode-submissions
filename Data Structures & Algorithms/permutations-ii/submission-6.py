class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        counts = Counter(nums)
        permutations = []
        
        def backtrack(curr: List[int]):
            if len(curr) == N:
                permutations.append(curr.copy())
                return

            for num, count in counts.items():
                if count:
                    counts[num] -= 1
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
                    counts[num] += 1
        
        backtrack([])
        return permutations
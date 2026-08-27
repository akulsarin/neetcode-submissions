class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        combinations = []

        def backtrack(i: int, t: int, curr: List[int]):
            if t == 0:
                combinations.append(curr.copy())
                return
            if t < 0 or i >= N:
                return
            
            num = candidates[i]
            curr.append(num)
            backtrack(i + 1, t - num, curr)
            curr.pop()
            j = i + 1
            while j < N and candidates[j] == num:
                j += 1
            backtrack(j, t, curr)
        
        backtrack(0, target, [])
        return combinations
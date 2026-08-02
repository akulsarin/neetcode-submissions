class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        combinations = []

        def dfs(i: int, currComb: List[int], t: int):
            if t == 0:
                combinations.append(currComb.copy())
                return
            elif i == N or t < 0:
                return

            currComb.append(candidates[i])
            dfs(i + 1, currComb, t - candidates[i])
            currComb.pop()
            j = i
            while j < N and candidates[j] == candidates[i]:
                j += 1
            dfs(j, currComb, t)

        dfs(0, [], target)
        return combinations
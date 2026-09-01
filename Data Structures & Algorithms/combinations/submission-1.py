class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(i: int, curr: List[int]):
            if i > n:
                if len(curr) == k:
                    combinations.append(curr[::])
                return
            if len(curr) > k:
                return
            
            backtrack(i + 1, curr)
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
        
        backtrack(1, [])
        return combinations
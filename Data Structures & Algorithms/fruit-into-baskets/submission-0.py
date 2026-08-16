class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxPick = 0
        typesPicked = defaultdict(int)

        l = 0
        for r in range(len(fruits)):
            typesPicked[fruits[r]] += 1
            while len(typesPicked) > 2:
                typesPicked[fruits[l]] -= 1
                if typesPicked[fruits[l]] == 0:
                    del typesPicked[fruits[l]]
                l += 1
            maxPick = max(maxPick, r - l + 1)
        return maxPick
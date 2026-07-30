class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping: Dict[str, List[str]] = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(digitIdx: int, curr: List[str], res: List[str]) -> None:
            if len(curr) == len(digits):
                comb = "".join(curr)
                if comb:
                    res.append(comb)
                return

            digitChars = mapping[digits[digitIdx]]
            for char in digitChars:
                curr.append(char)
                dfs(digitIdx + 1, curr, res)
                curr.pop()

        res = []
        dfs(0, [], res)
        return res
            
        
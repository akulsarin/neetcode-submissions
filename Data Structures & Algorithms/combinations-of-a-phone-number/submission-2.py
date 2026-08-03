class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        N = len(digits)
        result = []
        if N == 0:
            return result

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
        def dfs(curr: List[str], i: int) -> None:
            if i == N:
                result.append("".join(curr))
                return

            for char in mapping[digits[i]]:
                curr.append(char)
                dfs(curr, i + 1)
                curr.pop()

        dfs([], 0)
        return result
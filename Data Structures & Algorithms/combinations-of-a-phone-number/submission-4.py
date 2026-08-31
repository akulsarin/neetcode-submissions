class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_chars = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz",
        }
        N = len(digits)
        combinations = []

        def backtrack(i: int, curr: List[str]) -> None:
            if i == N:
                if curr:
                    combinations.append("".join(curr))
                return

            for char in digit_to_chars[digits[i]]:
                curr.append(char)
                backtrack(i + 1, curr)
                curr.pop()
            
        backtrack(0, [])
        return combinations
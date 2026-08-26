class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "]": "[", "}": "{"}
        open_brackets = set(close_to_open.values())
        
        stack = []
        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif not stack or stack.pop() != close_to_open[char]:
                return False
        
        return not stack
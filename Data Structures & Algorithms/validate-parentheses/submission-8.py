class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpened = {')': '(', '}': '{', ']': '['}

        stack = []
        for c in s:
            if c in closedToOpened:
                if not stack or closedToOpened[c] != stack.pop():
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

        
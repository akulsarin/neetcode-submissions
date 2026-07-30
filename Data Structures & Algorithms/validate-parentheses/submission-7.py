class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpened = {')': '(', '}': '{', ']': '['}
        openBrackets = set(closedToOpened.values())

        stack = []
        for c in s:
            if c in openBrackets:
                stack.append(c)
            else:
                if not stack or closedToOpened[c] != stack.pop():
                    return False

        return len(stack) == 0

        
class Solution:
    def isValid(self, s: str) -> bool:
        def is_open_bracket(c: str) -> bool:
            return c in {'(', '[', '{'}

        def get_correct_open_bracket(c: str) -> str:
            if c == ')':
                return '('
            elif c == ']':
                return '['
            elif c == '}':
                return '{'
            else:
                raise ValueError(f"Unrecognized open bracket: {c}")

        stack = []
        for c in s:
            if is_open_bracket(c):
                stack.append(c)
            else:
                # It is a closing bracket
                try:
                    last_open = stack.pop()
                except IndexError:
                    return False
                    
                correct_open = get_correct_open_bracket(c)
                if last_open != correct_open:
                    return False

        return len(stack) == 0


        
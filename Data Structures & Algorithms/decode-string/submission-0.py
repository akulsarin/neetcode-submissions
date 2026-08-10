class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        stack = []

        i = 0
        while i < N:
            char = s[i]
            if char != "]":
                stack.append(char)
            else:
                patternList = []
                while stack[-1] != "[":
                    patternList.append(stack.pop())
                stack.pop()
                patternString = "".join(reversed(patternList))
                

                freq = 0
                base = 1
                while stack and stack[-1].isdigit():
                    digit = int(stack.pop())
                    freq += base * digit
                    base *= 10
                
                stack.append(patternString * freq)
             
            i += 1

        return "".join(stack)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
                continue

            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()

        res = []
        for char, count in stack:
            res += [char] * count
        
        return "".join(res)
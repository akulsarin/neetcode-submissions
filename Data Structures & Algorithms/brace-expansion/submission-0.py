class Solution:
    def getOptions(self, s: str) -> List[List[str]]:
        N = len(s)
        options = []
        i = 0
        while i < N:
            c = s[i]
            if 'a' <= c <= 'z':
                options.append([c])
            elif c == "{":
                i += 1
                ops = []
                while s[i] != "}":
                    if 'a' <= s[i] <= 'z':
                        ops.append(s[i])
                    i += 1
                options.append(ops)
            i += 1
        return options

    def expand(self, s: str) -> List[str]:
        options = self.getOptions(s)
        N = len(options)
        res = []
        
        def backtrack(i: int, curr: List[str]):
            if i == N:
                res.append("".join(curr))
                return

            for op in options[i]:
                curr.append(op)
                backtrack(i + 1, curr)
                curr.pop()
        
        backtrack(0, [])
        return res
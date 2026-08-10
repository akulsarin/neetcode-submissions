class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openingRemoval = []
        closingRemoval = []

        for i, c in enumerate(s):
            if c == "(":
                openingRemoval.append(i)
            elif c == ")":
                if not openingRemoval:
                    closingRemoval.append(i)
                else:
                    openingRemoval.pop()

        removalIndices = set(openingRemoval + closingRemoval)
        res = []
        for i, c in enumerate(s):
            if i not in removalIndices:
                res.append(c)

        return "".join(res)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sourceChars = {c for c in source}
        for c in target:
            if c not in sourceChars:
                return -1

        M, N = len(source), len(target)
        i = j = 0
        while j < N:
            iMod = i % M
            if source[iMod] == target[j]:
                j += 1
            i += 1
        
        if (i % M) == 0:
            return i //M
            
        return (i // M) + 1

        
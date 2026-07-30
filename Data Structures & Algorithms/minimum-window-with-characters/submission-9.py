class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sLen = len(s)
        tLen = len(t)

        tCharCounts = {c: 0 for c in t}
        for c in t:
            tCharCounts[c] += 1
        matchLen = len(tCharCounts)

        matches = 0
        sCharCounts = {c: 0 for c in s}
        # for c in range

        minL, minR = 0, float('inf')
        found = False
        l = 0
        for r in range(sLen):
            rChar = s[r]
            
            sCharCounts[rChar] += 1
            if rChar in tCharCounts:
                if sCharCounts[rChar] == tCharCounts[rChar]:
                    matches += 1

            while matches == matchLen:
                found = True
                lChar = s[l]
                sCharCounts[lChar] -= 1
                if lChar in tCharCounts:
                    if r - l < minR - minL:
                        minL, minR = l, r
                    if sCharCounts[lChar] == tCharCounts[lChar] - 1:
                        matches -= 1
                l += 1

        if not found:
            return ""
        return s[minL : minR + 1]








        
        


            


        
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Ensure s is the smaller string
        if len(t) < len(s):
            s, t = t, s

        if abs(len(s) - len(t)) > 1:
            return False
        elif len(s) == 0 and len(t) == 1:
            return True

        i = j = 0
        editMade = False
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                if editMade:
                    return False
                editMade = True
                if len(s) < len(t):
                    j += 1
                elif len(s) == len(t):
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1

        return editMade or len(s) != len(t)



        